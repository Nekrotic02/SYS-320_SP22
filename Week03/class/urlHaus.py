# Import csv and RE libraries 
import re
import csv
#

# Changing the function name to resemble that on the console 
def ur1HausOpen(filename,searchTerms):
    # Open the file passed in as a function parameter 

    # Variable Declaration 
    rows = []
    #found = []
    contents = 0

    # Reading the file 
    with open(filename) as f:

        # Creating CSV reader object 

        contents = csv.reader(f, delimiter=',')

    # extracting field names through first row 
        for _ in range(9):
           fields = next(contents)

    # search for keywords 
        for keyword in searchTerms:
            for eachLine in contents:
        #for eachLine in contents:

                x = re.findall(r""+searchTerms+"",eachLine[2])
    for _ in x:
# Don't edit this line. It is here to show how it is possible
# to remove the "tt" so programs don't convert the malicious
# domains to links that an be accidentally clicked on.
        the_url = eachLine[2].replace("http","hxxp")
        the_src = eachLine[4]

        # Converting the int to a string for concatination
        print("""
        URL:{}
        Info: {}
        {}""".format(the_url, the_src,"*"+str(60)))
        
