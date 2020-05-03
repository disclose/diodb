#!/usr/bin/python3

# Adaptation of convert+to_csv.py (github.com/disclose/disclose/tree/master/tools/Convert%20JSON%20to%20CSV)
# removing the conversion part and leaving only the sorting and dumping of a json file.

import argparse
import csv
import json
import sys
from collections import OrderedDict

# Add commandline arguments.
parser = argparse.ArgumentParser()
required = parser.add_argument_group('Required Arguments')
required.add_argument('-j', '--jsonfile', help='Input json file', type=str)
required.add_argument('-oj', '--outfile-json', help='Output json file name', type=str)
args = parser.parse_args()

# Ensure proper arguments are given, and warn for missing ones.
if None in (args.jsonfile, args.outfile_json):
    if args.jsonfile is None: 
        print("Error: input json file (-j/--jsonfile) is required")
    if args.outfile_json is None:
        print("Error: Output JSON filename (-oj/--outfile-json) is required")
    sys.exit(0)

# Open and load JSON file. Load as utf-8, due to non-ascii characters in some names.
with open(args.jsonfile, 'r', encoding='utf-8') as f:
    programs = json.load(f, object_pairs_hook=OrderedDict)

# Sort list alphabetically and dump to file.
# Converting key to lowercase is to ensure proper sorting, as capitals are given preference over lowercase.
# This can lead to a situation such where the list goes Zynga Whitehat -> cPanel.
programs.sort(key=lambda a: a['program_name'].lower())
output_json = json.dump(programs, open(args.outfile_json, "w", encoding='utf8'), indent=2, ensure_ascii=False)
