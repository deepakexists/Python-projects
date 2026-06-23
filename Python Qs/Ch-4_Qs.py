                                     # Store following word meanings in a python Dictionary :
                                     #  table : "a piece of furniture", "list of facts & figures"
                                     #  cat : "a small animal"

dict = {
    "table" : ("a piece of furniture", "list of facts & figures"),
    "cat" : "a small animal"
}   

print(dict)







                               #     you are given a list of students. Assume one classroom is requred for 1 subject.
                               #     How many classrooms are required for all the students.
                               #         "python", "java", "c++", "python", "javascript", 
                               #          "java", "python", "java", "c++", "c"


subjects = { "python", "java", "c++", "python", "javascript", "java", "python", "java", "c++", "c"}
print(subjects)
print(len(subjects))








                     #     WAP to enter marks of three students from the user and store them in a dictionary. start with an 
                     #      empty dictionary & add one by one. use subject name as key and marks as value.


marks = {}

Maths = int(input("Enter maths marks : "))
marks.update({"Maths" : Maths})

phy = int(input("Enter phy marks : "))
marks.update({"phy" : phy})

chem = int(input("Enter chem marks : "))
marks.update({"chem" : chem})

print(marks)