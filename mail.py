import smtplib
EMAIL_ADDRESS = 'sarthaksat2@gmail.com'
EMAIL_PASSWORD = 'yfhxjbklrnrabmdc'

def do_stuff(RE_EMAIL, key):
    
    #if the folder name is too large, then reduce the size of the key
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        subject = 'SECRET IMAGE RECEIVED'
        body = key

        msg = f'SUBJECT:{subject}\n\nYou have received an image, to decrypt, enter the following key:\n{body}'

        smtp.sendmail(EMAIL_ADDRESS, RE_EMAIL, msg)
        #return id1



    
    
    
