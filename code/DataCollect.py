#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 11:12:54 2020

@author: stanley
"""


from PIL import Image
import pyscreenshot as ImageGrab
import os
  

class Screenshotter:
    """
    Ideally suitval_dict should be intrisic to this class, but for
    data collection purposes I'm making it global for now
    """
    count = 23
    
    def __init__(self, screen_position):
        self.screen_position = screen_position
        
    def go(self):
        im = ImageGrab.grab(bbox = self.screen_position)
        im.save(str(Screenshotter.count) + '.png')
        Screenshotter.count += 1
        
        
#Coordinates
#big screen
val1 = Screenshotter((545, 576, 568, 603))
suit1 = Screenshotter((547, 609, 565, 622))
val2 = Screenshotter((625, 576, 648, 603))
suit2 = Screenshotter((627, 609, 645, 622))

        
        

def filterDupes():
    suits = ['club', 'diamond', 'heart', 'spade']
    for s in suits:
        imgSet = set()
        for file in os.listdir("./data/" + s):
            if file.endswith(".png"):
                im = Image.open("./data/" + s + "/" + file)
                pix = list(im.getdata())
                for j in range(len(pix)):
                    r, g, b = pix[j]
                    pix[j] = int(0.3*r + 0.6*g + 0.1*b)
                if tuple(pix) in imgSet:
                    print("REMOVE " + file)
                    os.remove("./data/" + s + "/" + file)
                else:
                    imgSet.add(tuple(pix))
        
            
            
def testEq(num_a, num_b):
    im_a = Image.open(str(num_a) + '.png', 'r')
    pix_a = list(im_a.getdata())
    sum_a = 0
    for j in range(len(pix_a)):
            r, g, b = pix_a[j]
            pix_a[j] = int(0.3*r + 0.6*g + 0.1*b)
            sum_a += pix_a[j]
    
    im_b = Image.open(str(num_b) + '.png', 'r')
    pix_b = list(im_b.getdata())
    sum_b = 0
    for j in range(len(pix_b)):
            r, g, b = pix_b[j]
            pix_b[j] = int(0.3*r + 0.6*g + 0.1*b)
            sum_b += pix_b[j]
            
    print(sum_a, sum_b)
        
        
def renumber(num):
    suits = ['club', 'diamond', 'heart', 'spade']
    for s in suits:
        count = num
        for file in os.listdir("./data/" + s):
            #if file.endswith(".png"):
                os.rename("./data/" + s + "/" + file, "./data/" + s + "/" + s + str(count) + ".png")
                count += 1
                
    
    
    
"""count = 0
for file in os.listdir("./data/heart"):
    os.rename("./data/heart/" + file, "./data/heart/heart" + str(count) + '.png')
    count += 1"""
        
  
    
    
    
        
        