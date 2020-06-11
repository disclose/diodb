# validate-links
Validate programs' policy_urls, and flag the ones that appear to be invalid.

Check that each policy_url is a URL; and with a HEAD request, check that the response is 200 OK, 302 Found, 303 See Other or 307 Temporary Redirect. If yes, the URL is considered valid.

If not, but the response is 301 Moved Permanently or 308 Permanent Redirect, print the program name and URL with the redirect location.

With any other response or error, next try a GET request. If response is 200, 302, 303 or 307, the URL is considered valid. With any other response or error, print the program name and URL, together with information on the HEAD and GET responses or errors.

Finally, if any policy_url(s) require attention, print a count of the number of them that do; otherwise print a message indicating that all the policy_urls appear to be valid.

(Note: Because of bot detection measures, IP blocking, etc., some policy_urls may respond differently to this checker than how they would respond to a normal browser, so some results may need to be checked again in a browser.)
