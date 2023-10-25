import rsa

# Load your private key (keep this key secure)
with open("private1.pem", "rb") as f:
    private_key = rsa.PrivateKey.load_pkcs1(f.read())

# Load the ciphertext you want to decrypt
with open("plaintext.txt", "rb") as f:
    ciphertext = f.read()

# Decrypt the ciphertext using your private key
decrypted_data = rsa.decrypt(ciphertext, private_key)

# Write the decrypted data to a new file or display it
with open("decrypted.txt", "wb") as f:
    f.write(decrypted_data)
