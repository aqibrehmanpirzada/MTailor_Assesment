# ----------------------------For HardCoded Image Path Use this---------------------------------
# import requests
# import json
# import base64

# headers = {
#   'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJwcm9qZWN0SWQiOiJwLWYyZTUyNGZhIiwiaWF0IjoxNzQ4NzE3MjQ1LCJleHAiOjIwNjQyOTMyNDV9.PoQoqYd1fGXLW2e6Nm_qJ8b26L83-05j9FHSqm4-T9IkkY_ESc7SfZm41rZihZSbeTmBxFZK4J6oT9K80PnlB77aha9Ludi3o7sGNh0QZEZnj2phnxpuWVy3jMsFE0VaPsRT9MlvPs7v4royXzR1AXTdxDZdyL55HrF4HqacGjHv-lMHzuFFkLSWJjgN8KJsRfIKqQCgQVpMe2l_tu13kB1R-X8qHHxzerbZWfPjtajeoR1UwkUKlezGGJlCxlgwUboNM5kVX5Ds-qPKyK9r_ujAPVFJjg7Vsl5u4io6qMc1hIn08JGwxPQfiln2BzIpINBdpCiPqOqf0LItLgetyQ',
#   'Content-Type': 'application/json'
# }

# # Endpoint
# api_url = "https://api.cortex.cerebrium.ai/v4/p-f2e524fa/my-first-project/run"

# # Load and encode the image as base64
# image_path = "n01667114_mud_turtle.JPEG"
# with open(image_path, "rb") as image_file:
#     base64_image = base64.b64encode(image_file.read()).decode("utf-8")

# # Prepare the json_payload
# json_payload = {
#     "image": base64_image
# }

# # Send the POST request
# response = requests.post(api_url, json={"json_payload": json_payload}, headers=headers)

# # Print the response
# print("Status Code:", response.status_code)
# print("Response Text:", response.text)
# ---------------------------------------For User Input Use this -------------------------------------------
import requests
import json
import base64

# Your Authorization token (from your Cerebrium dashboard/login)
# Replace with your actual token from the original code or your dashboard
headers = {
  'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJwcm9qZWN0SWQiOiJwLWYyZTUyNGZhIiwiaWF0IjoxNzQ4NzE3MjQ1LCJleHAiOjIwNjQyOTMyNDV9.PoQoqYd1fGXLW2e6Nm_qJ8b26L83-05j9FHSqm4-T9IkkY_ESc7SfZm41rZihZSbeTmBxFZK4J6oT9K80PnlB77aha9Ludi3o7sGNh0QZEZnj2phnxpuWVy3jMsFE0VaPsRT9MlvPs7v4royXzR1AXTdxDZdyL55HrF4HqacGjHv-lMHzuFFkLSWJjgN8KJsRfIKqQCgQVpMe2l_tu13kB1R-X8qHHxzerbZWfPjtajeoR1UwkUKlezGGJlCxlgwUboNM5kVX5Ds-qPKyK9r_ujAPVFJjg7Vsl5u4io6qMc1hIn08JGwxPQfiln2BzIpINBdpCiPqOqf0LItLgetyQ',
  'Content-Type': 'application/json'
}

# Endpoint
api_url = "https://api.cortex.cerebrium.ai/v4/p-f2e524fa/my-first-project/run"

# Load and encode the image as base64
image_path = input('Enter image path: ')
with open(image_path, "rb") as image_file:
    base64_image = base64.b64encode(image_file.read()).decode("utf-8")

# Prepare the json_payload
json_payload = {
    "image": base64_image
}

# Send the POST request
response = requests.post(api_url, json={"json_payload": json_payload}, headers=headers)

# Print the response
print("Status Code:", response.status_code)
print("Response Text:", response.text)
