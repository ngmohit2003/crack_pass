import hashlib

password = "qwerty"
hash = hashlib.md5(password.encode()).hexdigest()
print("Hash of password:", hash)
