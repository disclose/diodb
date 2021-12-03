import os
import sys
import json
import string
import logging
import argparse
import urllib.parse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", default="programs", help="output directory")
    parser.add_argument("file", type=argparse.FileType("r"), help="program-list.json")
    return parser.parse_args()


def main():
    args = parse_args()

    with args.file as f:
        program_list = json.load(f)

    for d in string.digits + string.ascii_lowercase:
        os.makedirs(os.path.join(args.o, d), exist_ok=True)

    for program in program_list:
        if is_platform(program):
            continue

        slug = to_slug(program)
        alnum = to_first_alnum(slug)

        for i in range(0, 1337):
            filename = to_filename(slug, i)
            filepath = os.path.join(args.o, alnum, filename)
            if not os.path.isfile(filepath):
                with open(filepath, "w") as fp:
                    json.dump(program, fp, indent=4, sort_keys=True)
                break


def is_platform(program):
    # https://github.com/disclose/bug-bounty-platforms/blob/edbfc11ad07b642dc6daa1a712c1fb8389fdfbf2/README.md
    # cat README.md|grep -oE 'https?://[a-zA-Z0-9./_-]+'|cut -d '/' -f 3|sort -u|sed "s/^/'/g; s/$/',/g"|grep -vE 'github\.com'
    platforms = [
        "app.cobalt.io",
        "app.crowdswarm.io",
        "bugbounty.jp",
        "bugbounty.vn",
        "bugcrowd.com",
        "bughunt.com.br",
        "hackenproof.com",
        "hackerone.com",
        "hckrt.com",
        "huntr.dev",
        "immunefi.com",
        "intigriti.com",
        "safevuln.com",
        "securityat.me",
        "whitehub.net",
        "www.antihack.me",
        "www.cyberarmy.id",
        "www.hacktify.eu",
        "www.intigriti.com",
        "www.openbugbounty.org",
        "www.redstorm.io",
        "www.vulbox.com",
        "www.vulnerability-lab.com",
        "www.vulnscope.com",
        "www.zerodayinitiative.com",
        "yeswehack.com",
    ]

    _, netloc, _, _, _ = urllib.parse.urlsplit(program["policy_url"])
    if netloc in platforms:
        return True
    else:
        return False


def to_slug(program):
    url = None

    if program["policy_url"]:
        url = program["policy_url"]
    else:
        raise Exception(f"no url in program: {program}")

    if not url.startswith("https://") and not url.startswith("http://"):
        url = "https://" + url

    _, netloc, _, _, _ = urllib.parse.urlsplit(url)
    slug = netloc.replace(".", "_").replace(":", "_").lower()
    return slug


def to_first_alnum(slug):
    for l in slug:
        if l.isalpha() or l.isdigit():
            return l

    raise Exception(f"no alphas in slug: {slug}")


def to_filename(slug, integer):
    if integer == 0:
        return f"{slug}.json"
    else:
        return f"{slug}.{integer}.json"


if __name__ == "__main__":
    main()
