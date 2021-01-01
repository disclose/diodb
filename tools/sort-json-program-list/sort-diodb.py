#!/usr/bin/python
# Authors:      prodigysml <https://github.com/prodigysml>
#               Sick.Codes <https://github.com/sickcodes>
# License:      MIT
# Copyright:    CC 2020 Disclose.io

import json
import pandas as pd

def main():
    gh_url = "https://raw.githubusercontent.com/disclose/diodb/master/program-list/program-list.json"
    df_gh = pd.read_json(gh_url)
    df_gh.fillna('', inplace=True)
    df_gh.set_index('program_name', drop=False, inplace=True)
    df_gh_sorted = df_gh.iloc[df_gh.program_name.str.lower().argsort()]
    # df_gh.sort_index(inplace=True)
    f = open('program-list.json', 'w')
    f.write(json.dumps(df_gh_sorted.to_dict(orient='records')))
    f.close

if __name__ == "__main__":
    main()
