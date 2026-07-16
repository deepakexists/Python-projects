                # Create student class that takes name & marks of three subject as arguments in constructor.
                # then create the method to print the average.

class student:

    def __init__(self, name, marks1, marks2, marks3):
        self.name = name
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3

    def marks_average(self):
        return (self.marks1+self.marks2+self.marks3) / 2

s1 = student("Deepak", 98, 65, 87)
print(s1.name, s1.marks1, s1.marks2, s1.marks3)    

print(s1.marks_average())
