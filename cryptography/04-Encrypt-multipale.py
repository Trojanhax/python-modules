from cryptography.fernet import Fernet
import os

# Generate a key for encryption
key = Fernet.generate_key()
print(key)
f = Fernet(key)

# Directory containing the text files you want to encrypt
directory_path = r"C:\Users\DELL\Desktop\python project"

# List of file extensions you want to encrypt
valid_extensions = [".txt", ".md"]

# Iterate through all files in the directory
for filename in os.listdir(directory_path):
    if any(filename.endswith(ext) for ext in valid_extensions):
        file_path = os.path.join(directory_path, filename)

        # Open the file in binary read mode
        with open(file_path, "rb") as file:
            file_data = file.read()
            encrypted_data = f.encrypt(file_data)

        # Write the encrypted data back to the same file
        with open(file_path, "wb") as file:
            file.write(encrypted_data)

print("Encryption completed for all specified file extensions in the directory.")
