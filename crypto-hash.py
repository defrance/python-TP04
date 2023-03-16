import uuid
import hashlib
import getpass

def hash_password(password):
   # uuid is used to generate a random number of the specified password
   salt = uuid.uuid4().hex
   return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt

def check_password(hashed_password, user_password):
   password, salt = hashed_password.split(':')
   return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()

new_pass = input('Saisir un mot de passe: ')
hashed_password = hash_password(new_pass)
print('Mot de passe stocké : ' + hashed_password)
#old_pass = input('Saisir votre mot de passe à nouveau: ')
# pour cacher la saisie du mot de passe
old_pass = getpass.getpass('Password:')

if check_password(hashed_password, old_pass):
   print('Mot de passe Correct')
else:
   print('Mauvaise saisie')