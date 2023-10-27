# a script for exporting the structure of env variables
import os
import fnmatch

file_pattern = ".env"
search_directory = os.getcwd()


def find_file(file_pattern, search_dir):
    matches = []
    for root, _, files in os.walk(search_dir):
        for filename in fnmatch.filter(files, file_pattern):
            matches.append(os.path.join(root, filename))
    return matches

def get_env_variables_without_values(file_path):
    env_without_values = []
    with open(file_path, 'r') as env_file:
        for line in env_file:
            variable_name = line.split('=')[0].strip()
            if(variable_name.strip() and not variable_name.startswith('#')):
                variable_name += '='
            env_without_values.append(variable_name.strip())
    
    return env_without_values

found_files = find_file(file_pattern, search_directory)

if found_files:
    for file in found_files:
        output_file_path=os.path.dirname(file)+'/.env.example'
        variables = get_env_variables_without_values(file)
        try:
            with open(output_file_path, 'w') as output_file:
                for variable in variables:
                    output_file.write(variable + '\n')
                
            print(f"File '{file}' has been successfully read and written to '{output_file_path}'.")
        except IOError:
            print(f"Error reading or writing files.")
        
else:
    print(f"No files matching '{file_pattern}' found in '{search_directory}' or its subdirectories.")


