# Create and interface to search through syslog files 
import re 
import sys


def _syslog(filename,listOfKeywords):    
    #Open a File (remember to use readlines not readline)
    with open(filename) as f:

        contents = f.readlines() 

    # List to store the results 
    results = []
    # Loop through the list returned. Each element isa line from the small file 
    for line in contents:

        for eachKeyword in listOfKeywords: 

            # if the "line" contains the keyword then it will print 
            #if eachKeyword in line: 

            # Searches returned results using a regular expression search
            x = re.findall(r''+eachKeyword+'', line)

            for found in x:
                # Append he returned keywords to the results list 
                results.append(found)  
            
    # Check to see if there are results 
    if len(results) == 0:
        print('No Results')
        sys.exit(1)

    # Sort the list 
    results = sorted(results)
    
    # Remove Duplicates 
    results = set(results)

    return results  
            #print(x)