import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC as pbk
import mail
def makeKey(RE_EMAIL):
    word = RE_EMAIL
    password = word.encode()
    salt = b'\xce\x0c\xd5K\xd4E\x8dqR\xda1\\D-\x04\x08'

    kdf = pbk(
        algorithm = hashes.SHA256(),
        length = 32,
        salt = salt,
        iterations = 10000,
        backend = default_backend()
    )

    key = base64.urlsafe_b64encode(kdf.derive(password))
    #print(key)
    return key


def enc(key, filename):
    with open(filename, 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)

#check for other formats as well
    filename = filename.strip('.png')
    #print('filename', filename)
    with open(filename+'_encrypted.png', 'wb') as f:
        f.write(encrypted)
    filename = filename+'_encrypted.png'
    #print(filename)
    return filename

def dec(key):
    with open('test.jpg', 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    encrypted = fernet.decrypt(data)

    with open('decTest.jpg', 'wb') as f:
        f.write(encrypted)

#key = makeKey('sarthaksat2@gmail.com')
#enc(key, 'smit_A.png')
#dec(key)
