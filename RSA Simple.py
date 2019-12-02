import rsa
(pubkey, privkey) = rsa.newkeys(512)
 
message = b'KSTU'

print("Intial message:", message)
crypto = rsa.encrypt(message, pubkey)
print("Encrypted: ", crypto)
message = rsa.decrypt(crypto, privkey)
print("Decrypted: ", message)

print(pubkey)
print(privkey)