from cryptography.fernet import Fernet

# Generate a random Fernet key
key = Fernet.generate_key()
print(key)
# Create a Fernet cipher object with the key
f = Fernet(key)
print(f)
# Encrypt a message
message = b"Hello, World!"
encrypted_message = f.encrypt(message)
print(message)
# Decrypt the message
dencr = f.decrypt(encrypted_message)
print(dencr)
