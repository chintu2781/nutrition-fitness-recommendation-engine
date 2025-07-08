from sklearn.cluster import KMeans
import numpy as np

class RecommenderEngine:
    def __init__(self):
        # Sample training data: [calories, protein, steps, workouts]
        self.model = KMeans(n_clusters=3, random_state=42)
        self.train()

    def train(self):
        X = np.array([
            [1800, 60, 10000, 4],
            [2500, 80, 3000, 1],
            [2200, 70, 7000, 2],
            [1500, 50, 12000, 6],
        ])
        self.model.fit(X)

    def recommend(self, nutrition_data, activity_data):
        x = [nutrition_data['calories'], nutrition_data['protein'],
             activity_data['steps'], activity_data['workouts']]
        cluster = self.model.predict([x])[0]

        if cluster == 0:
            return "Focus on moderate carbs and increase strength training."
        elif cluster == 1:
            return "Cut calories slightly and walk more."
        else:
            return "Maintain current diet and continue active lifestyle."

