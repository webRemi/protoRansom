import os
import sys
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

print("Welcome to ghostUtility...")

path = sys.argv[1]

if len(sys.argv) < 2:
  print(f"{sys.argv[0]} <file>")
  sys.exit()

print(f"Starting decrypting {sys.argv[1]}")

hex_key = "61626b656c646c7768736b646c663b64"
key = bytes.fromhex(hex_key)

for root, dirs, files in os.walk(path):
  for file in files:
    file = os.path.join(root, file)
    data = open(file, "rb").read()

    ciphertext = open(file, "rb").read()
    cipher = AES.new(key, AES.MODE_CBC)

    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)

    open(file, "wb").write(plaintext[16:])

print("All the files have been decrypted")

