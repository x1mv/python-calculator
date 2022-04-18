from time import sleep
import os 
clear = lambda: os.system('cls')

print("Basic Python Calculator (with output to txt")
print("by: x1mv (just a beginner fun project)")
print("Operators: +  -  /")
input1 = float(input("Enter Number: "))
operator = input("Enter Operator: ")
input2 = float(input("Enter Number: "))
f = open("output.txt", "w")


if operator == "+":
    print("Calculated Output:", input1 + input2)
    f = open("output.txt", "w")
    f.write(str(input1 + input2))
    f.close()
elif operator == "-":
    print("Calculated Output:", input1 + input2)
    f = open("output.txt", "w")
    f.write(str(input1 + input2))
    f.close()
elif operator == "/":
    print("Calculated Output:", input1 + input2)
    f = open("output.txt", "w")
    f.write(str(input1 + input2))
    f.close()
elif operator == "*":
    print("Calculated Output:", input1 + input2)
    f = open("output.txt", "w")
    f.write(str(input1 + input2))
    f.close()
else:
    sleep(1)
    print('Something went wrong here...')
    sleep(1)
    clear()