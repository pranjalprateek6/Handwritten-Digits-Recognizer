import os
import tensorflow as tf
import cv2
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
import win32gui
from PIL import ImageGrab, Image
from tkinter import *
# mnist = tf.keras.datasets.mnist
# (x_train, y_train), (x_test, y_test) = mnist.load_data()
# x_train = tf.keras.utils.normalize(x_train,axis = 1)
# x_test = tf.keras.utils.normalize(x_test,axis = 1)
# model = tf.keras.models.Sequential()
# model.add(tf.keras.layers.Flatten(input_shape=(28,28)))
# model.add(tf.keras.layers.Dense(128, activation='relu'))
# model.add(tf.keras.layers.Dense(128, activation='relu'))
# model.add(tf.keras.layers.Dense(10, activation='softmax'))
# model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
# model.fit(x_train,y_train, epochs = 5)
# model.save('dig.model')
model = tf.keras.models.load_model('dig.model')
def predict(img):
	res = model.predict(img)
	return (np.argmax(res))
# def predict_digit(img):
#     img = img.resize((28,28))
#     img = img.convert('L')
#     img = np.array(img)
#     img = np.invert(img)
#     img = img.reshape(1,28,28,1)
#     img = img/255.0
#     #predicting the class
#     res = model.predict([img])[0]
#     plt.imshow(img[0], cmap=plt.cm.binary)
#     plt.show()
#     return np.argmax(res), max(res)