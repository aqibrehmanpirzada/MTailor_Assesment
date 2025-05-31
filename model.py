import torch
from torchvision import transforms

import onnx
import onnxruntime as ort
import numpy as np

from PIL import Image


class ONNXModel:
    def __init__(self, model_path='classification_model.onnx'):

        self.model_path = model_path
        self.input_name = None
        self.output_name = None
        self.session = None
        self.load_model()


    def load_model(self):

        self.model = onnx.load(self.model_path)

        try:
            onnx.checker.check_model(self.model)
            print("Model validation passed - model is valid!")
        except onnx.checker.ValidationError as e:
            print(f"Model validation failed: {e}")

        # Create inference session
        self.session = ort.InferenceSession(self.model_path)
        self.input_name = self.session.get_inputs()[0].name
        self.output_name = self.session.get_outputs()[0].name
        
        print(f"Model loaded: {self.model_path}")
        # print(f"Input: {self.input_name}, Shape: {self.session.get_inputs()[0].shape}")

    
    def predict(self, input_data):

        # Make sure data is a numpy array
        if isinstance(input_data, torch.Tensor):
            input_data = input_data.numpy()
        
        input_data = np.array(input_data, dtype=np.float32)
        
        # Run inference
        outputs = self.session.run([self.output_name], {self.input_name: input_data})

        logits = torch.from_numpy(outputs[0]) # Convert it to a PyTorch tensor

        # Now, this line should work correctly:
        _, class_prediction = torch.max(logits, dim=1)
        class_prediction = class_prediction.item() # convert to a python integer

        print(f'Class ID of given image is: {class_prediction}')
        return class_prediction


class PreProcessImage:
    def __init__(self, resize_dims=(224, 224)):
        self.transform = transforms.Compose([
            transforms.Resize(resize_dims, interpolation=Image.Resampling.BILINEAR),
            transforms.ToTensor(),  # Divides by 255 and reshapes Image from (H, W, C) to (C, H, W)
            transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                 std=[0.229, 0.224, 0.225])
        ])

    def __call__(self, image_path):
        image = Image.open(image_path).convert('RGB')  # Ensure RGB format
        transformed_image = self.transform(image)
        if len(transformed_image.size()) == 3:
            transformed_image = transformed_image.unsqueeze(0) # Convert tensor shape from [num_channels, H, W] to [batch_size, num_channels, H, W]
        return transformed_image
    

if __name__=='__main__':

    preprocessor = PreProcessImage()
    processed_tensor = preprocessor('n01667114_mud_turtle.JPEG')

    predictor = ONNXModel(model_path='classification_model.onnx')

    class_prediction = predictor.predict(processed_tensor)