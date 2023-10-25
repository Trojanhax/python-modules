import rsa

# Load the recipient's public key
with open("public1.pem", "rb") as f:
    public_key = rsa.PublicKey.load_pkcs1(f.read())

# Load your private key (keep this key secure)
with open("private1.pem", "rb") as f:
    private_key = rsa.PrivateKey.load_pkcs1(f.read())

# Read the plaintext file you want to encrypt
with open("plaintext.txt", "rb") as f:
    plaintext = f.read()

# Encrypt the plaintext using the recipient's public key
ciphertext = rsa.encrypt(plaintext, public_key)

# Overwrite the plaintext file with the encrypted data
with open("plaintext.txt", "wb") as f:
    f.write(ciphertext)
