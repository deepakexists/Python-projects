
                                                            # Function

                                       # Average of 3 numbers

def calc_avg(a, b, c):
    sum = a + b + c
    avg = sum/3
    print(avg)
    return(avg)

calc_avg(2, 4, 3)







                                    # WAF to print the length of a list. (list in the parameter)

num = [1, 2, 3, 4, 6]
name = ["Deepak", "Harsh", "tarun", "Aaryan"]

def len_list(list):
    print(len(list))

len_list(num)
len_list(name)





                              # WAF to print the element of a list in a single line. (list is the parameter)

num = [1, 2, 3, 4, 5]
name = ["Deepak", "Harsh", "tarun", "Aaryan"]

def print_list(list):
    for items in list:
        print(items, end=" ")

print_list(num)
print_list(name)



                                      # WAF to find the factorial of n. (n is the parameter)

def print_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)

print_fact(5)
print_fact(5)



             
                                               # WAF to convert USD to INR.

def converter(usd_val):
    inr_val = usd_val * 90
    print(usd_val, "USD = ", inr_val, "INR")

converter(5)    




                                    # WAF to find number is odd or even. (Number has to be given by the user)

def odd_even(n):
    if(n%2 == 0):
     print("EVEN")
    else:
     print("ODD")

odd_even(n = int(input("Enter a number: ")))     
