#!/usr/bin/python
# -*- coding: utf-8 -*-


from PIL import Image
from PIL import ImageDraw
from math import sqrt
import random

initIterations = 50
iterations = 100000

def aff(a, b, c, d, e, f):
    return lambda x, y: (a*x + b*y + e, c*x + d*y + f)

def getNextPoint(x, y, affTransforms):
    return random.choice(affTransforms) (x, y)

def sierpinski():
    width = 464
    height = 464
    image = Image.new('RGB', (width, height), (255, 255, 255)) 

    draw = ImageDraw.Draw(image)

    affTransforms = [
#                aff(a,b,c,d,e,f),
#                aff(a1,b1,c1,d1,e1,f1),
#                aff(a2,b2,c2,d2,e2,f2)
            ]

    x = random.randint(0, width - 1) 
    y = random.randint(0, height - 1) 

    for i in range(initIterations):
        (x, y) = getNextPoint(x, y, affTransforms)

    for i in range(iterations):
        draw.point( [(int(x), int(y))] , fill= 'orange')
        (x, y) = getNextPoint(x, y, affTransforms)


    image.save("sierpinski.gif")


if __name__ == '__main__':
    sierpinski()
