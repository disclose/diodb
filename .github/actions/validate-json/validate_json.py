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
        if isinstance(record["hall_of_fame"], bool):
            print("hall_of_fame value is a boolean, but should be a string. Program: " + record["program_name"])
            is_valid = False

        try:
            if "@" not in record["contact_email"]:
                print(f"An invalid email has been provided for {record['program_name']}")
                is_valid = False
        except KeyError:
            pass

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
