import torch
from pytorch_model import Classifier, BasicBlock
import os


def main(pytorch_weights='pytorch_model_weights.pth', onnx_file_path='classification_model.onnx'):

    weights_loaded = False

    if not os.path.exists(onnx_file_path):
        mtailor = Classifier(BasicBlock, [2, 2, 2, 2])
        try:
            device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
            mtailor.load_state_dict(torch.load(pytorch_weights), map_location=device)
            weights_loaded = True
            print("Model weights loaded successfully!")
        except FileNotFoundError:
            print(f"File Not Found Error: {pytorch_weights} file not found")
        except RuntimeError as e:
            print(f"Runtime Error: Error loading weights: {e}")
        except Exception as e:
            print(f"Unexpected Error: {e}")
        
        if not weights_loaded:
            print("Warning: Cannot export model without proper weights!")
            return None
        
        mtailor.eval()
        dummy_input = torch.randn(1, 3, 224, 224)

        try:
            torch.onnx.export(
                mtailor,
                dummy_input,
                onnx_file_path,
                export_params=True,
                opset_version=11,
                do_constant_folding=True,
                input_names=['input'],
                output_names=['output'],
                dynamic_axes={'input': {0: 'batch_size'}, 'output': {0: 'batch_size'}}
            )
            print(f"Model successfully exported to {onnx_file_path}")
        except Exception as e:
            print(f"Error during ONNX export: {e}")
            return None
            
    else:
        print(f'ONNX model already exists at {onnx_file_path}')

if __name__ == "__main__":
    main()