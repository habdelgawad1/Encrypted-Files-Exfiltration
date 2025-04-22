$taskName = "StartUpScript"
$scriptPath = "C:\Users\Test 1\Desktop\coursework\startup.ps1"

# Define the action: run PowerShell with your script
$action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-ExecutionPolicy Bypass -File `"$scriptPath`""

# Trigger: when user logs on
$trigger = New-ScheduledTaskTrigger -AtLogOn

# Run with highest privileges
$principal = New-ScheduledTaskPrincipal -UserId $env:USERNAME -LogonType Interactive -RunLevel Highest

# Optional: clean up existing task
if (Get-ScheduledTask -TaskName $taskName -ErrorAction SilentlyContinue) {
    Unregister-ScheduledTask -TaskName $taskName -Confirm:$false
}

# Register the task
Register-ScheduledTask -TaskName $taskName -Action $action -Trigger $trigger -Principal $principal