cd "C:\Users\Test 1\Desktop\coursework"

# === Set log file location ===
$logFile = "C:\Users\Test 1\Desktop\startup.log"

# === Function to log messages with timestamp ===
function Log-Message {
    param ([string]$message)
    $timestamp = Get-Date -Format "[yyyy-MM-dd HH:mm:ss]"
    "$timestamp $message" | Out-File -FilePath $logFile -Append
}

# === Log start ===
Log-Message "Script started"

# === Python setup ===
$pythonPath = "C:\Users\Test 1\AppData\Local\Programs\Python\Python313\python.exe"
$scripts = @(
    "File_Collection.py",
    "AES_Key_Generation.py",
    "RSA_Key_Generation.py",
    "AES_Encryption.py",
    "RSA_Encryption.py",
    "SMTP.py",
    "RSA_Decryption.py",
    "AES_Decryption.py"
)

# === Run Python scripts and capture output ===
foreach ($script in $scripts) {
    $scriptPath = "C:\Users\Test 1\Desktop\coursework\$script"
    & $pythonPath $scriptPath 2>&1 | Out-File -FilePath $logFile -Append
}

# === Hash files ===
$filesToHash = @(
    "Test.txt",
    "Test.txt.txt",
    "Test.docx",
    "Test.docx.docx",
    "OIP.jpg",
    "OIP.jpg.jpg"
)

foreach ($file in $filesToHash) {
    $filePath = "C:\Users\Test 1\Desktop\coursework\$file"
    Get-FileHash -Path $filePath | Out-File -FilePath $logFile -Append
}

# === Log end ===
Log-Message "Script finished"