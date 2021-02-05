#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 10:45:55 2020

@author: stanley
"""

import keras
import numpy as np
import os
from PIL import Image
import pyscreenshot as ImageGrab


from keras.models import load_model




os.environ['KMP_DUPLICATE_LIB_OK']='True'


num_to_suit = {0: 'c', 1: 'd', 2: 'h', 3: 's'}
num_to_val = {0: '2', 1: '3', 2: '4', 3: '5', 4: '6', 5: '7', 6: '8', \
              7: '9', 8: 'T', 9: 'J', 10: 'Q', 11: 'K', 12: 'A'}


modelsuit = load_model('modelsuit.h5')
modelval = load_model('modelval.h5')
    
print("Done loading models!")


class Screenshotter:
    """
    Ideally suitval_dict should be intrisic to this class, but for
    data collection purposes I'm making it global for now
    """
    
    def __init__(self, screen_position, id_type):
        self.screen_position = screen_position
        self.id_type = id_type
        
    def go(self):
        im = ImageGrab.grab(bbox = self.screen_position)
        im.save('hash.png')
        im = Image.open("hash.png")
        cur = np.zeros((im.size[1], im.size[0]))
        pix = list(im.getdata())
        for i in range(im.size[1]):
            for j in range(im.size[0]):
                r, g, b = pix[i * im.size[0] + j]
                cur[i][j] = int(0.3*r + 0.6*g + 0.1*b)
        if self.id_type == "suit":
            X_test = np.array([cur])
            X_test = np.reshape(X_test, (1, 26, 36, 1))
            pred = modelsuit.predict(X_test)
            _, pos = np.where(pred == 1)
            pos = int(pos)
            print(num_to_suit[pos])
        elif self.id_type == "val":
            X_test = np.array([cur])
            X_test = np.reshape(X_test, (1, 54, 46, 1))
            pred = modelval.predict(X_test)
            _, pos = np.where(pred == 1)
            pos = int(pos)
            print(num_to_val[pos])
        
        
        
        
        
#Coordinates
#big screen
val1 = Screenshotter((545, 576, 568, 603), "val")
suit1 = Screenshotter((547, 609, 565, 622), "suit")
val2 = Screenshotter((625, 576, 648, 603), "val")
suit2 = Screenshotter((627, 609, 645, 622), "suit")
    
 


