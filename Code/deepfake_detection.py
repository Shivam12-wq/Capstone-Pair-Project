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

# Data Gathering
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

# Data Preparation
train_images, test_images, train_labels, test_labels = train_test_split(images, labels, test_size=0.2, random_state=42)

def preprocess_image(image):
    image = cv2.resize(image, (224, 224)) #resize image using OpenCV
    image = image.astype("float") / 255.0
    return image

train_images = np.array([preprocess_image(img) for img in train_images])
test_images = np.array([preprocess_image(img) for img in test_images])


"""# ***4. Modeling *** """

# Model# 1 - Basic CNN
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


#  Model# 2 - Pre-trained Model ResNet50
def resnet_model():
    base_model = ResNet50(include_top=False, weights='imagenet', input_shape=(224, 224, 3))
    for layer in base_model.layers:
        layer.trainable = False  # Freeze pre-trained layers
    model = models.Sequential([
        base_model,
        layers.GlobalAveragePooling2D(),
        layers.Dense(128, activation='relu'),
        layers.Dense(1, activation='sigmoid')
    ])
    return model


# Model# 3- VGG16 Model
def vgg_model():
    base_model = VGG16(include_top=False, weights='imagenet', input_shape=(224, 224, 3))
    for layer in base_model.layers[:-4]:  # Unfreeze the last 4 layers
        layer.trainable = False
    model = models.Sequential([
        base_model,
        layers.Flatten(),
        layers.Dense(256, activation='relu'),
        layers.Dense(1, activation='sigmoid')
    ])
    return model

# Model# 4 - EfficientNetB0 Model
def efficientnet_model():
    # EfficientNetB0 with preloaded ImageNet weights, not including the top, for customized top layers
    base_model = EfficientNetB0(include_top=False, weights='imagenet', input_shape=(224, 224, 3))
    base_model.trainable = False
    model = models.Sequential([
        base_model,
        layers.GlobalAveragePooling2D(),
        layers.Dense(128, activation='relu'),
        layers.Dense(1, activation='sigmoid')
    ])
    return model

# Model Training
def train_model(model, train_images, train_labels, val_images, val_labels, epochs=10):
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    history = model.fit(train_images, train_labels, epochs=epochs, validation_data=(val_images, val_labels))
    return model, history

# Split train set further into train and validation sets
train_images, val_images, train_labels, val_labels = train_test_split(train_images, train_labels, test_size=0.2, random_state=42)

# Train basic CNN model
basic_cnn_model = create_basic_cnn()
basic_cnn_model, basic_cnn_history = train_model(basic_cnn_model, train_images, train_labels, val_images, val_labels)

# Train ResNet50 model
resnet_model = resnet_model()
resnet_model, resnet_history = train_model(resnet_model, train_images, train_labels, val_images, val_labels)

#Train VGG16 model
vgg_model = vgg_model()
vgg_model, vgg_history = train_model(vgg_model, train_images, train_labels, val_images, val_labels)

# Train efficientnetB0 model
efficientnet_model = efficientnet_model()
efficientnet_model, efficientnet_history = train_model(efficientnet_model, train_images, train_labels, val_images, val_labels)


"""# ***5. Evaluation***"""

#  Model Evaluation
def evaluate_model(model, test_images, test_labels):
    test_loss, test_accuracy = model.evaluate(test_images, test_labels)
    return test_accuracy

basic_cnn_accuracy = evaluate_model(basic_cnn_model, test_images, test_labels)
resnet_accuracy = evaluate_model(resnet_model, test_images, test_labels)
vgg_accuracy = evaluate_model(vgg_model, test_images, test_labels)
efficientnet_accuracy = evaluate_model(efficientnet_model, test_images, test_labels)

"""# ***6. Deployment***
"""

# Deployment using Gradio Interface
def predict_deepfake(image):
    processed_image = preprocess_image(image)
    basic_cnn_prediction = basic_cnn_model.predict(np.expand_dims(processed_image, axis=0))[0][0]
    resnet_prediction = resnet_model.predict(np.expand_dims(processed_image, axis=0))[0][0]
    vgg_prediction = vgg_model.predict(np.expand_dims(processed_image, axis=0))[0][0]
    # Threshold for classifying as real or fake
    threshold = 0.5

    # Determine labels based on predictions that are either real or fake
    basic_cnn_label = "Real" if basic_cnn_prediction < threshold else "Fake"
    resnet_label = "Real" if resnet_prediction < threshold else "Fake"
    vgg_label = "Real" if vgg_prediction < threshold else "Fake"
    return basic_cnn_label, resnet_label, vgg_label

# Create a Gradio interface
iface = gr.Interface(fn=predict_deepfake, inputs="image", outputs=["text", "text", "text"], title="Deepfake Detection")
iface.launch()

