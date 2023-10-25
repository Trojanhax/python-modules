import rsa

# Generate an RSA key pair with a specified key size (e.g., 2048 bits)
(public_key, private_key) = rsa.newkeys(2048)

# Print the public and private keys
print("Public Key (PEM format):")
print(public_key.save_pkcs1().decode())

print("Private Key (PEM format):")
print(private_key.save_pkcs1().decode())
