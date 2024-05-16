# Capstone-Pair-Project
DeepFake Detection using CRISP-DM

The AI project caters to the need to protect people's digital data or media. As we know deepfake technology is very crucial because it undermines the trust in media content. It can manipulate any media and deceive viewers most likely on the internet by creating hyper-realistic yet entirely fabricated images and videos. Deepfake threats are increasing these days this AI project offers security for users by detecting any malicious activity involving deepfake.

six phases of the CRISP-DM framework:
1. Business Understanding
2. Data Understanding
3. Data Preparation
4. Modelling
5. Evaluation
6. Deployment

# 1. Business Understanding
Developing an AI-based deepfake detection system.

Target Audience: Users who want to identify and protect against deepfake content.

Value Proposition: Provide a reliable tool to detect and flag deepfake images, enhancing user trust and security.

# 2. Data Understanding
Gathering a diverse dataset of real and deepfake images.

We have identified several datasets that offer real and deepfake images for testing and training our deepfake detection model. finally, we gathered some relevant data for our deepfake detection through Kaggle. This dataset directory contains real and fake subdirectories that include real images and deepfake AI-generated images to train and test data. Currently, we have stored the data in Google Drive because storing large amounts of data in Google Drive and accessing it directly from there makes it more efficient.


# 3. Data Preparation
Preprocessing the data by resizing, normalizing pixel value, and converting formats.

The preprocess_image function takes an image file from the given path and uses OpenCV to read it. Then, it resizes the image to the specified target size using cv2.resize. After that, the function normalizes the resized image by dividing all pixel values by 255.0 to make them fall within the range of 0 to 1. 

We are using standard size 224x224 which is commonly used in deep-learning models, especially the CNN (convolutional neural networks) model which will be used in the modeling phase of this deepfake detection.


# 4. Modelling
In the modelling phase, we utilized advanced deep learning methods.

There are many efficient CNN pretrained models but in this project we have chosen Basic CNN, ResNet50, VGG-16 and EfficientNetB0 models to conduct a comprehensive comparative analysis of these models and determine which one gives the highest accuracy in identifying deepfake images.




#5. Evaluation
Evaluate the trained model using the testing set.

Calculating the accuracy and performance in detecting deepfake images to assess the model's effectiveness.

