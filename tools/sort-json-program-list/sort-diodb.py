#!/usr/bin/python
# Authors:      prodigysml <https://github.com/prodigysml>
#               Sick.Codes <https://github.com/sickcodes>
# License:      MIT
# Copyright:    CC 2021 Disclose.io

import json
import pandas as pd
import sqlite3

DB_FILE = 'program-list.sqlite'
DB_TBLE = 'diodb'

def create_empty_table(filename):
    conn = sqlite3.connect(filename)
    c = conn.cursor()
    c.execute('''CREATE TABLE "diodb" ( "null" TEXT NULL );''')
    conn.commit()
    conn.close()





class ExtendTable(object):
    def __init__(self, dbtable, df, DB_FILE):
        self.df = df
        self.DB_FILE = DB_FILE
        self.dbtable = dbtable
        self.df_columns_list = list(self.df.columns)
        self.conn = sqlite3.connect(DB_FILE)
        self.db_columns = list(
            pd.read_sql_query(
                'SELECT * FROM '+self.dbtable+' LIMIT 1;',
                con=self.conn
            ).columns
        )
        self.conn.close()
        for column_item in self.df_columns_list:
            if column_item not in self.db_columns:
                self.conn = sqlite3.connect(DB_FILE)
                local_query = 'ALTER TABLE `'+self.dbtable+'` ADD `'+column_item+'` TEXT NULL;'
                self.conn.execute(local_query)
                self.conn.close()
                print(local_query)

def main():
    gh_url = "https://github.com/disclose/diodb/raw/master/program-list.json"
    df_gh = pd.read_json(gh_url)
    df_gh.fillna('', inplace=True)
    df_gh.set_index('program_name', drop=False, inplace=True)
    df_gh_sorted = df_gh.iloc[df_gh.program_name.str.lower().argsort()]
    # df_gh.sort_index(inplace=True)
    f = open('program-list.json', 'w')
    try: create_empty_table(DB_FILE)
    except sqlite3.OperationalError: print('Table exists, pass.')
    ExtendTable('diodb', df_gh_sorted, DB_FILE)
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    try: df_gh_sorted.to_sql('diodb', conn, if_exists='append', index=False)
    except: print('Error: '+df_gh_sorted)
    conn.close()
    f.write(json.dumps(df_gh_sorted.to_dict(orient='records')))
    f.close

if __name__ == "__main__":
    main()