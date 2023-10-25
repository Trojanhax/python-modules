import rsa

# Load the public key from a file
with open("public1.pem", "rb") as f:
    public_key = rsa.PublicKey.load_pkcs1(f.read())

# Load the private key from a file
with open("private1.pem", "rb") as f:
    private_key = rsa.PrivateKey.load_pkcs1(f.read())

# Load the encrypted message from a file
with open('encrypt_message.txt', 'rb') as f:
    encrypted_message = f.read()

# Decrypt the message using the private key
decrypted_message = rsa.decrypt(encrypted_message, private_key)

# Save the decrypted message to a file
with open('decrypted_message.txt', 'wb') as f:
    f.write(decrypted_message)
