# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 00:19:43 2019

@author: angel
"""

from subprocess import call
from PIL import Image, ImageDraw, ImageFont, ImageOps
import numpy as np
import matplotlib.pyplot as plt

def _resize_to_square(img, fill=0):
    if img.width > img.height:
        border = (0, (img.width - img.height) // 2)
    elif img.width < img.height:
        border = ((img.height - img.width) // 2, 0)
    else:
        border = (0, (img.height) // 4)
    return ImageOps.expand(img, border, fill="White")

def GeneraMeme(imagen,text):   
    x, y = imagen.size
    TamañoFont=x/20
    imagenMarco=_resize_to_square(imagen, fill=0)
    draw = ImageDraw.Draw(imagenMarco)
    font = ImageFont.truetype("arial.ttf", int(TamañoFont))
    
    text=text.replace('.', '.\n') 
    lines = text.splitlines()
    linecount=0
    for line in lines:
        vacios=line.count(' ')
        if vacios > 6:
            count=0
            char=0
            linetemp=list(line)
            for i in line:
                if i==' ':
                    if char > 35:
                        linetemp[count]='\n'
                        char=0
                count+=1
                char+=1
            line=''.join(linetemp)
        lines[linecount]=line
        linecount+=1          
    y_text=10
    for line in lines:
        draw.text((10, y_text), line, font=font, fill="Black", align="center")
        y_text = 314
    plt.imshow(imagenMarco)
    plt.show()
    return(imagenMarco)


#    
def main(args):
    if len(args)!=1:
        call(['python', 'run_inference.py', args[1]])
        call(['python', 'sample.py'])
        archivo = open("broma.txt", "r") 
        contenido = archivo.readlines()
        text=contenido[2]
        
        imagen = Image.open(args[1])
        Meme=GeneraMeme(imagen,text)
        Meme.save("Meme/meme.jpg")
        archivo.close()
    else:
        count=0
        for j in range(25):   
            for i in range(5):
                call(['python', 'run_inference.py', 'imagenes/image_{}.jpg'.format(j)])
                call(['python', 'sample.py'])
                archivo = open("broma.txt", "r") 
                contenido = archivo.readlines()
                text=contenido[2]
                
                imagen = Image.open("imagenes/image_{}.jpg".format(j))
                #print(text)
                Meme=GeneraMeme(imagen,text)
                Meme.save("Meme/meme_{}.jpg".format(count))
                archivo.close()
                count+=1
if __name__ == '__main__':
    import sys
    main(sys.argv)