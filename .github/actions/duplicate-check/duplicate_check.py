import sys
import json


def duplicate_check_program_name(json_data):
	program_names = list()

	for program in json_data:
		if program["program_name"] in program_names:
			print("Duplicate program found. Name: " + program["program_name"])
			return True
		else:
			program_names.append(program["program_name"])

	return False


if __name__ == "__main__":
	full_path = sys.argv[1]

	json_data = json.loads(open(full_path + "program-list.json").read())

	if duplicate_check_program_name(json_data):
		print("Duplicate programs found with the same name")
		sys.exit(1)
