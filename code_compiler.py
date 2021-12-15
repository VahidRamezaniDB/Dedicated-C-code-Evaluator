
import os

def execute_code(path: str):
    command = "g++ -o out " + path
    os.system(command)
    os.system("out.exe")
