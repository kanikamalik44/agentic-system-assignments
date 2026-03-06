class StudentScores:
    def __init__(self, value):
        self.value = value
    
    def highest_last_two(self):
        try:
            if (self.value[-1] > self.value[-2]):
                print(f"Highest score among last two is: {self.value[-1]}")
            else:
                print(f"Highest score among last two is: {self.value[-2]}")
        except:
            print("Not enough scores to find highest value")

scores = [45,67,89,72]
s1 = StudentScores(scores)
s1.highest_last_two()

scores = []
s2 = StudentScores(scores)
s2.highest_last_two()