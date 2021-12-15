import csv
from code_compiler import execute_code
from evaluator import evaluator

with open('student_number_sheet.csv','r') as file:

    csvreader = csv.reader(file)

    for line in csvreader:
        print(line[0])
        path = "codes/"+line[0]+".cpp"
        execute_code(path)
        if evaluator('test_cases/test_case.txt', 'test.txt'):
            with open('grades.csv','w') as grade_file:
                csvwriter = csv.writer(grade_file)
                csvwriter.writerow([line[0], '100'])
            


