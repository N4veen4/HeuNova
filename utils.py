import cv2
import numpy as np

def preprocess_image(image_bytes):
    """
    Converts uploaded image bytes to an OpenCV image and extracts the L channel.
    """
    nparr = np.frombuffer(image_bytes, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    # Scale pixels to [0, 1] range
    scaled = image.astype("float32") / 255.0
    
    # Convert to LAB color space
    lab = cv2.cvtColor(scaled, cv2.COLOR_BGR2LAB)
    
    # Extract the L channel
    l_channel = lab[:, :, 0]
    
    return image, l_channel, lab

def postprocess_image(l_channel, ab_predicted, original_shape):
    """
    Combines the original L channel with predicted AB channels.
    """
    # Combine L and predicted AB
    colorized = np.concatenate((l_channel[:, :, np.newaxis], ab_predicted), axis=2)
    
    # Convert back to BGR
    colorized = cv2.cvtColor(colorized, cv2.COLOR_LAB2BGR)
    
    # Clip values to [0, 1] and scale to [0, 255]
    colorized = np.clip(colorized, 0, 1)
    colorized = (255 * colorized).astype("uint8")
    
    # Resize back to original dimensions
    colorized = cv2.resize(colorized, (original_shape[1], original_shape[0]))
    
    return colorized
