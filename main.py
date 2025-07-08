from nutrition_analyzer import NutritionAnalyzer
from activity_tracker import ActivityTracker
from recommender import RecommenderEngine

def main():
    # Simulated input
    food_log = ["Rice", "Dal", "Chicken", "Banana"]
    steps = 6000
    workouts = 3

    print("\n Analyzing your input...")
    
    # Analyze diet
    nutrition = NutritionAnalyzer().analyze(food_log)
    print(f" Nutrition: {nutrition}")

    # Analyze activity
    activity = ActivityTracker().analyze(steps, workouts)
    print(f" Activity: {activity}")

    # Get recommendations
    recommendation = RecommenderEngine().recommend(nutrition, activity)
    print(f"\n Recommendation: {recommendation}")

if __name__ == "__main__":
    main()

