# visualization.py
import matplotlib.pyplot as plt

def plot_match_type_distribution(match_type_count, year='2024'):
    if match_type_count:
        plt.figure(figsize=(8, 6))
        plt.pie(match_type_count.values(), labels=match_type_count.keys(), autopct='%1.1f%%', startangle=140)
        plt.title(f"Match Type Distribution in {year}")
        plt.show()
    else:
        print(f"No match data available for {year}.")
