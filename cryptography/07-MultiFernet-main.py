from cryptography.fernet import Fernet, MultiFernet

# Generate multiple Fernet keys
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

# Create a MultiFernet object with the list of keys
multi_cipher = MultiFernet([key1, key2, key3])

# Encrypt the message using the MultiFernet object
encrypted_message = multi_cipher.encrypt(message)

# Decrypt the message using the MultiFernet object
decrypted_message = multi_cipher.decrypt(encrypted_message)

print("Original Message:", message)
print("Encrypted Message 1:", encrypted_message1)
print("Encrypted Message 2:", encrypted_message2)
print("Encrypted Message 3:", encrypted_message3)
print("Combined Encrypted Message:", encrypted_message)
print("Decrypted Message:", decrypted_message)
