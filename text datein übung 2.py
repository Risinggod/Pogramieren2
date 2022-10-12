user_input=input("write down a nommber")
user_input=float(user_input)
count=1
counter1=open("counter1.txt", "w")
while count<=user_input:
    counter1.write(str(count))
    counter1.write("\n")
    count+=1

counter1=open("counter1.txt", "r")
txt=counter1.read()
print(txt)
counter1.close()








