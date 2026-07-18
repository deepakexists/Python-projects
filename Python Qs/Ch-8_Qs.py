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





                                        # Create account with 2 attributes = balance & account no. 
                                        # create method for debit, credit, print the balance.

 
class account:
    def __init__(self, balance, account_no):
        self.balance = balance
        self.account_no = account_no

    # debit method  
    def debit(self, amount):
        self.balance -= amount
        print("Rs. ", amount, " was debited")
        print("Total Balance = ", self.get_balance())

    # credit method  
    def credit(self, amount):
        self.balance += amount
        print("Rs. ", amount, " was credited")
        print("Total Balance = ", self.get_balance())

    # balance
    def get_balance(self):
        return self.balance


acc1 = account(10000, 12345)
acc1.debit(1000)
acc1.credit(500)







                       # Define a circle class to create a circle with radius r using constructor.
                       # Define an area() method of the class which calculate the area of circle
                       # Define the parimete() method of the which allows you to calculate the perimeter
                       #  of the circle 


class circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        area = 3.14*self.r*self.r
        return area

    def perimeter(self):
        perimeter = 2*3.14*self.r
        return perimeter
    
c1 = circle(3)
print(c1.area()) 
print(c1.perimeter())



