# Step1.ps1 

Copy-Item -Path "C:\Windows\system32\WindowsPowerShell\v1.0\powershell.exe" -Destination "C:\Users\cpb20"

$random = Get-Random -Minimum 1000 -Maximum 9876

Rename-Item -Path "C:\Users\cpb20\powershell.exe" -NewName "EnNoB-$random.exe"

$result = Test-Path -Path "C:\Users\cpb20\EnNoB-$random.exe" -PathType Leaf

if ($result = "True")
{
    Write-Host "Is Found"
}
else
{
    Write-Host "Error" 
}

"If you want your files restored, please contact me at ciaran.byrne@mymail.champlain.edu. I look forward to doing business with you." | Out-File -FilePath "C:\Users\cpb20\Desktop\Readme.READ"

$result = Test-Path -Path "C:\Users\cpb20\Desktop\Readme.READ" -PathType Leaf

if ($result = "True")
{
    Write-Host "Is Found"
}
else
{
    Write-Host "Error" 
}