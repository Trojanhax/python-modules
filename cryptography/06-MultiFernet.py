from cryptography.fernet import Fernet

# Generate three Fernet keys
key1 = Fernet.generate_key()
key2 = Fernet.generate_key()
key3 = Fernet.generate_key()

# Print the generated keys
print("Key1:", key1)
print("Key2:", key2)
print("Key3:", key3)

# Create Fernet ciphers using the keys
cipher1 = Fernet(key1)
cipher2 = Fernet(key2)
cipher3 = Fernet(key3)

# Message to be encrypted
message = b"hello grey"

# Encrypt the message using each cipher
encrypted_message1 = cipher1.encrypt(message)
encrypted_message2 = cipher2.encrypt(message)
encrypted_message3 = cipher3.encrypt(message)

# Combine the encrypted messages
combined_encrypted_message = encrypted_message1 + encrypted_message2 + encrypted_message3

print("Original Message:", message)
print("Combined Encrypted Message:", combined_encrypted_message)
