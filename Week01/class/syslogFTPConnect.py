import syslogCheck
import importlib 
importlib.reload(syslogCheck)
# SSH authentication failures 

def ftp_connection(filename, searchTerms):

    # Call syslockCheck and return results
    is_found = syslogCheck._syslog(filename,searchTerms)

    # found list 
    found = []

    # Loop through the results 
    for eachFound in is_found:

        #split the results 
        sp_results = eachFound.split(" ")

        # Append the split value to the found list 
        found.append(sp_results[3])

    #print(set(found))
    for eachHost in set(found): 
        print(eachHost)
