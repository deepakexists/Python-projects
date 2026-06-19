                          # WAP to ask user to enter a names of their 3 favorite movies & store them in list


movies = []
mov = input("Enter movie name 1 : ")
movies.append(mov)
mov = input("Enter movie name 2 : ")
movies.append(mov)
mov = input("Enter movie name 3 : ")
movies.append(mov)

print(movies)






                      # WAP to check if a list contains of palindrome of elements. (Hint: use copy() method)

list = [1, 2, 2, 1]
print(list)

copy_list = list.copy()
copy_list.reverse()
print(copy_list)

if(copy_list == list):
    print("Its a palindrome")
else:
    print("not palidrome")




                        # WAP to count the number of student with the "A" grade in the following tuple.

grade = ("C", "D", "A", "A", "B", "B", "A")
count = grade.count("A")
print(count)

