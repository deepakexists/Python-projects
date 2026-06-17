                               # WAP to input first name and print its length


name = input("Name : ")
print(len(name))

                  

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





                                 # WAP to check if a number is multiple of 7 or not


num = 36

if(num % 7 == 0):
    print("number is multiple of 7")
else:
    print("number is not multiple of 7")






                                 # WAP to find the greatest of 4 number enter by the user


a = int(input("Enter number A : "))
b = int(input("Enter number B : "))
c = int(input("Enter number C : "))
d = int(input("Enter number D : "))

if(a > b):
    if(a > c):
       if(a > d):
            print("Number A is Greater")
    elif(c > d):
            print("Number C is Greater")
elif(b > c):
    if(b > d):
        print("Number B is Greater")
elif(c > d):
    print("Number C is Greater")
else:
    print("Number D is Greater")