
from os import name, path

def get_valid_res(path):
    path_to_file = path
    file = open(path_to_file,mode='r')
    res = file.readlines()
    file.close()
    return res

def get_results(path):
    path_to_file = path
    file = open(path_to_file,mode='r')
    res = file.readlines()
    file.close()
    return res

def clean_output(output: list):
    trim_chars = [' ', '\n', '  ']
    if output[-1][-1] in trim_chars:
        output[-1] = output[-1][0:-1]
    return output

def check_results(code_output, valid_output):
    code_output = clean_output(code_output)
    if len(code_output) != len(valid_output):
        return False
    if len(list(set(code_output) & set(valid_output))) != len(valid_output):
        return False
    return True

def main():
    test_case_path = "test.txt"
    output_path = "test1.txt"
    test_case = get_valid_res(test_case_path)
    print(check_results(get_results(output_path), test_case))

if __name__ == "__main__":
    main()
