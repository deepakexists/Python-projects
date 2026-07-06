
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

