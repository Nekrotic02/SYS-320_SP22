import os, argparse, searchLogs

parser = argparse.ArgumentParser(

    description="Parses through multiple log files in a given directory and matches it to threats detailed in a yaml file",
    epilog="Developed by Ciaran Byrne, 14/02/2022 (DD/MM/YYYY)"
)
# Parameter Passing
parser.add_argument("-d","--directory", required=True,help="Directory conatianing log files.")
parser.add_argument("-s","--service",required=True,help="Search Service to parse files for")
parser.add_argument("-t","--term",required=True, help="Term to search for as defined in yaml file")

args = parser.parse_args()

rootdir = args.directory
search_service = args.service
search_term = args.term

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

#parse through each file in the list looking for pattern 

for eachFile in fList:
    results = []
    # Checking for specific needs and logs
    if search_service == "web":
        found = searchLogs.search_bytes(eachFile, search_service,search_term)
        for eachFound in found:
            results.append(eachFound)
    if search_service == "proxy":
        found = searchLogs.search_proxy(eachFile, search_service,search_term)
        for eachFound in found:
            results.append(eachFound)
    else: 
        # Generic full line printed if no special modules are made 
        found = searchLogs.logsearch(eachFile,search_service,search_term)
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
