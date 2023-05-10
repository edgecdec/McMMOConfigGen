import json
import os


def convert_string_to_json(string):
    lines = string.strip().split('\n')
    print(len(lines))
    result = {}
    current_level = result

    for line in lines:
        line = line.strip()
        if not line:
            continue

        indent_count = line.index(line.lstrip())
        key_value = line.strip().split(':')
        key = key_value[0].strip()
        value = key_value[1].strip()

        if indent_count == 0:
            current_level[key] = value
        else:
            nested_keys = key.split(':')
            current_level = result
            for nested_key in nested_keys:
                if nested_key not in current_level:
                    current_level[nested_key] = {}
                current_level = current_level[nested_key]
            current_level = value

    return json.dumps(result, indent=4)


def read_file_as_string(file_name):
    with open(file_name, 'r') as file:
        content = file.read()
    return content


def write_obj_to_file(obj, file_name):
    with open(file_name, 'w') as file:
        file.write(obj)


def get_file_contents(file_path):
    with open(file_path, 'r') as file:
        contents = file.read()
        return contents

def add_indentation(string, indentation):
    lines = string.split('\n')
    indented_lines = [(indentation + line) for line in lines]
    indented_string = '\n'.join(indented_lines)
    return indented_string

def create_yaml_str_from_dir(directory):
    yaml_str = ""
    files = os.listdir(directory)
    files = sorted(files)
    for filename in files:
        path = os.path.join(directory, filename)
        if os.path.isdir(path):
            yaml_str += f"\n{filename}:"
            yaml_str_addition = create_yaml_str_from_dir(path)  # Recursive call for subdirectories
            yaml_str += add_indentation(yaml_str_addition, "    ")
            # yaml_str += "\n"
        else:
            yaml_str += f'\n{get_file_contents(f"{directory}/{filename}")}'
            # print(yaml_str)
    return f"{yaml_str}"
