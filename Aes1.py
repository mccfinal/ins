from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
from Cryptodome.Util.Padding import pad, unpad

def aes_encrypt(key, plaintext):
    cipher = AES.new(key, AES.MODE_CBC)
    padded_plaintext = pad(plaintext.encode('utf-8'), AES.block_size)
    return cipher.iv + cipher.encrypt(padded_plaintext)

def aes_decrypt(key, ciphertext):
    iv = ciphertext[:AES.block_size]
    ciphertext = ciphertext[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    decrypted_padded = cipher.decrypt(ciphertext)
    return unpad(decrypted_padded, AES.block_size).decode('utf-8')

# Generate a random key
key = get_random_bytes(16)

# Get plaintext input from the user
plaintext = input("Enter plaintext: ")

# Encrypt the plaintext
e = aes_encrypt(key, plaintext)

# Decrypt the ciphertext
d = aes_decrypt(key, e)

# Print encrypted and decrypted data
print("Encrypted:", e)
print("Decrypted:", d)
