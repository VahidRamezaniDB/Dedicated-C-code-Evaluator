# Dedicated-C-code-Evaluator
A dedicated application that evaluate the output of a C code with by comparing it with valid cases.
The program will execute every C code given and compare the output with a valid output already defined.
The C program to be evaluated must write it's output in an output file.

# Manual

* ### first step:
    clone the project and place your C/C++ codes inside "codes/" directory.
* ### then:
    Modify "test_cases/test_case.txt" file as you wish. It is the valid output that your code output will be compared to.

* ### at last:
    write yore student number, also yore C file name, in the first column of the "student_number_sheet.csv" file.
    **note** that your C file name format must be in the following format:

    **"student_number".c**

now just run the [run.bat](run.bat) file. You can see the result inside the grades.csv.