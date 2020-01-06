#STEP 1: GENERATE KEY FROM THE RECEIVER'S EMAIL ADDRESS
import mail
import EncDec
from firebase import firebase
import json


def bfunc(mail_id, fileAddr):
    RE_EMAIL = mail_id

    #STEP 2: SELECT THE IMAGE TO SEND
    from finalUpload import functionName
    infile = fileAddr

    #generate key
    key = EncDec.makeKey(RE_EMAIL)
    #upload key to RTDB
    firebaseRT = firebase.FirebaseApplication('https://mini-257604.firebaseio.com/')

    result = firebaseRT.post(f'/mini-257604/{str(key)}', infile)
    #result= firebaseRT.get(f'/mini-257604/{str(key)}', None)
    #print(list(result.values())[0].strip('.jpg'))


    #print(result)

    functionName(infile, key)

    #sendEmail
    mail.do_stuff(RE_EMAIL, key)
    print('EMAIL SENT TO RECEIVER')



