import syslogCheck
import importlib 
importlib.reload(syslogCheck)
# SSH authentication failures 

def userCheck(filename, searchTerms):

    # Call syslockCheck and return results
    is_found = syslogCheck._syslog(filename,searchTerms)

    # found list 
    found = []

    # Loop through the results 
    for eachFound in is_found:
        #print("eachFound Variable before split: ", eachFound)
        #print()
        #split the results 
        sp_results = eachFound.split(" ")
        #print("eachFound Variable after split: ", eachFound)
        #print()
        # Append the split value to the found list 
        found.append(sp_results[5])

    #print(set(found))
    for eachValue in set(found): 
        print(eachValue)