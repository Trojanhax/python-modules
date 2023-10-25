from cryptography.fernet import Fernet
import os

# Load the key used for encryption (keep it secure)
key = b'lUcFa9PAm8ZGBNKfYarL_SIS5G4rB9Je0qQI6FTb4zI='  # Replace with your actual encryption key
f = Fernet(key)

# Directory containing the text files you want to decrypt
directory_path = r"C:\Users\DELL\Desktop\python project"

# List of file extensions you want to decrypt
valid_extensions = [".txt", ".md"]

# Iterate through all files in the directory
for filename in os.listdir(directory_path):
    if any(filename.endswith(ext) for ext in valid_extensions):
        file_path = os.path.join(directory_path, filename)

        # Open the encrypted file in binary read mode
        with open(file_path, "rb") as file:
            encrypted_data = file.read()
            decrypted_data = f.decrypt(encrypted_data)

        # Write the decrypted data back to the same file
        with open(file_path, "wb") as file:
            file.write(decrypted_data)

print("Decryption completed for all specified file extensions in the directory.")
