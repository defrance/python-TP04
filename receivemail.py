import email
import imaplib

EMAIL = 'isitech@benke.fr'
PASSWORD = 'pythonFormation'
SERVER = 'ssl0.ovh.net'

# connect to the server and go to its inbox
mail = imaplib.IMAP4_SSL(SERVER)
mail.login(EMAIL, PASSWORD)
# we choose the inbox but you can select others
mail.select('inbox')

status, data = mail.search(None, 'UnSeen')
mail_ids = []
for block in data:
    mail_ids += block.split()

for i in mail_ids:
    status, data = mail.fetch(i, '(RFC822)')

    for response_part in data:
        if isinstance(response_part, tuple):
            message = email.message_from_bytes(response_part[1])

            mail_from = message['from']
            mail_subject = message['subject']

            if message.is_multipart():
                mail_content = ''

                for part in message.get_payload():
                    if part.get_content_type() == 'text/plain':
                        mail_content += part.get_payload()
            else:
                mail_content = message.get_payload()

            # gestion des pièces jointes
            attachment = message.get_payload()[1]
            attachment.get_content_type() # return the first item in attachments
            open('attachment.pdf', 'wb').write(attachment.get_payload(decode=True))



            # and then let's show its result
            print(f'From: {mail_from}')
            print(f'Subject: {mail_subject}')
            print(f'Content: {mail_content}')