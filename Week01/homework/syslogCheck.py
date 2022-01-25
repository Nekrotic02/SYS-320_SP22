import grep 
import sys 
import re
def _syslog(filename,listOfKeywords):

    results = []
    # Open the file to be read
    with open(filename) as file:
        
        # Check each line in the file 
        for eachLine in file: 

            x = re.findall(r''+listOfKeywords+'', eachLine)

            for found in x:
                # Append he returned keywords to the results list 
                results.append(found)  

    if len(results) == 0:
        print('No Results')
        sys.exit(1)
    
    results = sorted(results)
    
    results = set(results)

    return results