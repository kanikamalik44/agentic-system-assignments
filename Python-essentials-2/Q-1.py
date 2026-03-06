class StudentMarks:
    def __init__(self, marks):
        self.marks = marks
    
    def last_three_avg(self):
        try:
            avg = (self.marks[-1] + self.marks[-2] +self.marks[-3]) / 3
            print(f"Average of last 3 marks is : {avg}")
            return avg
        except:
            print("Not enough marks to calculate average")

marks = [50,60,70,80,90]
s1 = StudentMarks(marks)
s1.last_three_avg()

marks = []
s2 = StudentMarks(marks)
s2.last_three_avg()