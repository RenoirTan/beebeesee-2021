import base64
import cv2
import numpy as np

def extract_raw(data):
    data = data.lstrip("data:image/png;base64,")

def image_from_base64(data):
    return base64.b64decode(data)
