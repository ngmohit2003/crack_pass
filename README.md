HEAD
# 🔐 Password Cracker (Educational Use Only)

## 📌 Description
A command-line Python tool that cracks MD5 password hashes using a dictionary attack.

## 🛠️ How It Works
- Reads a hash from the user
- Reads a wordlist (dictionary of passwords)
- Hashes each word and compares it
- Displays the password if a match is found

## 📂 Files
- `password_cracker.py` → main tool
- `passwords.txt` → dictionary wordlist
- `hash.txt` → target hash to crack
- `hash_gen.py` → generates sample hashes

## ⚠️ Disclaimer
For ethical use only — designed for learning, CTF, pentesting labs, or password audits.

## ✅ Sample Run
```bash
python3 password_cracker.py 0192023a7bbd73250516f069df18b500 passwords.txt
# crack_pass
 909c321b836f145f149ed6cd79cff2ba9e6e469d
