from cryptography.fernet import Fernet
import os

# Generate a key for encryption
key = Fernet.generate_key()
f = Fernet(key)

# Directory containing the text files you want to encrypt
directory_path = r"C:\Users\DELL\Desktop\python project"

# Iterate through all files in the directory
for filename in os.listdir(directory_path):
    if filename.endswith(".txt"):
        file_path = os.path.join(directory_path, filename)
        
        # Open the file in binary read mode
        with open(file_path, "rb") as file:
            file_data = file.read()
            encrypted_data = f.encrypt(file_data)
        
        # Write the encrypted data back to the same file
        with open(file_path, "wb") as file:
            file.write(encrypted_data)

print("Encryption completed for all .txt files in the directory.")
