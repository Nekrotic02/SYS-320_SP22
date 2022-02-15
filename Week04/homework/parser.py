import os, argparse, searchLogs, re, sys, yaml

parser = argparse.ArgumentParser(

    description="Parses through multiple log files in a given directory and matches it to threats detailed in a yaml file",
    epilog="Developed by Ciaran Byrne, 14/02/2022 (DD/MM/YYYY)"
)
# Parameter Passing
parser.add_argument("-d","--directory", required=True,help="Directory conatianing log files.")
parser.add_argument("-s","--service",required=True,help="Search Service to parse files for")
parser.add_argument("-t","--term",required=True,help="Term to search for as defined in yaml file")
parser.add_argument("-y","--yaml",required=True,help="Yaml file for config")
args = parser.parse_args()

rootdir = args.directory
search_service = args.service
search_term = args.term
yaml_file = args.yaml

# Error Handling with Directory argument

if not os.path.isdir(rootdir):
    print("Invalid Directory => {}".format(rootdir))
    exit()

# Crawl to get list of files 
fList = []

for root, subfolders, filenames in os.walk(rootdir):
    
    for f in filenames:

        fileList = root + "/" + f
        fList.append(fileList)


# Function Defenitions 
def search_bytes(filename, service, terms, yaml_file):

    is_found = logs(filename, service, terms, yaml_file)

    found = []

    for eachFound in is_found:

        #split the results 
        sp_results = eachFound.split(" ")

        # Append the split value to the found list 
        found.append(sp_results[0] + " " + sp_results[2] + " " + sp_results[4] + " " + sp_results[5] + " " + sp_results[6])

    found = set(found)
    return found
def search_proxy(filename, service, terms, yaml_file):

    # Call syslockCheck and return results
    is_found = logs(filename, service, terms, yaml_file)

    # found list 
    found = []

    # Loop through the results 
    for eachFound in is_found:

        #split the results 
        sp_results = eachFound.split(" ")

        # Append the split value to the found list 
        found.append(sp_results[0] + " " + sp_results[2] + " " + sp_results[3] + " " + sp_results[4] + " " + sp_results[5] + " " + sp_results[6])

    return found

def logsearch(filename,service,terms, yaml_file):
    

    # Call syslockCheck and return result 
    is_found = logs(filename, service, terms, yaml_file)

    found = []

    for eachFound in is_found:

        found.append(eachFound)
    return found

def logs(filename, service, terms, yaml_file):

    with open(yaml_file) as yf:
        keywords = yaml.safe_load(yf)

    terms = keywords[service][terms]

    lisOfKeywords = terms.split(',')

    with open(filename) as f: 
        
        contents = f.readlines()
    results = []

    for line in contents:

        for eachKeyword in lisOfKeywords:

            #Escaped characters using the re.escape function instead of \ 
            x = re.findall(r''+eachKeyword+'', line)

        for found in x: 

            results.append(found)

    #if len(results) == 0:
    #    print('No Results')
    #    sys.exit(1)

    results = sorted(results)

    return results
#parse through each file in the list looking for pattern 

for eachFile in fList:
    results = []
    # Checking for specific needs and logs
    if search_service == "web":
        found = search_bytes(eachFile, search_service,search_term, yaml_file)
        for eachFound in found:
            results.append(eachFound)
    if search_service == "proxy":
        found = search_proxy(eachFile, search_service,search_term, yaml_file)
        for eachFound in found:
            results.append(eachFound)
    else: 
        # Generic full line printed if no special modules are made 
        found = logsearch(eachFile,search_service,search_term, yaml_file)
        for eachFound in found:
            results.append(eachFound)

    # Print the file and the contents otherwise specify that there are no contents

    print("""File:{}""".format(eachFile))
    if len(results) == 0:
        print("No Results")
    else:
        for eachValue in results:
            print(eachValue)
    print("*"*60)