# Send an email using powershell 

# Message Body 


$toSend = @('ciaran.byrne@mymail.chammplain.edu','nekrotic.protonmail.com','ciaran@nekrotic.co.uk')

$msg = "Hello" 

while ($true) {

    foreach ($email in $toSend) {
        # Send the email 
    
        Write-Host "Send-MailMessage -From 'ciaran.byrne@mymail.champlain.edu' -To $email -Subject 'Spam Test' -Body $msg -SmtpServer X.X.X.X"
        
        # start-sleep 1
    }
}

