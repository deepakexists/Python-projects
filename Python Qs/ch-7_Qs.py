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







                                    # Search if the word "learning" exists in the file or not

def check_for_word(word):
    #word = "learning"
    with open("practice.txt", "r") as f:
        data = f.read()
    if(data.find(word) != -1):
        print("FOUND")
    else:
        print("Not found")

check_for_word("learning")






                                    # WAF to find in which line of the file dose the word "learning" occur first
                                    # print -1 if word not found

def check_for_line():
    word = "learning"
    data = True
    line_no = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1

    return -1

check_for_line()


