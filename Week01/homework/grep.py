import re 

def grep(filename, string):

    with open(filename) as file:
        for line in file: 
            if re.findall(string, line):
                return line
