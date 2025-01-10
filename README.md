# HashCracker

**HashCracker** is a Python-based command-line tool designed to identify and crack various hashes using `hashid` for identification and `hashcat` for cracking. It supports multiple hash types and uses the popular `rockyou.txt` wordlist for brute-forcing.

---

## Features

- **Hash Identification**: Automatically identifies possible hash types and their corresponding Hashcat modes using `hashid`.
- **Fallback Identification**: Provides hash type suggestions based on the hash length when `hashid` fails.
- **Cracking Support**: Attempts to crack hashes using `hashcat` with the `rockyou.txt` wordlist.
- **Logging**: Logs cracking attempts and results with timestamps for future reference.
- **User-Friendly**: Provides detailed outputs for each step, including identified hash types and cracking progress.

---

## Supported Hash Types

HashCracker can identify and attempt to crack the following types of hashes (and more):

- **MD5** (Mode: 0)
- **SHA-1** (Mode: 100)
- **SHA-256** (Mode: 1400)
- **SHA-512** (Mode: 1700)
- **NTLM** (Mode: 1000)

Additional hash types may be supported based on `hashid` results or fallback rules.

---

## Prerequisites

- **Python**: Make sure Python 3.x is installed on your system.
- **Hashcat**: Install Hashcat for cracking functionality. [Download Hashcat](https://hashcat.net/hashcat/)
- **Hashid**: Install Hashid for hash identification. You can install it via pip:
  ```bash
  pip install hashid
**Wordlist**: Ensure the rockyou.txt wordlist is available in /usr/share/wordlists/ or provide a custom path.
## Installation
**Clone the repository:**
```bash
git clone https://github.com/Dharan10/Scraker.git
cd Scraker
```
## Usage
**Run the script:**
```bash
python Scraker.py
```

## Limitations
**Wordlist-Dependent**: Cracking success depends on the quality and size of the wordlist.

**Identification Accuracy**: Hash identification relies on hashid and may not always provide exact matches.

**Single Hash at a Time**: Currently, the tool only processes one hash per execution.
# Log mechanism
The script has a inbuilt loging mechanism which has a log of series of cracked hash and its hash type
# Example
![image](https://github.com/user-attachments/assets/c4eb8fc6-fb44-4fb9-b6a1-f4affaa73984)
**Log:**
![image](https://github.com/user-attachments/assets/0692c71f-ff34-4e84-b684-ece478499371)

---

## Usage Policy

This tool is open for use with prior permission from the author. Please contact the author for any inquiries or to request usage rights.

**Contact:** dharanragunathan@gmail.com

**Linkedin:** [Dharan Ragunathan](https://www.linkedin.com/in/r-dharan-37b556272/)  
