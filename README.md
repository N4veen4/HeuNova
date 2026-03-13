# Image Colorization using CNN

A beginner-friendly mini project that uses a Convolutional Neural Network (CNN) to colorize black-and-white images. Built with Python, Streamlit, and OpenCV.

## 📌 Abstract
Image colorization is the process of taking a grayscale image and predicting the color information for each pixel based on a deep learning model. This project uses a pre-trained CNN model (based on the research by Richard Zhang et al.) to provide realistic (though not necessarily historically accurate) colorization of images.

## 🎯 Objectives
- To implement a deep learning-based image colorization pipeline.
- To provide a user-friendly interface for uploading and colorizing images.
- To understand the L*a*b* color space and its role in image processing.

## 🛠️ Tools Used
- **Language:** Python
- **UI Framework:** Custom HTML5/CSS3/JS (Premium UI)
- **Backend:** FastAPI
- **Computer Vision:** OpenCV (DNN module)
- **Numerical Processing:** NumPy

## 📥 Installation & Setup

1. **Clone the project** or download the files.
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Download Model Files:**
   The pre-trained model files are required for the project to work. Download them and place them inside the `models/` folder:
   - [colorization_deploy_v2.prototxt](https://raw.githubusercontent.com/richzhang/colorization/caffe/colorization/models/colorization_deploy_v2.prototxt)
   - [pts_in_hull.npy](https://raw.githubusercontent.com/richzhang/colorization/caffe/colorization/resources/pts_in_hull.npy)
   - [colorization_release_v2.caffemodel](https://storage.openvinotoolkit.org/repositories/datumaro/models/colorization/colorization_release_v2.caffemodel) (Updated Reliable Link)

4. **Run the App:**
   ```bash
   python main.py
   ```
   Visit `http://localhost:8000` in your browser.

## 🚀 How it Works
1. **L*a*b* Color Space:** The model works in the L*a*b* color space. The 'L' channel (lightness) represents the grayscale version of the image.
2. **CNN Prediction:** The CNN takes the 'L' channel as input and predicts the 'a' and 'b' (color) channels.
3. **Reconstruction:** The predicted 'a' and 'b' channels are combined with the original 'L' channel to form the final colorized image.

## ⚠️ Limitations
- Predictions are plausible estimates, not guarantees of original colors.
- High-resolution images may be downscaled during processing to save time.
- Complex scenes with many colorful objects might have blended or muted colors.

## 🔮 Future Improvements
- Support for video colorization.
- Fine-tuning the model on specific datasets (e.g., historical photos).
- Using more advanced architectures like GANs for more vivid colors.
