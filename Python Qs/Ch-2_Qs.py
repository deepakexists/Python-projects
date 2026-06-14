
                        # WAP to check if a number enter by the user is odd or even.


num = int(input("Enter a number : "))

if(num%2 == 0):
    print("even")
else:
    print("odd")




                    # WAP to find the greatest of 3 number enter by the user



a = int(input("Enter number A : "))
b = int(input("Enter number B : "))
c = int(input("Enter number C : "))

if(a > b):
    if(a > c):
        print("Number A is Greater")
elif(c > b):
    print("Number C is Greater")
else:
    print("Number B is Greater")

