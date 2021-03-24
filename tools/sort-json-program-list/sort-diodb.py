#!/usr/bin/python
# Authors:      prodigysml <https://github.com/prodigysml>
#               Sick.Codes <https://github.com/sickcodes>
#               0ddInput   <https://github.com/0ddInput>
# License:      MIT
# Copyright:    CC 2021 Disclose.io

import json

def main():
    master_list = json.loads(open("../../program-list.json").read())

    master_list = sorted(master_list, key=lambda k: k["program_name"])

    print(json.dumps(master_list, indent=4))

if __name__ == "__main__":
    main()
