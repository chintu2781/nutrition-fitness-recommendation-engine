
import json
import os

def load_sample_input(file_path="data/sample_input.json"):
    """
    Loads sample user data (diet and activity) from a JSON file.
    Returns a dictionary with 'food_log', 'steps', 'workouts'.
    """
    if not os.path.exists(file_path):
        print(f" Input file not found at: {file_path}")
        return {}

    with open(file_path, 'r') as file:
        try:
            data = json.load(file)
            return data
        except json.JSONDecodeError:
            print("Failed to parse JSON.")
            return {}

def pretty_print_dict(data, title="Data"):
    
    print(f"\n {title}:")
    for key, value in data.items():
        print(f"  {key}: {value}")

def normalize_food_item(item):
    """
    Standardizes food item input (e.g., '  Rice ' → 'rice')
    """
    return item.strip().lower()

