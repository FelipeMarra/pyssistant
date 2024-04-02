import os
import subprocess as sp
from tempfile import TemporaryFile

#TODO: test answers

# The path to the directory that contains the code you 
# want to run
DIR = "/home/dpi/Documents/materias/estagio_ensino/INF 100 - 8 /p3"

# Each line of the injection.txt file corresponds to a 
# user input
# To create different test cases just leave a blank line
# Each blank line delimitates the end of a test and the
# beginning of another
# There MUST exist a blank line at the end of the file

# The answer.txt file will be used to test the test cases 
# from injection.txt
# Each word for each line in answer.txt will correspond
# to words that must be returned by the test case

def read_injections() -> list[str]:
    treated = []

    injections = open("injection.txt").read()
    injections = injections.split("\n")

    temp = ""
    for injection in injections:
        if injection != "":
            temp = temp + injection + "\n"
        else:
            treated.append(temp)
            temp = ""

    return treated
            
def test_file(file_path:str):
    """
        Tests the program inside [file] for all the text
        cases from injection.txt and answer.txt 
    """
    # Read injection
    injections = read_injections()

    for injection in injections:
        # For each injection, create a temp file, and 
        # pass it as stdin for the file being tested
        with TemporaryFile(mode='w+t') as temp_f:
            temp_f.writelines(injection)
            temp_f.seek(0)

            print("\n ################")
            print("Testing: \n", temp_f.read())
            temp_f.seek(0)
            print("################ \n")

            # try:
            answer = sp.run(["python3", file_path], stdin=temp_f, capture_output=True, encoding="utf-8")
            temp_f.seek(0)

            if answer.stdout:
                print(answer.stdout)
            else:
                print("There was an error testing the file")
                print(answer)
            # except Exception as e:
            #     print(f"There was an error in file {file} \n {e} \n")
            

for file in os.listdir(DIR):
    print(f"\n Testing the file {file} \n")

    file_path = f'{os.path.join(DIR, file)}'

    test_file(file_path)

    # Open the current file in VS Code
    sp.run([f"code '{file_path}'"], shell=True, check=True)

    input("Press ENTRER to continue")