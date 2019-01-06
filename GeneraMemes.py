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
    #imagen = Image.open("kratos.jpg")
    
    #imagenMarco = ImageOps.expand(imagen, border=5, fill=(0,0,255))
#    plt.imshow(imagen)
#    plt.show()
    x, y = imagen.size
    TamañoFont=x/20
    imagenMarco=_resize_to_square(imagen, fill=0)
#    plt.imshow(imagenMarco)
#    plt.show()
    draw = ImageDraw.Draw(imagenMarco)
    font = ImageFont.truetype("arial.ttf", int(TamañoFont))
    
    #text = "Hola"
    text=text.replace('.', '.\n') 
    #text=text.encode('utf-8')
    #text=text.decode('utf-8')
    lines = text.splitlines()
    #print(lines)
    linecount=0
    for line in lines:
        vacios=line.count(' ')
        if vacios > 6:
            count=0
            char=0
            linetemp=list(line)
            for i in line:
                #print("count"+str(count))
                #print("char"+str(char))
                if i==' ':
                    if char > 35:
                        linetemp[count]='\n'
                        char=0
                count+=1
                char+=1
            line=''.join(linetemp)
            #print(line)
        lines[linecount]=line
        linecount+=1
    #print(lines)          
    w = font.getsize(max(lines, key=lambda s: len(s)))[0]
    h = font.getsize(text)[1] * len(lines)
    x, y = imagenMarco.size
    x /= 2
    x -= w / 2
    y /= 2
    y -= h / 2
    #y_text=40
    y_text=10
    for line in lines:
        draw.text((10, y_text), line, font=font, fill="Black", align="center")
        #y_text += 580
        y_text = 314
    #draw.text((x, 40), text , font=font, fill="Black", align="center")
    plt.imshow(imagenMarco)
    plt.show()
    return(imagenMarco)
    #imagenMarco.save("Meme/meme1.jpg")


#    
#def main():
# Creamos cada proceso    
    
#
count=0
for j in range(25):   
    for i in range(5):
        call(['python', 'run_inference.py', 'imagenes/image_{}.jpg'.format(j)])
        #process2 = subprocess.Popen(['python', 'sample.py'])
        call(['python', 'sample.py'])
        archivo = open("broma.txt", "r") 
        contenido = archivo.readlines()
        text=contenido[2]
        
        #print(contenido)
        imagen = Image.open("imagenes/image_{}.jpg".format(j))
        #text = "Boyyyy"
        print(text)
        Meme=GeneraMeme(imagen,text)
        Meme.save("Meme/meme_{}.jpg".format(count))
        archivo.close()
        count+=1
#if __name__ == '__main__':
#    main()