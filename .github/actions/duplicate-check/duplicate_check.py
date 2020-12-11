import sys
import json


def duplicate_check_boilerplate(json_data, param, context):
	values = list()
	ret_val = False

	for program in json_data:
		if program[param] in values:
			print("Duplicate " + context + " found. " + context + ": " + program[param])
			ret_val = True
		else:
			values.append(program[param])

	return ret_val


def duplicate_check_policy_url(json_data):
	return duplicate_check_boilerplate(json_data, "policy_url", "policy url")


def duplicate_check_contact_url(json_data):
	return duplicate_check_boilerplate(json_data, "contact_url", "contact url")


def duplicate_check_program_name(json_data):
	return duplicate_check_boilerplate(json_data, "program_name", "name")


if __name__ == "__main__":
	full_path = sys.argv[1]

	json_data = json.loads(open(full_path + "program-list.json").read())

	duplicate_check_policy_url(json_data)

	if duplicate_check_program_name(json_data):
		print("Duplicate programs found with the same name")
		sys.exit(1)


