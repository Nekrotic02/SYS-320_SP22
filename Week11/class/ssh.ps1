cls
# Login to a remote SSH server 

New-SSHSession -ComputerName "192.168.4.22" -Credential (Get-Credential sys320)

# Add a prompt to run commands 

while ($true) 
{
    $the_cmd = Read-Host -Prompt "Please enter a command"

    # Run command on remote SSH Server 
    (Invoke-SSHCommand -index 0 $the_cmd).Output 
}


Set-SCPItem -ComputerName "192.168.4.22" - -Credential (Get-Credential sys320) -Path "/home/sys320" -Destination "./ssh.ps1"

