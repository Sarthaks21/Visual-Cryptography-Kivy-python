from firebase import firebase
from PIL import Image, ImageDraw
import time
firebase = firebase.FirebaseApplication('https://mini-257604.firebaseio.com/')

def reFun(dkey):
    
    #ask for the key
    key = dkey
    #download both the images

    result= firebase.get(f'/mini-257604/{str(key)}', None)
    fname = list(result.values())[0].strip('.jpg')
    #print(fname)
    #download both the shares and then merge them or alternatively, download the merged image
    outfile = Image.open('output_file.png')
    outfile.show()
