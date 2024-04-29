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

We have identified several datasets that offer real and deepfake images for testing and training our deepfake detection model. However, accessing these datasets requires meeting certain requirements. Currently, we are in the process of fulfilling those requirements. Once we obtain the dataset, we will proceed with data exploration, which will involve tasks such as splitting and organizing the data.


# 3. Data Preparation
Preprocessing the data by resizing, normalizing pixel value, and converting formats.

The preprocess_image function takes an image file from the given path and uses OpenCV to read it. Then, it resizes the image to the specified target size using cv2.resize. After that, the function normalizes the resized image by dividing all pixel values by 255.0 to make them fall within the range of 0 to 1. Finally, it saves the resized image as 'resized.png' using cv2.imwrite and returns the preprocessed image as a NumPy array.

We are using standard size 224x224 which is commonly used in deeplearning models specially like CNN (convolutional neural networks) model which will be used in modeling phase of this deepfake detection.


