import argparse
import base64
import json
import requests

CEREBRIUM_URL = "https://api.cortex.cerebrium.ai/v4/p-84e93a14/mtailor-mlops-assessment/run"
HEADERS = {
    'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJwcm9qZWN0SWQiOiJwLTg0ZTkzYTE0IiwiaWF0IjoxNzQ4NzE3ODEzLCJleHAiOjIwNjQyOTM4MTN9.TQyW8fqrYpvyXm8aqRja50LjVpOys5tPFChmnQ0pjbKyC0M0MViMK2VdzIgRZIRgUmrV0sh0TAO0WWkCq8mTNzU_VuVEQ0xhco6xida7wHROT1ryKU8x6xWXpVtYZwvXDr7QyLLDcNd1tOP4hzHJB90Pc1NNQhZsEf8XyjXqC__Exlp5U3gWa4JdeWXwr0Q36rnyLRQL55U2oS4ErmLawi-jk9ciZtjH6LFbi0xQxwUEBgwnQKQFxVyUm3UFl-atDiRl4G4xRoLWmhkK57upRu9VtsM1zweRqBUPmEFlhnQoulBK6_c6xMn0LgoSDPuIJCBEf5aoY0ibA8vGit2c3g',
    'Content-Type': 'application/json'
}

def encode_image_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')

def predict(image_path):
    image_b64 = encode_image_to_base64(image_path)
    payload = json.dumps({
    "param_1": "classify_image",  # just a label or action name
    "param_2": image_b64          # base64-encoded image
})



    response = requests.post(CEREBRIUM_URL, headers=HEADERS, data=payload)

    if response.ok:
        print("Prediction result:", response.json())
    else:
        print("Failed to get prediction:", response.status_code, response.text)

def run_custom_tests():
    print("Running custom test cases on deployed Cerebrium endpoint...")
    sample_images = [
        "n01440764_tench.jpeg",
        "n01667114_mud_turtle.JPEG"
    ]
    for img in sample_images:
        print(f"Testing with image: {img}")
        predict(img)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Test deployed ONNX model on Cerebrium.")
    parser.add_argument("--image", type=str, help="Path to the image for prediction")
    parser.add_argument("--test", action="store_true", help="Run predefined test suite")

    args = parser.parse_args()

    if args.test:
        run_custom_tests()
    elif args.image:
        predict(args.image)
    else:
        print("Please provide an image path or use the --test flag.")
