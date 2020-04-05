#!/bin/bash

if [ $# -eq 0 ]
  then
    echo "Please provide a json filename as argument"
    echo "e.g. ./test_order program-list.json"
    exit
fi

# generates a temp json file ordered
python3 aux_test_order.py -j $1 -oj .temp_program-list.json
# if original file and temp file are different
    # (for those unfamiliar with bash, the ">" is redirecting the output of "diff"
    # to a null file, and NOT comparing if the output of "diff" is greater then "/dev/null")
if diff $1 .temp_program-list.json > /dev/null; then
    echo "File is sorted, everything is fine"
    rm .temp_program-list.json
else
    echo "Uh-oh, some things are out of order"
    mv .temp_program-list.json program-list_fixed.json
    echo "Fixed file created"
fi
