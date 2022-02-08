# Import csv and RE libraries 
import csv
import re 

# Variable Declaration 
contents = 0 

# Function Defenition 
def urlHausOpen(filename,searchTerms):

# Changing While open to With Open and removing 'filename' to the variable instead of a hard-coded string
    with open(filename) as f:

        # removing extra = to set instead of compare and changing review to reader on the f variable and setting the delimiter to ','
        contents = csv.reader(f,delimiter=',')

    # Extracting each field through the first line 
        for _ in range(9):
            next(contents)
    
        # Removed Extra For Loop 
        for eachLine in contents:
            x = re.findall(r""+searchTerms+"",eachLine[2])
            for _ in x:
# Don't edit this line. It is here to show how it is possible
# to remove the "tt" so programs don't convert the malicious
# domains to links that an be accidentally clicked on.
                the_url = eachLine[2].replace("http","hxxp")
                the_src = eachLine[4]

                # Changing the + to a * to multiply string instead of concatenate 
                print("""
                URL:{}
                Info: {}
                {}""".format(the_url, the_src,"*"*60))
