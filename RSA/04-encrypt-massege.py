import rsa

# Save the public key to a file
with open("public1.pem", "rb") as f:
    public_key=rsa.PublicKey.load_pkcs1(f.read())
    

# Save the private key to a file
with open("private1.pem", "rb") as f:
    private_key=rsa.PrivateKey.load_pkcs1(f.read())

message = 'my words are allways true'

ecrypte_message= rsa.encrypt(message.encode(),public_key)
with open('ecrypte_message.txt','wb') as f:
    f.write(ecrypte_message)
# print(ecrypte_message)
    

