import yaml, re, sys

with open('searchTerms.yaml') as yf:
    keywords = yaml.safe_load(yf)

def search_bytes(filename, service, terms):

    is_found = logs(filename, service, terms)

    found = []

    for eachFound in is_found:

        #split the results 
        sp_results = eachFound.split(" ")

        # Append the split value to the found list 
        found.append(sp_results[0] + " " + sp_results[2] + " " + sp_results[4] + " " + sp_results[5] + " " + sp_results[6])

    found = set(found)
    return found
def search_proxy(filename, service, terms):

    # Call syslockCheck and return results
    is_found = logs(filename, service, terms)

    # found list 
    found = []

    # Loop through the results 
    for eachFound in is_found:

        #split the results 
        sp_results = eachFound.split(" ")

        # Append the split value to the found list 
        found.append(sp_results[0] + " " + sp_results[2] + " " + sp_results[3] + " " + sp_results[4] + " " + sp_results[5] + " " + sp_results[6])

    return found

def logsearch(filename,service,terms):
    
    # Call syslockCheck and return result 
    is_found = logs(filename, service, terms)

    found = []

    for eachFound in is_found:

        found.append(eachFound)
    return found

def logs(filename, service, terms):

    terms = keywords[service][terms]

    lisOfKeywords = terms.split(',')

    with open(filename) as f: 
        
        contents = f.readlines()
    results = []

    for line in contents:

        for eachKeyword in lisOfKeywords:

            #Escaped characters using the re.escape function instead of \ 
            escaped = re.escape(eachKeyword)
            x = re.findall(r''+escaped+'', line)

        for found in x: 

            results.append(found)

    #if len(results) == 0:
    #    print('No Results')
    #    sys.exit(1)

    results = sorted(results)

    return results