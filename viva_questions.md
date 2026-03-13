# Viva Questions & Answers - Image Colorization CNN

## 1. What is the main objective of this project?
The objective is to use a Convolutional Neural Network (CNN) to automatically predict and add realistic colors to grayscale images by learning from a large dataset of color photos.

## 2. Which color space is used in this project and why?
The **L*a*b* color space** is used. 
- **L (Lightness):** Represents the grayscale information.
- **a & b (Color components):** Represent the color signals.
It is used because it separates brightness from color, allowing the model to focus solely on predicting color channels for a given brightness channel.

## 3. How does the CNN predict colors?
The CNN takes the 'L' channel as input. It passes through multiple layers of convolutions to extract features and finally outputs the predicted 'a' and 'b' channels, which are then combined with the original 'L' channel.

## 4. What is the role of the `pts_in_hull.npy` file?
It contains the cluster center points for the color space. Since the model treats colorization as a classification task (predicting which color bucket a pixel belongs to), these points define those buckets.

## 5. What are the limitations of this approach?
The model predicts "plausible" colors. It might not know the exact original color (e.g., if a car was red or blue originally), but it will pick a color that looks realistic based on its training.

## 6. What is the function of the `prototxt` and `caffemodel` files?
- **Prototxt:** Defines the architecture (layers) of the CNN.
- **Caffemodel:** Contains the actual trained weights (knowledge) of the model.

## 7. Why use OpenCV's DNN module?
OpenCV's DNN (Deep Neural Network) module is highly optimized for inference on CPUs, making it ideal for running pre-trained models locally without needing heavy frameworks like TensorFlow or PyTorch during runtime.

## 8. What is "Mean Centering" in preprocessing?
In this model, we subtract 50 from the 'L' channel values. This centers the data around zero, which helps the neural network process information more efficiently.

## 9. Can this model colorize any image?
It works best on images that resemble its training data (landscapes, objects, people). It might struggle with highly abstract or very low-quality old photos.

## 10. How can we improve this project in the future?
- Using **Generative Adversarial Networks (GANs)** for more vibrant colors.
- Adding **User Interaction** where a user can "hint" a color by brushing over an area.
- Applying it to **Video Frames**.

---

### Project Details for Documentation:
- **Problem Statement:** Manual colorization of historical photos is time-consuming and requires artistic skill. An automated AI-based solution is needed.
- **Abstract:** This project implements an automated image colorization system using a Deep CNN. By leveraging the L*a*b* color space, the model predicts color distributions for grayscale inputs.
- **Architecture:** Input (L Channel) -> CNN (Deep Convolutional Layers) -> Predicted AB Channels -> Final Color Image (L + predicted AB).
