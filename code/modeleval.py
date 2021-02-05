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

from keras.models import load_model




os.environ['KMP_DUPLICATE_LIB_OK']='True'


"""suit_to_num = {'c': 0, 'd': 1, 'h': 2, 's': 3}

#load training data
X_test = np.array([])
y_test = np.array([])


for file in os.listdir("./data/testsuit"):
    if file.endswith(".png"):
        im = Image.open("./data/testsuit/" + file)
        cur = np.zeros((im.size[1], im.size[0]))
        pix = list(im.getdata())
        for i in range(im.size[1]):
            for j in range(im.size[0]):
                r, g, b = pix[i * im.size[0] + j]
                cur[i][j] = int(0.3*r + 0.6*g + 0.1*b)
        if len(X_test) == 0:
            X_test = np.array([cur])
        else:
            X_test = np.append(X_test, np.array([cur]), axis=0)
        y_test = np.append(y_test, suit_to_num[str(file)[0]])
        
X_test = X_test.reshape(X_test.shape[0], 26, 36, 1)

num_classes = 4
y_test = keras.utils.to_categorical(y_test, num_classes)
        
print("Done loading test data!")

model = load_model('modelsuit.h5')
    
print("Done loading model!")


scores = model.evaluate(X_test, y_test, verbose = 1)
print('Accuracy on test data: {}'.format(scores[1]))"""   



val_to_num = {'2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6, \
               '9': 7, 'T': 8, 'J': 9, 'Q': 10, 'K': 11, 'A': 12}

#load training data
X_test = np.array([])
y_test = np.array([])


for file in os.listdir("./data/testval"):
    if file.endswith(".png"):
        im = Image.open("./data/testval/" + file)
        cur = np.zeros((im.size[1], im.size[0]))
        pix = list(im.getdata())
        for i in range(im.size[1]):
            for j in range(im.size[0]):
                r, g, b = pix[i * im.size[0] + j]
                cur[i][j] = int(0.3*r + 0.6*g + 0.1*b)
        if len(X_test) == 0:
            X_test = np.array([cur])
        else:
            X_test = np.append(X_test, np.array([cur]), axis=0)
        y_test = np.append(y_test, val_to_num[str(file)[0]])
        
X_test = X_test.reshape(X_test.shape[0], 54, 46, 1)

num_classes = 13
y_test = keras.utils.to_categorical(y_test, num_classes)
        
print("Done loading test data!")

model = load_model('modelval.h5')
    
print("Done loading model!")


scores = model.evaluate(X_test, y_test, verbose = 1)
print('Accuracy on test data: {}'.format(scores[1]))   
 


