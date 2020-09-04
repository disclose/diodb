import sys
import json
from jsonschema.exceptions import ValidationError
from jsonschema import validate


def validateJson(json_data, schema):
    try:
        validate(instance=json_data, schema=schema)
    except ValidationError as err:
        print(err)
        return False
    return True


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
