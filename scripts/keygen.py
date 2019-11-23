import subprocess
import binascii
import DataSync as ds

config = ds.load_config()

key: bytes = str.encode(config['key'])
iv: bytes = str.encode(config['iv'])

assert len(key) == 32
assert len(iv) == 16

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
