#!/usr/bin/python3

# Adaptation of convert_to_csv.py (github.com/disclose/disclose/tree/master/tools/Convert%20JSON%20to%20CSV)
# removing the conversion part and leaving only the sorting and dumping of a json file.

import argparse
import csv
import json
import sys
from collections import OrderedDict
import copy

# Add commandline arguments.
parser = argparse.ArgumentParser()
parser.add_argument('-j', '--jsonfile', default='program-list.json', help='Input json file', type=str)
parser.add_argument('-oj', '--outfile-json', default='program-list.json', help='Output json file name', type=str)
args = parser.parse_args()

# Open and load JSON file. Load as utf-8, due to non-ascii characters in some names.
with open(args.jsonfile, 'r', encoding='utf-8') as f:
    programs = json.load(f, object_pairs_hook=OrderedDict)

# Copy json.
programs_sorted = copy.deepcopy(programs)
# Sort alphabetically.
# Converting key to lowercase is to ensure proper sorting, as capitals are given preference over lowercase.
# This can lead to a situation such where the list goes Zynga Whitehat -> cPanel.
programs_sorted.sort(key=lambda a: a['program_name'].lower())
# Compare the original json with the sorted one and dump to file if they are different.
if programs_sorted == programs:
    print("File is sorted, everything is fine")
else:
    print("Uh-oh, some things are out of order")
    output_json = json.dump(programs_sorted, open(args.outfile_json, "w", encoding='utf8'), indent=2, ensure_ascii=False)
    print("Writed fixed json to " + args.outfile_json)
