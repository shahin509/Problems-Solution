import cv2
import numpy as np
from PIL import Image

def compare_images(original_path, signature_path):
    # load the images
    original = cv2.imread(original_path, cv2.IMREAD_GRAYSCALE)
    signature = cv2.imread(signature_path, cv2.IMREAD_GRAYSCALE)

    # Resize 
    original = cv2.resize(original, (500, 500))
    signature = cv2.resize(signature, (500, 500))

    # structural Similarity Index (SSI)
    from skimage.metrics import structural_similarity as ssim

    score, _ = ssim(original, signature, full=True)
    return score
