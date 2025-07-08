class ActivityTracker:
    def analyze(self, steps, workouts_per_week):
        if steps > 10000:
            level = "Active"
        elif steps > 5000:
            level = "Moderately Active"
        else:
            level = "Sedentary"
        return {"steps": steps, "workouts": workouts_per_week, "level": level}
