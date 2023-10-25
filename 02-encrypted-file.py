from cryptography.fernet import Fernet

key = Fernet.generate_key()
print(key)
f = Fernet(key)

input_file_path = "*.txt"

#  Open the file in binary read mode
with open(input_file_path, "rb") as file:
    file_data = file.read()
    encrypted_data = f.encrypt(file_data)

# Write the encrypted data back to the same file
with open(input_file_path, "wb") as file:
    file.write(encrypted_data)
