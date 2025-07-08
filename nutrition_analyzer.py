import numpy as np

class NutritionAnalyzer:
    def __init__(self):
        self.food_db = {
            "rice": {"calories": 130, "protein": 2.7},
            "chicken": {"calories": 239, "protein": 27},
            "banana": {"calories": 89, "protein": 1.1},
            "dal": {"calories": 104, "protein": 7},
        }

    def analyze(self, food_log):
        total = {"calories": 0, "protein": 0}
        for item in food_log:
            data = self.food_db.get(item.lower())
            if data:
                total["calories"] += data["calories"]
                total["protein"] += data["protein"]
        return total

