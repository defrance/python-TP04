from cryptography.fernet import Fernet

key = Fernet.generate_key()
print ("Clée : "+ key.decode('UTF-8'))
f = Fernet(key)
message_saisie = input("message à crypter : ")
message_crypte = f.encrypt(bytes(message_saisie, 'utf-8'))
print ("message crypté : " + message_crypte.decode('UTF-8'))

message_decrypt = f.decrypt(message_crypte)
print ("message décrypté : " + message_decrypt.decode('UTF-8'))
