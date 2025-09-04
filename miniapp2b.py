import rsa

publicKey, privateKey = rsa.newkeys(512)

message = input("Please input a phrase to encrypt.")

print("original string: ", message)

encMessage = rsa.encrypt(message.encode(), 
                         publicKey)

print("encrypted string: ", encMessage)

decMessage = rsa.decrypt(encMessage, privateKey).decode()

print("decrypted string: ", decMessage)