PROGRAM_LIST_JSON="$1"

jq --indent 3 -s '.[] | unique_by(.program_name)' < "$PROGRAM_LIST_JSON" > "_"

if ! cmp -s "$PROGRAM_LIST_JSON" "_"; then
  echo '::error title=Bad format::The "program-list.json" file is not formatted and sorted in accordance with the guidelines. Please use the command from https://github.com/disclose/diodb#how-to-contribute to format and sort the file.'
  exit 1
fi
