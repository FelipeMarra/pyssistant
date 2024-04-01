#https://stackoverflow.com/questions/47986858/give-inputs-to-a-running-program-using-python
import sys

# A dict w/
# key: input string to the target program
# value: list of strings of valeus that must be int the 
# program's output
expected = dict[str:list[str]]

expected = {
    "This is a test": ["input", "test"]
}

for key, values in expected.keys():
    sys.stdout(key)

    for v in values:
        data = sys.stdin.read()
        print(data)
