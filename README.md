# MTailor_Assesment
**Convert PyTorch Model to ONNX format**

- Download the model weights and place them in the project directory
- Make sure the .pth file has the name: pytorch_model_weights.pth
- Run convert_to_onnx.py file
- A file named 'classification_model.onnx' will be saved

**Test the model and image preprocessing**
- Run the test.py script
- If all goes well, this should be the final print statement: 'Model Loading and Prediction Passed.'

**Test the deployed model**
- Make sure to be in the my-first-project directory or whatever your cereberium project directory is
- Run the command: python3 test_server.py
- Enter the image path when prompted
- This will call the api with the image path specified and run inference using the 'run' function in main.py
- The output will be a printed dictionary containing predicted class, and other information.
