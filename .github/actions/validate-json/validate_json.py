import sys
import json
from jsonschema.exceptions import ValidationError
from jsonschema import validate


def validateJson(json_data, schema):
    is_valid = False
    try:
        validate(instance=json_data, schema=schema)
        is_valid = True
    except ValidationError as err:
        print(err)
        return False

    for record in json_data:
        # hall_of_fame is optional; when present it must be a URI string, never a boolean.
        # Use .get() so a missing key is treated as "not provided" instead of crashing.
        if isinstance(record.get("hall_of_fame"), bool):
            print("hall_of_fame value is a boolean, but should be a string. Program: " + record["program_name"])
            is_valid = False

        # contact_email is optional and an empty string is the dataset's "not provided"
        # convention; only flag a value that is present, non-blank, and missing an "@".
        email = record.get("contact_email", "")
        if email and "@" not in email:
            print(f"An invalid email has been provided for {record['program_name']}")
            is_valid = False

    return is_valid


if __name__ == "__main__":
    full_path = sys.argv[1]

    schema = json.loads(open(full_path + "program-list-schema.json").read())

    json_data = json.loads(open(full_path + "program-list.json").read())

    if validateJson(json_data, schema):
        print("JSON list is valid!")
        sys.exit(0)
    else:
        print("Updates to the JSON list is required to pass validation. Do not merge till it meets our validation criteria")
        sys.exit(1)
