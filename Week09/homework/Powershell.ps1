# Get a list of running processes 

#Get-Process | Get-Member

# Get a list of process: name, id, path 

Get-Process | Select ProcessName, id, path | Export-Csv -Path "C:\Users\cpb20\Desktop\SYS320\process.csv"

# System Services 

$outputName = "C:\Users\cpb20\Desktop\SYS320\services.csv"
#Get-Service | get-member
Get-Service | select Status, Name, DisplayName, BinaryPathName | export-csv -Path $outputName



# Get a list of running services 

Get-Service | Where-Object { $__.Status -eq "running" } | Export-Csv -Path $outputName

# Check if file exists 

if ( Test-Path $outputName ) {
    Write-Host -BackgroundColor "Green" -ForegroundColor "White" "Services file was created"
} Else {
    Write-Host -BackgroundColor "Red" -ForegroundColor "White" "Services file was not created"
}

