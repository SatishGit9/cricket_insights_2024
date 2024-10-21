# data_processing.py
from collections import Counter

def filter_and_count_match_types(match_data, year='2024'):
    # count the total matches 
    match_type_count = Counter()  
    for match in match_data:
        match_date = match.get('date', '')
        # Count the matches by type 
        match_type = match.get('matchType', '').lower()  
        if match_date.startswith(year):
            match_type_count[match_type] += 1
    return match_type_count
