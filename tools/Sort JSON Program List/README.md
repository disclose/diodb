# Sort JSON Program List Alphabetically

This tool is designed to take program-list.json, and export an alphabetically sorted json file. 

```bash
# Authors:      prodigysml <https://github.com/prodigysml>
#               Sick.Codes <https://github.com/sickcodes>
# License:      MIT
# Copyright:    CC 2020 Disclose.io

pipenv run pip install -r requirements.txt
pipenv run python sort-diodb.py
jq < program-list.json > program-list.json.tmp
mv program-list.json.tmp program-list.json

```
