                              #    create a new file "practice.txt" using python. Add the following data in it:
                              #                        Hi everyone
                              #                        We are learning file I/o
                              #                        using Java
                              #                        I like programing in Java


with open("practice.txt", "w") as f:
    f.write("Hi everyone \n")
    f.write("We are learning file I/O \n")
    f.write("using Java \n")
    f.write("I like programing in Java")







                                  #   WAF that all the occurrences of "java" with "python" in above file.

def replace_word():
 with open("practice.txt", "r") as f:
    data = f.read()

 new_data = data.replace("Java", "python")
 print(new_data)    

 with open("practice.txt", "w") as f:
    f.write(new_data)

replace_word()
