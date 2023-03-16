# Import smtplib for the actual sending function
import smtplib
import getpass

# Import the email modules we'll need
from email.mime.text import MIMEText

# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.
msg = MIMEText("Messages transmis")

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = 'Message de test python'
msg['From'] = "isitech@benke.fr"
msg['To'] = "charlene.r@benke.fr" 
password = getpass.getpass(prompt='Password: ', stream=None)
password = "pythonFormation"
# Send the message via our own SMTP server, but don't include the
# envelope header.
s = smtplib.SMTP('ssl0.ovh.net', 587)
s.connect('ssl0.ovh.net', 587)
s.login('isitech@benke.fr',password)
s.sendmail("isitech@benke.fr", ["charlene.r@benke.fr"], msg.as_string())
s.quit()