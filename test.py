import os
import numpy as np
from model import PreProcessImage, ONNXModel

def test_image_preprocessing(test_image):
    print("Testing Image Preprocessing...")
    preprocessor = PreProcessImage()
    assert os.path.exists(test_image), "Test image not found."
    processed = preprocessor(test_image)
    assert processed.shape == (1, 3, 224, 224), f"Unexpected shape: {processed.shape}"
    print("Preprocessing Passed.")
    return processed

def test_model_loading_and_prediction(model_path, input):
    print("Testing ONNX Model Loading & Prediction...")
    model = ONNXModel(model_path)
    output = model.predict(input)
    assert isinstance(output, int), "Prediction output should be an integer which is the class number."
    print("Model Loading and Prediction Passed.")

if __name__ == "__main__":
    processed_image = test_image_preprocessing(test_image='n01667114_mud_turtle.JPEG')
    test_model_loading_and_prediction(model_path='classification_model.onnx', input=processed_image)
