import grep

def ipcheck(filename, keyword):

    #Grep line with the username into memory 
    is_found = grep.grep(filename,keyword)

    #Split the results up into an array
    found = is_found.split()

    #Print results on the 8th array (IP address)
    print(found[8])