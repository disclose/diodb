#!/bin/bash

jq --indent 3 -s '.[] | unique_by(.program_name)' < program-list.json > _ && mv _ program-list.json
