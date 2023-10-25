import rsa

# Save the public key to a file
with open("public1.pem", "rb") as f:
    public_key=f.read()
    

# Save the private key to a file
with open("private1.pem", "rb") as f:
    private_key=f.read()
