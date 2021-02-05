#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 10:55:49 2020

@author: stanley
"""


import keras
import numpy as np
import os
from PIL import Image

from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K



os.environ['KMP_DUPLICATE_LIB_OK']='True'


"""#load training data for suits
suits = ['club', 'diamond', 'heart', 'spade']
X_train = np.array([])
y_train = np.array([])

for c in range(len(suits)):
    s = suits[c]
    for file in os.listdir("./data/" + s):
        if file.endswith(".png"):
            im = Image.open("./data/" + s + "/" + file)
            cur = np.zeros((im.size[1], im.size[0]))
            pix = list(im.getdata())
            for i in range(im.size[1]):
                for j in range(im.size[0]):
                    r, g, b = pix[i * im.size[0] + j]
                    cur[i][j] = int(0.3*r + 0.6*g + 0.1*b)
            if len(X_train) == 0:
                X_train = np.array([cur])
            else:
                X_train = np.append(X_train, np.array([cur]), axis=0)
            y_train = np.append(y_train, c)
                
                
(x_mnist, y_mnist), _ = mnist.load_data()
        

print("Done loading data!")

X_train = X_train.reshape(X_train.shape[0], 26, 36, 1)
input_shape = (26, 36, 1)

num_classes = 4
y_train = keras.utils.to_categorical(y_train, num_classes)

X_train = X_train.astype('float32')
X_train /= 255

print("Done preprocessing data!")

batch_size = 4
epochs = 10

model = Sequential()
model.add(Conv2D(32, kernel_size = (3, 3), activation = 'relu', input_shape = input_shape))
model.add(Conv2D(64, (3, 3), activation = 'relu'))
model.add(MaxPooling2D(pool_size = (2, 2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(256, activation = 'relu'))
model.add(Dropout(0.5))
model.add(Dense(num_classes, activation = 'softmax'))

model.compile(loss = keras.losses.categorical_crossentropy, \
              optimizer = keras.optimizers.Adadelta(), metrics=['accuracy'])
    
print("Done setting up CNN!")

#hist = model.fit(X_train, y_train, batch_size = batch_size, epochs = epochs, \
#                 verbose = 1, validation_data = (X_test, y_test))

hist = model.fit(X_train, y_train, batch_size = batch_size, epochs = epochs, \
                 verbose = 1, validation_data  = (X_train[:10], y_train[:10]))
    
print("Done training model!")

model.save('modelsuit.h5')

print("Saved model.")"""



#load training data
vals = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
X_train = np.array([])
y_train = np.array([])

for c in range(len(vals)):
    v = vals[c]
    for file in os.listdir("./data/" + v):
        if file.endswith(".png"):
            im = Image.open("./data/" + v + "/" + file)
            cur = np.zeros((im.size[1], im.size[0]))
            pix = list(im.getdata())
            for i in range(im.size[1]):
                for j in range(im.size[0]):
                    r, g, b = pix[i * im.size[0] + j]
                    cur[i][j] = int(0.3*r + 0.6*g + 0.1*b)
            if len(X_train) == 0:
                X_train = np.array([cur])
            else:
                X_train = np.append(X_train, np.array([cur]), axis=0)
            y_train = np.append(y_train, c)
                
                
#(x_mnist, y_mnist), _ = mnist.load_data()
        

print("Done loading data!")

X_train = X_train.reshape(X_train.shape[0], 54, 46, 1)
input_shape = (54, 46, 1)

num_classes = 13
y_train = keras.utils.to_categorical(y_train, num_classes)

X_train = X_train.astype('float32')
X_train /= 255

print("Done preprocessing data!")

batch_size = 13
epochs = 12

model = Sequential()
model.add(Conv2D(32, kernel_size = (3, 3), activation = 'relu', input_shape = input_shape))
model.add(Conv2D(64, (3, 3), activation = 'relu'))
model.add(MaxPooling2D(pool_size = (2, 2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(256, activation = 'relu'))
model.add(Dropout(0.5))
model.add(Dense(num_classes, activation = 'softmax'))

model.compile(loss = keras.losses.categorical_crossentropy, \
              optimizer = keras.optimizers.Adadelta(), metrics=['accuracy'])
    
print("Done setting up CNN!")

#hist = model.fit(X_train, y_train, batch_size = batch_size, epochs = epochs, \
#                 verbose = 1, validation_data = (X_test, y_test))

hist = model.fit(X_train, y_train, batch_size = batch_size, epochs = epochs, \
                 verbose = 1, validation_data  = (X_train[:10], y_train[:10]))
    
print("Done training model!")

model.save('modelval.h5')

print("Saved model.")



