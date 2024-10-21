# main.py

from fetch_api import fetch_match_data
from data_processing import filter_and_count_match_types
from visualization import plot_match_type_distribution
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Step 1: Fetch data from the API
api_key = os.getenv('API_KEY')
if not api_key:
    print("API key not found. Make sure the .env file is set up correctly.")
    exit(1)

match_data = fetch_match_data()

# Step 2: Filter and count match types for 2024
match_type_count = filter_and_count_match_types(match_data, year='2024')

# Step 3: Visualize the match type distribution
plot_match_type_distribution(match_type_count, year='2024')