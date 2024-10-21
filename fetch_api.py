# fetch_api.py

import requests
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

def fetch_match_data():
    # Get the API key and base URL from the environment variables
    api_key = os.getenv('API_KEY')
    base_url = os.getenv('BASE_URL')

    if not api_key or not base_url:
        print("API key or base URL not found. Make sure the .env file is set up correctly.")
        return []

    # Use the base URL and API key to form the complete URL
    url = f'{base_url}?apikey={api_key}&offset=0'
    response = requests.get(url)

    if response.status_code == 200:
        # Parse the JSON response
        match_data = response.json().get('data', [])
        return match_data
    else:
        print("Failed to fetch data from the API.")
        return []
