#!/bin/bash

# https://stackoverflow.com/a/23930212
read -r -d '' entry << EOM
{
  "program_name": "",
  "policy_url": "",
  "contact_url": "",
  "contact_email": "",
  "offers_bounty": "no",
  "offers_swag": false,
  "pgp_key": "",
  "hall_of_fame": "",
  "hiring": "",
  "launch_date": "",
  "policy_url_status": "alive",
  "preferred_languages": "",
  "public_disclosure": "",
  "safe_harbor": "",
  "securitytxt_url": ""
}
EOM

jq --indent 3 --argjson entry "$entry" '[$entry] + .' program-list.json > _ && mv _ program-list.json
