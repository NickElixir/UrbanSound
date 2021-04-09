import os
import pandas as pd
from glob import glob
import numpy as np
import time
import keras.backend as K
import librosa
import librosa.display
import pylab
import matplotlib.pyplot as plt
from matplotlib import figure
import gc
from path import Path
import soundfile
from keras.layers import Dense, Activation, Flatten, Dropout, BatchNormalization, Conv2D, MaxPooling2D, GlobalAveragePooling2D
from keras.layers.advanced_activations import LeakyReLU
from keras.models import Sequential, Model
from keras import regularizers, optimizers
from keras import applications
from keras import layers
from keras import models
from keras.optimizers import Adam
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing import image

DIMENSION_OF_PIC = 200
PATH_TO_WEIGHTS = '/home/nippon/DL/'
WEIGHTS_FILENAME = 'pretrained-weights-resnet10_mono_2021-03-11_23-07-36.h5'

def create_spectrogram(filename,name):
    plt.interactive(False)
    clip, sample_rate = librosa.load(filename, sr=None)
    fig = plt.figure(figsize=[0.72,0.72])
    ax = fig.add_subplot(111)
    ax.axes.get_xaxis().set_visible(False)
    ax.axes.get_yaxis().set_visible(False)
    ax.set_frame_on(False)
    S = librosa.feature.melspectrogram(y=clip, sr=sample_rate)
    librosa.display.specshow(librosa.power_to_db(S, ref=np.max))
    filename  = 'spectros/' + 'tmp' + '.jpg'
    plt.savefig(filename, dpi=3000, bbox_inches='tight',pad_inches=0)

def process_prediction():
    model = applications.ResNet50(
        include_top=True,
        weights=None,
        input_tensor=None,
        input_shape=(DIMENSION_OF_PIC,DIMENSION_OF_PIC,3),
        classes=10
    )
    model.compile(optimizers.RMSprop(lr=0.00001, decay=1e-6),loss="categorical_crossentropy",metrics=["accuracy"])
    model = models.load_model(PATH_TO_WEIGHTS + WEIGHTS_FILENAME)

    Data_dir = np.array(glob('wavs/*'))
    for file in Data_dir[len(Data_dir) - 1:]:
        filename,name = file,file.split('/')[-1].split('.')[0]
        create_spectrogram(filename,name)
    Data_dir = np.array(glob('spectros/*'))
    img = image.load_img(Data_dir[0], target_size=(DIMENSION_OF_PIC,DIMENSION_OF_PIC))
    img = np.expand_dims(img, axis=0)
    result = model.predict(img)
    predicted_class_indices=np.argmax(result, axis=1)
    prediction_holder = ['air conditioner',
                         'car horn',
                         'children playing',
                         'dog bark',
                         'drilling',
                         'engine idling',
                         'gun shot',
                         'jackhammer',
                         'siren',
                         'street music']
    print(prediction_holder[int(predicted_class_indices)])

    return int(predicted_class_indices)
process_prediction()
