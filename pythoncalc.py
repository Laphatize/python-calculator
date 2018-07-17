
# Super basic calculator program I wrote using python.
# Feel free to use if you'd like.





import time

print("© Pranav Ramesh (Laphatize) 2018-2019")
print("Loading...")
time.sleep(3)
print("Welcome to Terminal Calculator!")



name = input("What's your name?: ")
print("Alrighty, " + name + ". Let's get started.")

operator = input("What is the operation you want to do? (*,/,-,+):  ")
number1 = input("What is the first number?:  ")
number2 = input("What is the second number?:  ")

if (operator == "*") : final = (int(number1)*int(number2))
if (operator == "+") : final = (int(number1)+int(number2))
if (operator == "-") : final = (int(number1)-int(number2)) 
if (operator == "/") : final = (int(number1)/int(number2)) 




try : print("The final answer should be" + final)
except : print("I don't think you used valid inputs, please try again!")



print("Terminal Calculator application has finished!")
