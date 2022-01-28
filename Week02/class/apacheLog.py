import logCheck
import importlib 
importlib.reload(logCheck)

# Apache Events 
def apache_events(filename, service, terms):

    # Call syslockCheck and return results
    is_found = logCheck._logs(filename, service, terms)

    # found list 
    found = []

    # Loop through the results 
    for eachFound in is_found:

        #split the results 
        sp_results = eachFound.split(" ")

        # Append the split value to the found list 
        found.append(sp_results[3] + " " + sp_results[0] + " " + sp_results[1])

    #print(set(found))
    for eachValue in set(found): 
        print(eachValue)
