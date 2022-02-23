import re, yaml


def logs(filename, service, terms, yaml_file):

    with open(yaml_file) as yf:
        keywords = yaml.safe_load(yf)

    terms = keywords[service][terms]

    lisOfKeywords = terms.split(',')

    with open(filename, "r", encoding="UTF-8") as f: 
        
        contents = f.readlines()
    results = []

    for line in contents:

        for eachKeyword in lisOfKeywords:

            #Escaped characters using the re.escape function instead of \ 
            x = re.findall(r''+eachKeyword+'', line)

        for found in x: 
            sp_results = found.split(",")

            found = sp_results[1] + " | " + sp_results[2] + " | " + sp_results[3] + " | "  + sp_results[4] + " | " + sp_results[5] + " | " + sp_results[6]
            results.append(found)

    #if len(results) == 0:
    #    print('No Results')
    #    sys.exit(1)

    results = sorted(results)

    return results