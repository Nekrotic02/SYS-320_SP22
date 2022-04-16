# Create a commandline parameter to copy a file and place into an evidence directory

param(
    [parameter(Mandatory = $true)] 
    [int]$reportNo,

    [parameter(Mandatory = $true)]
    [String]$filePath 
) 

# Create a direcotry with the report number 
$reportDir = "rpt$reportNo"

# Create new directory 
mkdir $reportDir

# Copy file into new directory
Copy-Item $filePath $reportDir

