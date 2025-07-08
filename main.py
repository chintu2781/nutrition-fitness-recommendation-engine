# main.py

from nutrition_analyzer import NutritionAnalyzer
from activity_tracker import ActivityTracker
from recommender import RecommenderEngine
from utils import load_sample_input, pretty_print_dict

def main():
    # Step 1: Load sample user data
    input_data = load_sample_input()

    if not input_data:
        print(" No input data found. Please check sample_input.json")
        return

    food_log = input_data.get("food_log", [])
    steps = input_data.get("steps", 0)
    workouts = input_data.get("workouts", 0)

    print("\n Analyzing your lifestyle input...")

    # Step 2: Nutrition Analysis
    nutrition = NutritionAnalyzer().analyze(food_log)
    pretty_print_dict(nutrition, "Nutrition Summary")

    # Step 3: Activity Analysis
    activity = ActivityTracker().analyze(steps, workouts)
    pretty_print_dict(activity, "Activity Summary")

    # Step 4: Personalized Recommendation
    recommendation = RecommenderEngine().recommend(nutrition, activity)
    print(f"\n Final Recommendation:\n {recommendation}")

if __name__ == "__main__":
    main()
