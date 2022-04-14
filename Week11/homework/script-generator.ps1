$choice = Read-Host -Prompt "Please Enter 'windows' Or 'iptables' If you would like to create Windows Firewall rules or IPTables rules" 

$drop_urls = @('https://rules.emergingthreats.net/blockrules/emerging-botcc.rules','https://rules.emergingthreats.net/blockrules/compromised-ips.txt')

# Loop through the URLs for the rules list 
foreach ($u in $drop_urls) {
    
    # Extract the filename 
    $temp = $u.split("/")

    # The last element in the array plucked off is the filename 
    $file_name = $temp[-1]

    if (Test-Path $file_name)
    {
        continue
    }
    else 
    {
        # Download thhe rules list 
        Invoke-WebRequest -Uri $u -OutFile $file_name
    } 

} 

# Array containing the filename 
$input_paths = @('emerging-botcc.rules','compromised-ips.txt')


# Extract the IP addresses. 
# 255.255.255.255 
$regex_drop = '\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'

# Append the IP addresses to the temporary IP list. 
Select-String -Path $input_paths -Pattern $regex_drop | ForEach-Object {$_.Matches} | ForEach-Object {$_.Value} | Sort-Object | Get-Unique | Out-File -FilePath "bad-ips.txt"
 

$ip = Read-Host -Prompt "IP of Server: "
$user = Read-Host -Prompt "Username of admin on the server"

function iptables {
    (Get-Content -Path 'bad-ips.txt') | % {$_ -replace "^", "iptables -A INPUT -s " -replace "$", " -j DROP"} | Out-File -FilePath "iptables.bash"

   if (Test-Path ".\iptables.bash"){
       Write-Host "Script Created"
   } 
   else {
       Write-Host "Error: File Not Created"
       Exit
   }

   $copy = Read-Host -Prompt "Would you like to copy and execute this on the server? (y/n)"

   switch ($copy) {
       "y" { Set-SCPItem -ComputerName $ip -Credential (Get-Credential $user) -Path ".\iptables.bash" -Destination "/home/ciaran";
        $cmd = "bash /home/ciaran/iptables.sh";
       (Invoke-SSHCommand -index 0 $cmd).Output; 
       Break }

       "n" {Break}
   }
    
}

function windows {
    (Get-Content -Path ".\bad-ips.txt") | % {
        "New-NetFirewallRule -DisplayName 'Block $_ out' -Direction Outbound -Profile Any -Action Block -RemoteAddress $_"
        "New-NetFirewallRule -DisplayName 'Block $_ in' -Direction Inbound -Profile Any -Action Block -RemoteAddress $_" 
    } | Out-File -FilePath ".\Windows-Firewall.ps1"
    
    If (Test-Path ".\Windows-Firewall.ps1"){
        Write-Host "Script Created!"
    }
    else {
        Write-Host "Error: File Not Created"
        Exit
    }
}
switch ($choice) {

    "iptables" { iptables; Break}
    "windows" { windows; Break }
    
    default {throw "Please enter 'iptables' or 'windows' Caps Lock Matter"}
}