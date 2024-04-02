#https://stackoverflow.com/questions/47986858/give-inputs-to-a-running-program-using-python
import sys
import subprocess as sp
from tempfile import TemporaryFile

#TODO: test answers

#TODO: change to a loop in a directory
# The path to the folder that contains the code you want
#  to run
PATH = "p03.py"

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
        answer = None

        # For each injection, create a temp file, and 
        # pass it as stdin for the file being tested
        with TemporaryFile(mode='w+t') as temp_f:
            temp_f.writelines(injection)
            temp_f.seek(0)

            print("\n ################")
            print("Testing: \n", temp_f.read())
            temp_f.seek(0)
            print("################ \n")

            answer = sp.run(["python3", file_path], stdin=temp_f, capture_output=True, encoding="utf-8")
            print(answer.stdout)

test_file(PATH)

# Open the current file in VS Code
sp.run([f"code {PATH}"], shell=True, check=True)
input("Press ENTRER to continue")