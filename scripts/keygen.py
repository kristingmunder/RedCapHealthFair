import random
import string
import subprocess
import binascii


def random_string(len=32):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(len))


key_string: str = random_string(32)
iv_string: str = random_string(16)

key: bytes = str.encode(key_string)
iv: bytes = str.encode(iv_string)

hex_key: str = binascii.hexlify(key).decode("utf-8")
hex_iv: str = binascii.hexlify(iv).decode("utf-8")

key_set_cmd: str = f"travis env set encrypted_key {hex_key}"
iv_set_cmd: str = f"travis env set encrypted_iv {hex_iv}"
encrypt_cmd: str = f"travis encrypt-file ./config.json ./config.json.enc --key {hex_key} --iv {hex_iv} --force"

process = subprocess.run(key_set_cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
print(process.stdout.decode("utf-8"))

process = subprocess.run(iv_set_cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
print(process.stdout.decode("utf-8"))

process = subprocess.run(encrypt_cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
print(process.stdout.decode("utf-8"))
