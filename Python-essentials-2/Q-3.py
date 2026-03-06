class StudentPerformance:
    def __init__(self, score):
        self.score = score
    
    def score_difference(self):
        try:
            d = self.score[-1] - self.score[0]
            print(f"Difference between last and first score is {d}")
        except:
            print("No scores available to calculate difference")

scores = [55,65,75,85]
s1 = StudentPerformance(scores)
s1.score_difference()

scores = []
s2 = StudentPerformance(scores)
s2.score_difference()