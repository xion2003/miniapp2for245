from cryptography.fernet import Fernet

message = input("Please input a phrase to encrypt.")

print("original string: ", message)

key = Fernet.generate_key()

fernet = Fernet(key)

encMessage = fernet.encrypt(message.encode())

print("encrypted string: ", encMessage)

decMessage = fernet.decrypt(encMessage).decode()

print("decrypted string: ", decMessage)