# -*- coding: utf-8 -*-
"""Deepfake_Detection.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1wCimy8h13QbDKZKtSUfH3CiOYWrwjUb-

# **DEEPFAKE DETECTION**

> Using CRISP-DM Framework

# ***1. Business Understanding***


> Developing an AI-based deepfake  detection system.

Target Audience: Users who want to identify and protect against deepfake content.

Value Proposition: Provide a reliable tool to detect and flag deepfake images, enhancing user trust and security.

# ***2. Data Understanding***


> Gathering a diverse dataset of real and deepfake images.

We have identified several datasets that offer real and deepfake images for testing and training our deepfake detection model. However, accessing these datasets requires meeting certain requirements. Currently, we are in the process of fulfilling those requirements. Once we obtain the dataset, we will proceed with data exploration, which will involve tasks such as splitting and organizing the data.
"""

import os
import numpy as np
import cv2
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.applications import ResNet50
import gradio as gr

# Step 1: Data Gathering
def load_data(data_dir):
    images = []
    labels = []
    for label in os.listdir(data_dir):
        label_dir = os.path.join(data_dir, label)
        for image_file in os.listdir(label_dir):
            image_path = os.path.join(label_dir, image_file)
            image = cv2.imread(image_path)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB
            images.append(image)
            labels.append(1 if label == 'fake' else 0)  #'fake' folder contains deepfake images
    return np.array(images), np.array(labels)

data_dir = "/content/drive/MyDrive/Deepfake_Dataset"
images, labels = load_data(data_dir)


"""# ***3. Data Preparation***

> Preprocessing the data by resizing, normalizing pixel value, and converting formats.

The **preprocess_image** function takes an image file from the given path and uses OpenCV to read it. Then, it resizes the image to the specified target size using cv2.resize. After that, the function normalizes the resized image by dividing all pixel values by 255.0 to make them fall within the range of 0 to 1. Finally, it saves the resized image as 'resized.png' using cv2.imwrite and returns the preprocessed image as a NumPy array.

We are using standarsd size 224x224 which is commonly used in deeplearning models specially like CNN (convolutional neural networks) model which will be used in modelling phase of this deepfake detection.
"""

# Step 2: Data Preparation
train_images, test_images, train_labels, test_labels = train_test_split(images, labels, test_size=0.2, random_state=42)

def preprocess_image(image):
    image = cv2.resize(image, (224, 224))
    image = image.astype("float") / 255.0
    return image

train_images = np.array([preprocess_image(img) for img in train_images])
test_images = np.array([preprocess_image(img) for img in test_images])


"""# ***4. Modeling *** """

# Step 3: Modeling - Basic CNN
def create_cnn():
    model = models.Sequential([
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(128, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Flatten(),
        layers.Dense(128, activation='relu'),
        layers.Dense(1, activation='sigmoid')
    ])
    return model

# Step 4: Model Training
def train_model(model, train_images, train_labels, val_images, val_labels, epochs=10):
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    history = model.fit(train_images, train_labels, epochs=epochs, validation_data=(val_images, val_labels))
    return model, history


"""# ***5. Evaluation***

# ***6. Deployment***
"""
