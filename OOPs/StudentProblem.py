class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks 

    def average(self):
        return sum(self.marks) / len(self.marks)
    
    def display(self):
        print("Name:", self.name)
        print("Roll No.:", self.roll)
        print("Marks:", self.marks)
        print("Average:", self.average())


marks1 = [85, 90, 78, 88, 92]
student1 = Student("Amit", 101, marks1)
student1.display()

marks2 = [72, 81, 65, 74, 80]
student2 = Student("Priya", 102, marks2)
student2.display()
