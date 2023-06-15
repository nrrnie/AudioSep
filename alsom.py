import sys
import argparse
import librosa
import musdb
import ffmpeg
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from IPython.display import Audio

def downloadMUSDB():
    train = musdb.DB(download=True, subsets='train', split=None)
    test = musdb.DB(download=True, subsets='test', split=None)
    return train, test

def spec(dataset, targets=False):
    return 

def make_model():
    model = tf.keras.Sequential([
        tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape = (1025, 587)),
        tf.keras.layers.MaxPooling2D((2, 2)),
        tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D((2, 2)),
        tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(64, activation="relu"),
        tf.keras.layers.Dense(5, activation='softmax')
    ])

    return model

def train_model(model):
    model.fit()    


    return

def main():

    short_train, short_test = downloadMUSDB()

    mus = musdb.DB(
        root = r'./musdb/',
    )

    


    #model = make_model()

    #model.compile(optimizer='adam', loss=tf.keras.losses.MeanSquaredError, metrics=['acc'])

    print("ready")



if __name__ == '__main__':
    main()