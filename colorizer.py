import cv2
import numpy as np
import os

class ImageColorizer:
    def __init__(self, model_dir="models"):
        # File paths
        prototxt = os.path.join(model_dir, "colorization_deploy_v2.prototxt")
        model = os.path.join(model_dir, "colorization_release_v2.caffemodel")
        points = os.path.join(model_dir, "pts_in_hull.npy")
        
        # Check if files exist
        if not (os.path.exists(prototxt) and os.path.exists(model) and os.path.exists(points)):
            raise FileNotFoundError("Model files not found in the 'models' directory.")

        # Load the model
        self.net = cv2.dnn.readNetFromCaffe(prototxt, model)
        
        # Load the cluster centers
        pts = np.load(points)
        
        # Add cluster centers as 1x1 convolutions to the network
        class8 = self.net.getLayerId("class8_ab")
        conv8 = self.net.getLayerId("conv8_313_rh")
        pts = pts.transpose().reshape(2, 313, 1, 1)
        self.net.getLayer(class8).blobs = [pts.astype("float32")]
        self.net.getLayer(conv8).blobs = [np.full([1, 313], 2.606, dtype="float32")]

    def colorize(self, l_channel):
        """
        Performs the forward pass to predict AB channels.
        """
        # Resize L channel to 224x224 (required by the model)
        l_resized = cv2.resize(l_channel, (224, 224))
        
        # Subtract 50 for mean centering (specific to this model)
        l_resized -= 50
        
        # Set input and forward pass
        self.net.setInput(cv2.dnn.blobFromImage(l_resized))
        ab_predicted = self.net.forward()[0, :, :, :].transpose((1, 2, 0))
        
        # Resize predicted AB back to match the input L channel size
        ab_predicted = cv2.resize(ab_predicted, (l_channel.shape[1], l_channel.shape[0]))
        
        return ab_predicted
