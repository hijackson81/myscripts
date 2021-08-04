Add-PSSnapin VeeamPSSnapin

#Export Encrypted Disk
Get-VBRImportedEncryptedBackup -Name "Job*" | Select Name | Export-CSV "C:\scripts\encrypted_jobs.csv" -NoTypeInformation -Encoding UTF8

# Import Encrypted Disk Name
Import-Csv "C:\scripts\encrypted_jobs.csv" | ForEach-Object {

$jobname = $_."Name"
$encryptedbackup = Get-VBRImportedEncryptedBackup -Name $jobname
Write-Output "Decrypting - $jobname"
Set-VBREncryptedBackupPassword -Backup $encryptedbackup -Password "YourEncryptPassword"
Write-Output "Decrypted Successfully- $jobname"
}

