import hashlib
import argparse

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Simple password hash cracker")
parser.add_argument("hash", help="Target hash to crack")
parser.add_argument("wordlist", help="Path to dictionary wordlist")

args = parser.parse_args()
target_hash = args.hash

try:
    # Open the wordlist
    with open(args.wordlist, "r", encoding="latin-1") as f:
        # Loop through each password
        for word in f:
            word = word.strip()  # remove newline
            hashed_word = hashlib.md5(word.encode()).hexdigest()
            if hashed_word == target_hash:
                print(f"[+] Password found: {word}")
                break
        else:
            print("[-] Password not found in wordlist")
except FileNotFoundError:
    print("Wordlist file not found.")
