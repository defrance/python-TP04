from ftplib import FTP
ftp = FTP('127.0.0.1' )  
#ftp.login()                     # connection anonyme par defaut
ftp.login("user", "12345")	# connection avec login et mot de passe
# list le contenu du répertoire
ftp.retrlines('LIST')           # list directory contents
# on récupère un fichier 
with open('README.md', 'wb') as fp:
	ftp.retrbinary('RETR README.md', fp.write)

# on envoie un fichier
with open('README.md', 'rb') as fp:
	ftp.storbinary('STOR toto.txt', fp)
 
ftp.quit()
