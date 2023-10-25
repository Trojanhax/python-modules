import rsa

# Generate an RSA key pair with a specified key size (e.g., 2048 bits)
(public_key, private_key) = rsa.newkeys(2048)

# Save the public key to a file
with open("public1.pem", "wb") as f:
    f.write(public_key.save_pkcs1('PEM'))

# Save the private key to a file
with open("private1.pem", "wb") as f:
    f.write(private_key.save_pkcs1('PEM'))

print("Public Key (PEM format) has been saved to 'public.pem'")
print("Private Key (PEM format) has been saved to 'private.pem'")
