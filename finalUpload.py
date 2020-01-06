from PIL import Image, ImageDraw
import os, sys
from random import SystemRandom
random = SystemRandom()
import numpy as np
import testfire
def functionName(infile, key):
        
        img0 = Image.open(infile)

        f, e = os.path.splitext(infile)
        out_filename_A = f+"_A.png"
        out_filename_B = f+"_B.png"
        img = img0.convert('L')
        img = img.convert('1')

        width = img.size[0]*2
        height = img.size[1]*2

        out_image_A = Image.new('1', (width, height))
        out_image_B = Image.new('1', (width, height))
        draw_A = ImageDraw.Draw(out_image_A)
        draw_B = ImageDraw.Draw(out_image_B)

        patterns=((1,1,0,0), 
                  (1,0,1,0), 
                  (1,0,0,1), 
                  (0,1,1,0), 
                  (0,1,0,1), 
                  (0,0,1,1))

        for x in range(int(width/2)):
                for y in range(int(height/2)):
                        pixel=img.getpixel((x,y))
                        #selecting a random pattern from the list of given patterns. 
                        pat=random.choice(patterns)
                        #expanding one pixel to 4 pixels
                        draw_A.point((x*2, y*2), pat[0])
                        draw_A.point((x*2+1, y*2), pat[1])
                        draw_A.point((x*2, y*2+1), pat[2])
                        draw_A.point((x*2+1, y*2+1), pat[3])

                        if pixel==0:
                                draw_B.point((x*2, y*2), 1-pat[0])
                                draw_B.point((x*2+1, y*2), 1-pat[1])
                                draw_B.point((x*2, y*2+1), 1-pat[2])
                                draw_B.point((x*2+1, y*2+1), 1-pat[3])
                        else:
                                draw_B.point((x*2, y*2), pat[0])
                                draw_B.point((x*2+1, y*2), pat[1])
                                draw_B.point((x*2, y*2+1), pat[2])
                                draw_B.point((x*2+1, y*2+1), pat[3])
                        
        #out_image_A.show()
        #out_image_B.show()
        ##        			
        out_image_A.save(out_filename_A, 'png')
        out_image_B.save(out_filename_B, 'png')
        
        import merge
        merge.mergeFunction(f)
        folderName = str(key)

        from EncDec import enc
        path_1 = enc(key, out_filename_A)
        path_2 = enc(key, out_filename_B)
        #print(path_1, path_2)
        #NAME OF THE FOLDER SHOULD BE THE KEY OF THE ENC IMAGE!
        
        print(testfire.send_image(folderName+'/first',imagePath =  path_1))
        print(testfire.send_image(folderName+'/second', imagePath = path_2))
        
        testfire.send_image(folderName, 'output_file.png')

