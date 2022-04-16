# List the files in a directory 

# List all files and print the full path 
#Get-ChildItem -Recurse -Include *.docx,*.pdf,*.txt -Path .\Documents | Select FullName

Get-ChildItem -Recurse -Include *.docx,*.pdf,*.txt -Path .\Documents | export-csv -Path files.csv 

# Import CSV File. 

$filelist = import-csv -Path .\files.csv -Header FullName 



# Loop through the results 
foreach ($f in $filelist) {


    Get-ChildItem -Path $f.FullName
}
