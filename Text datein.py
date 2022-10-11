user_input_name=input("write down your name")
user_input_age=input("write down your age")

file1=open("file.txt", "w")
file1.write("Name:")
file1.write(user_input_name)
file1.write("\n")
file1.write("Age:")
file1.write(user_input_age)

file1=open("file.txt", "r")
txt=file1.read()

print(txt)

file1.close()



