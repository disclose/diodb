const core = require('@actions/core');
const fsPromises = require('fs').promises;
const http = require('http');
const https = require('https');
const zlib = require('zlib');
require('tls').DEFAULT_MIN_VERSION = 'TLSv1';


const MAX_CONCURRENT_REQUESTS = 8;
// Check at most this many URLs concurrently. Giving this a higher value
// makes it faster up to a certain point, but we may run into 429 Too Many
// Requests responses (e.g. by sending requests to many URLs from different
// programs on the same bug bounty platform). With too many concurrent
// requests, we may also hit other resource limits.
const PROGRAM_LIST_FILE = './program-list.json';
const SOCKET_IDLE_TIMEOUT = 10 * 1000; // 10 seconds


(() => {
  const streamToString = (stream, encoding) => {
    return new Promise((resolve, reject) => {
      const chunks = [];
      stream.on('data', (chunk) => chunks.push(chunk));
      stream.on('error', reject);
      stream.on('end', () => resolve(Buffer.concat(chunks).toString(encoding)));
    });
  };

  const decompressResponseBody = async (incomingMessage) => {
    return new Promise(async (resolve, reject) => {
      let encoding;
      try {
        encoding = incomingMessage.headers['content-type'].split('=')[1].trim()
            .toLowerCase() === 'iso-8859-1'? 'latin1': 'utf8';
      } catch (error) {
        encoding = 'utf8';
      }

      const contentEncodingHeader = incomingMessage.headers['content-encoding'];
      let responseBodyStream;
      switch (
        contentEncodingHeader? contentEncodingHeader.toLowerCase(): 'identity'
      ) {
        case 'br':
          responseBodyStream = incomingMessage.pipe(
              zlib.createBrotliDecompress());
          break;
        case 'gzip':
          responseBodyStream = incomingMessage.pipe(zlib.createGunzip());
          break;
        case 'deflate':
          responseBodyStream = incomingMessage.pipe(zlib.createInflate());
          break;
        default:
          responseBodyStream = incomingMessage;
      }
      responseBodyStream.on('error', (error) => {
        reject(
            new Error(`Error decompressing response body: ${error.message}.`));
      });

      resolve(
          await streamToString(responseBodyStream, encoding).catch((error) => {
            reject(error);
          }));
    });
  };

  const headers = { // To get past some bot detection based on headers
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,' +
      'image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;' +
      'q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en-GB;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 ' +
      '(KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
  };
  const tryingGETMsg = 'Trying GET...';

  const tryHEADRequest = (protocol, url) => {
    return new Promise((resolve, reject) => {
      const headMsgIntro = 'HEAD: ';
      const clientRequest = protocol.request(url, {
        'headers': headers,
        'method': 'HEAD',
      }, async (incomingMessage) => {
        incomingMessage.on('aborted', () => {
          // "...if the response closes prematurely, the response object does
          // not emit an 'error' event but instead emits the 'aborted' event."
          reject(new Error(headMsgIntro + 'The response closed prematurely.'));
        });

        const statusCode = incomingMessage.statusCode;
        // http.ClientRequest: "...the data from the response object must be
        // consumed..."
        incomingMessage.resume();

        if ([200, 302, 303, 307].includes(statusCode)) {
          resolve(true);
        } else {
          let additionalInfo;
          if ([301, 308].includes(statusCode)) {
            additionalInfo = '\nLocation: ' +
                `${incomingMessage.headers['location']}`;
          } else { // including 404
            additionalInfo = tryingGETMsg;
          }
          reject(new Error(headMsgIntro + `${incomingMessage.statusCode} ` +
              `${incomingMessage.statusMessage}. ${additionalInfo}`));
        }
      }).setTimeout(SOCKET_IDLE_TIMEOUT, () => {
        clientRequest.destroy();
        reject(new Error(headMsgIntro +
            `Socket timed out after more than ${SOCKET_IDLE_TIMEOUT / 1000}` +
            ' seconds of inactivity. ' + tryingGETMsg));
      }).on('error', (error) => {
        clientRequest.destroy();
        reject(new Error(headMsgIntro + error.message + '. ' + tryingGETMsg));
      }).end();
    });
  };

  const tryGETRequest = (protocol, url) => {
    return new Promise((resolve, reject) => {
      const getMsgIntro = 'GET: ';
      const clientRequest = protocol.get(url, {
        'headers': headers,
      }, async (incomingMessage) => {
        incomingMessage.on('aborted', () => {
          reject(new Error(getMsgIntro + 'The response closed prematurely.'));
        });

        const statusCode = incomingMessage.statusCode;
        if ([200, 302, 303, 307].includes(statusCode)) {
          resolve(true);
        } else {
          let additionalInfo;
          if (statusCode === 404) {
            additionalInfo = '';
          } else if ([301, 308].includes(statusCode)) {
            additionalInfo = '\nLocation: ' +
                `${incomingMessage.headers['location']}`;
          } else {
            additionalInfo = '\nHeaders: ' +
                `${JSON.stringify(incomingMessage.headers, null, 2)}`;
            await decompressResponseBody(incomingMessage).then((value) => {
              additionalInfo += `\nBody: ${value}`;
            }, (error) => {
              incomingMessage.resume();
              additionalInfo += '\nResponse body decompression error: ' +
                  `${error.message}.`;
            });
          }
          incomingMessage.resume();
          reject(new Error(getMsgIntro +
             `${incomingMessage.statusCode} ` +
             `${incomingMessage.statusMessage}. ${additionalInfo}`));
        }
      }).setTimeout(SOCKET_IDLE_TIMEOUT, () => {
        clientRequest.destroy();
        reject(new Error(getMsgIntro +
            `Socket timed out after more than ${SOCKET_IDLE_TIMEOUT / 1000}` +
            ' seconds of inactivity.'));
      }).on('error', (error) => {
        clientRequest.destroy();
        reject(new Error(getMsgIntro + error.message));
      });
    });
  };

  const checkPolicyURL = async (program) => {
    return new Promise(async (resolve, reject) => {
      let url;
      try {
        url = new URL(program.policy_url);
      } catch (error) {
        reject(new Error('Not a URL.'));
        return;
      }

      let protocol;
      if (url.protocol === 'https:') {
        protocol = https;
      } else if (url.protocol === 'http:') {
        protocol = http;
      } else {
        reject(new Error('URL protocol not HTTPS or HTTP.'));
        return;
      }

      try {
        await tryHEADRequest(protocol, url);
        resolve(true);
      } catch (error) {
        if (error.message.endsWith(tryingGETMsg)) {
          const headErrorMsg = error.message;
          try {
            await tryGETRequest(protocol, url);
            resolve(true);
          } catch (error) {
            reject(new Error(headErrorMsg + '\n' + error.message));
          }
        } else {
          reject(error);
        }
      }
    });
  };

  /*
   * Like arrayOfValues.map(promiseFunc), which would return an array of
   * promises -- but limits the maximum number of concurrent pending promises
   * at any one time to `maxNumberOfPendingPromises`, and returns a promise for
   * the array.
   */
  const throttled = (promiseFunc, arrayOfValues,
      maxNumberOfPendingPromises) => {
    return new Promise((resolve, reject) => {
      const results = [];
      let arrayOfValuesIndex = 0;
      const lastArrayIndex = arrayOfValues.length - 1;
      const addPromise = () => {
        if (arrayOfValuesIndex < lastArrayIndex) {
          const promise = promiseFunc(arrayOfValues[arrayOfValuesIndex]);
          promise.then(addPromise, addPromise);
          results.push(promise);
        } else if (arrayOfValuesIndex === lastArrayIndex) {
          results.push(promiseFunc(arrayOfValues[arrayOfValuesIndex]));
          resolve(results);
        }
        ++arrayOfValuesIndex;
      };
      for (let i = 0; i < maxNumberOfPendingPromises &&
          i < arrayOfValues.length; ++i) {
        addPromise();
      }
    });
  };


  const main = async () => {
    let file;
    try {
      file = await fsPromises.readFile(PROGRAM_LIST_FILE, 'utf8');
    } catch (error) {
      core.setFailed(error.message);
      return;
    }

    let programsList;
    try {
      programsList = JSON.parse(file);
    } catch (error) {
      core.setFailed(error.message);
      return;
    }

    console.log(
        `Checking policy URLs for ${programsList.length} programs...\n`);

    Promise.allSettled(await throttled(checkPolicyURL, programsList,
        MAX_CONCURRENT_REQUESTS)).then((results) => {
      let invalidURLsCount = 0;
      for (const [index, result] of results.entries()) {
        const program = programsList[index];
        if (program.policy_url_status == "dead"){
          continue
        }
        const programInfo = `${index + 1}. ${program.program_name} ` +
            `(${program.policy_url}): `;
        if (result.status === 'rejected') {
          ++invalidURLsCount;
          console.log(programInfo + `${result.reason.message}\n`);
        }
      }
      if (invalidURLsCount) {
        const moreThanOneInvalidURL = (invalidURLsCount > 1);
        core.setFailed(`${invalidURLsCount} policy URL` +
            `${moreThanOneInvalidURL? 's': ''} ` +
            `require${moreThanOneInvalidURL? '': 's'} attention.`);
      } else {
        console.log('\nAll policy URLs appear to be valid.\n');
      }
    });
  };

  let done = false;
  try {
    main().then(() => { done = true; });
  } catch (error) {
    core.setFailed(error.message);
    done = true;
  };

  // Prevent process from exiting until main() promise is settled (See
  // https://github.com/nodejs/node/issues/22088)
  const noExitUntilPromiseSettled = () => {
    if (!done) { setTimeout(noExitUntilPromiseSettled, 1000); }
  };
  noExitUntilPromiseSettled();
})();

