import sys
import json
import argparse
import urllib.parse



def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=argparse.FileType('r'), help='program-list.json')
    return parser.parse_args()


def main():
    args = parse_args()

    with args.file as f:
        program_list = json.load(f)
    
    for program in program_list:
        if not is_platform(program):
            print(to_slug(program))


def is_platform(program):
    # https://github.com/disclose/bug-bounty-platforms/blob/edbfc11ad07b642dc6daa1a712c1fb8389fdfbf2/README.md
    # cat README.md|grep -oE 'https?://[a-zA-Z0-9./_-]+'|cut -d '/' -f 3|sort -u|sed "s/^/'/g; s/$/',/g"|grep -vE 'github\.com'
    platforms = [
        'app.cobalt.io',
        'app.crowdswarm.io',
        'bugbounty.jp',
        'bugbounty.vn',
        'bugcrowd.com',
        'bughunt.com.br',
        'hackenproof.com',
        'hackerone.com',
        'hckrt.com',
        'huntr.dev',
        'immunefi.com',
        'intigriti.com',
        'safevuln.com',
        'securityat.me',
        'whitehub.net',
        'www.antihack.me',
        'www.cyberarmy.id',
        'www.hacktify.eu',
        'www.intigriti.com',
        'www.openbugbounty.org',
        'www.redstorm.io',
        'www.vulbox.com',
        'www.vulnerability-lab.com',
        'www.vulnscope.com',
        'www.zerodayinitiative.com',
        'yeswehack.com',
    ]

    _, netloc, _, _, _ = urllib.parse.urlsplit(program['policy_url'])
    if netloc in platforms:
        return True
    else:
        return False


def to_slug(program):
    _, netloc, _, _, _ = urllib.parse.urlsplit(program['policy_url'])
    return netloc.replace('.', '_')


if __name__ == '__main__':
    main()