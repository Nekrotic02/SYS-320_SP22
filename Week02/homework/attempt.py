import yaml 
import re
import sys
try:
    with open('searchTerms.yaml') as yf:
        keywords = yaml.safe_load(yf)

except EnvironmentError as e:
    print(e.strerror)


def parse(filename,service,term):

    terms = keywords[service][term]

    listOfKeywords = terms.split(' ')

    with open(filename) as f:
        contents = f.readlines()

    results = []

    for line in contents: 

        for eachKeyword in listOfKeywords:

            x = re.findall(r''+eachKeyword+'',line)

            for found in x:
                results.append(found)

    if len(results) == 0:
        print("No Results")
        sys.exit(1)

    results = sorted(results)

    results = set(results) 

    return results
    