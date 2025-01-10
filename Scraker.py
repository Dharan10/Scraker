import subprocess
import os
import datetime

# Banner
banner = """
                                                                      
 @@@@@@    @@@@@@@  @@@@@@@    @@@@@@   @@@  @@@  @@@@@@@@  @@@@@@@   
@@@@@@@   @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@  @@@  @@@@@@@@  @@@@@@@@  
!@@       !@@       @@!  @@@  @@!  @@@  @@!  !@@  @@!       @@!  @@@  
!@!       !@!       !@!  @!@  !@!  @!@  !@!  @!!  !@!       !@!  @!@  
!!@@!!    !@!       @!@!!@!   @!@!@!@!  @!@@!@!   @!!!:!    @!@!!@!   
 !!@!!!   !!!       !!@!@!    !!!@!!!!  !!@!!!    !!!!!:    !!@!@!    
     !:!  :!!       !!: :!!   !!:  !!!  !!: :!!   !!:       !!: :!!   
    !:!   :!:       :!:  !:!  :!:  !:!  :!:  !:!  :!:       :!:  !:!  
:::: ::    ::: :::  ::   :::  ::   :::   ::  :::   :: ::::  ::   :::  
:: : :     :: :: :   :   : :   :   : :   :   :::  : :: ::    :   : :  

                       A scripted cracker
                       @hashcat @hashid
"""

# Input and validation
def get_user_input():
    hash_value = input("Enter the hash: ").strip()
    if not hash_value or " " in hash_value:
        raise ValueError("[!] Invalid hash input.")
    return hash_value

# Save hash to file
def save_to_file(filename, data):
    with open(filename, "w") as file:
        file.write(data + "\n")
    print(f"[*] Hash saved to {filename}")

# Log results
def log_results(log_file, hash_value, cracked_value):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] Hash: {hash_value} | Cracked: {cracked_value}\n"
    with open(log_file, "a") as file:
        file.write(log_entry)
    print(f"[*] Results logged in {log_file}")

# Hash identification
def identify_all_possible_hash_modes(hash_value):
    try:
        result = subprocess.run(["hashid", hash_value], capture_output=True, text=True, check=True)
        lines = result.stdout.strip().split("\n")
        hash_modes = []
        for line in lines:
            if "[Hashcat Mode:" in line:
                name = line.split("[")[0].strip()  # This gets the name of the hash type
                mode = line.split("[Hashcat Mode: ")[-1].strip("]")  # This extracts the mode
                hash_modes.append((name, mode))
                
        if not hash_modes:
            print("[!] Hash modes not found using hashid. Falling back to length-based identification.")
            return fallback_identify_hash_modes(hash_value)

        return hash_modes
    except Exception as e:
        print(f"[!] Error running hashid: {e}")
        return fallback_identify_hash_modes(hash_value)

# Fallback identification with NTLM rule
def fallback_identify_hash_modes(hash_value):
    if len(hash_value) == 32 and hash_value.isalnum() and any(c.isupper() for c in hash_value) and any(c.isdigit() for c in hash_value):
        return [("NTLM", "1000")]
    hash_length = len(hash_value)
    length_map = {
        32: [("MD5", "0")],
        40: [("SHA-1", "100")],
        64: [("SHA-256", "1400")],
        128: [("SHA-512", "1700")]
    }
    return length_map.get(hash_length, [])

# Attempt cracking
def attempt_cracking(hash_file, mode):
    try:
        wordlist = "/usr/share/wordlists/rockyou.txt"
        if not os.path.exists(wordlist):
            raise FileNotFoundError("[!] Wordlist not found. Ensure rockyou.txt is present.")
        result = subprocess.run(
            ["hashcat", "-m", mode, hash_file, wordlist, "--quiet", "--potfile-disable"],
            capture_output=True, text=True, check=True
        )
        if result.stdout.strip():
            cracked_value = result.stdout.split("\n")[0].split(":")[-1].strip()
            return cracked_value
        return None
    except subprocess.CalledProcessError as e:
        print(f"[!] Hashcat error for mode {mode}: {e.stderr}")
        return None

# Main workflow
def main():
    try:
        print(banner)
        hash_value = get_user_input()
        save_to_file("hashes.txt", hash_value)

        hash_modes = identify_all_possible_hash_modes(hash_value)
        
        if not hash_modes:
            print("[!] Unable to identify hash modes. Please check the hash.")
            return

        print("[*] Identified possible hashes:")
        for name, mode in hash_modes:
            print(f"    - {name} (Mode: {mode})")  # This line will now correctly print both name and mode

        for idx, (name, mode) in enumerate(hash_modes, 1):
            print(f"[*] Attempting to crack {name} [Mode: {mode}] ({idx}/{len(hash_modes)})")
            cracked_value = attempt_cracking("hashes.txt", mode)
            if cracked_value:
                print(f"[*] Successfully cracked: {cracked_value}")
                log_results("hash_cracking_log.txt", hash_value, cracked_value)
                return

        print("[!] Unable to crack the hash. Try alternative methods.")
    except Exception as e:
        print(f"[!] An unexpected error occurred: {e}")

# Run the script
if __name__ == "__main__":
    main()
