                                       #  print number from 1 to 100

num = 1
while num <= 100:   # Stoping condition
    print(num)
    num+=1




                                           #  print number from 100 to 1
num = 100
while num >= 1:
    print(num)
    num-=1




                                      #  print the multiplation table of a number n
i = int(input(("Enter which table you want : ")))
n = 1
while n <= 10:
    print(n*i)
    n +=1





                                # Print the elements of the following list using loop:
                                # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# traverse
idx = 0
while idx < len(list):
    print(list[idx])
    idx += 1


# i = 1
# while i <= 10:
#     print(i**2)
#     i += 1



                             # Search for the number X in the tuple using loop:
                             # (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = 36

i = 0
while i < len(tup):
    if(tup[i] == x):
        print("Found at idx", i)
        break 
    i += 1



                                                               # Loops Qs


#                             # print the element of the following list using a loop:
#                             # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

for num in list:
    print(num)