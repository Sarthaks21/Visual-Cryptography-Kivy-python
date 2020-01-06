from PIL import Image, ImageDraw
import sys

def mergeFunction(nameOfImage):
    infile1 = Image.open(nameOfImage+'_A.png')
    infile2 = Image.open(nameOfImage+'_B.png')
    #print (f'infile1 {infile1.size} \ninfile2 {infile2.size}')
    outfile = Image.new('1', infile1.size)

    for x in range(infile1.size[0]):
        for y in range(infile1.size[1]):
            outfile.putpixel((x, y), min(infile1.getpixel((x, y)), infile2.getpixel((x, y))))

    outfile.save("output_file.png")
    #outfile.show()
