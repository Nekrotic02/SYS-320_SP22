# List the files in a directory 

# List all files and print the full path 
#Get-ChildItem -Recurse -Include *.docx,*.pdf,*.txt -Path .\Documents | Select FullName

$dir = "D:\Champlain Work\Second Semester\SYS-320 Automation and Scripting\SYS-320_SP22\Week12\class\Documents"
$csv = "D:\Champlain Work\Second Semester\SYS-320 Automation and Scripting\SYS-320_SP22\Week12\files.csv"

Get-ChildItem -Recurse -Include *.pdf,*.xlsx,*.docx -Path $dir | export-csv -Path $csv

# Import CSV File. 

$filelist = import-csv -Path $csv -Header FullName 



# Loop through the results 
foreach ($f in $filelist) {


    Get- -Path $f.FullName
}
