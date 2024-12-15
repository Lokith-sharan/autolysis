import requests
import json

# API endpoint
url = "http://localhost:8000/run-analysis/"

# Data to be sent in the POST request
data = {
    "file_path": "goodreads.csv"  # Replace with the actual path to your CSV file
}

# Send POST request
try:
    response = requests.post(url, json=data)
    response.raise_for_status()  # Raise an exception for HTTP errors
    
    # Print response JSON from the server
    print("Response from server:")
    print(response.json())
except requests.exceptions.RequestException as e:
    print(f"Error during request: {e}")
