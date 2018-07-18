
# Super basic calculator program I wrote using python.
# Feel free to use if you'd like.





import time

print("© Pranav Ramesh (Laphatize) 2018-2019")
print("Loading...")
time.sleep(3)
print("Welcome to Terminal Calculator!")



startup = input("First Time? (y/n): ")

if (startup == "y") :
    print("Enure your numbers are valid and aren't decimals.")
    
    print("  ")


operator = input("What is the operation you want to do? (*,/,-,+):  ")
number1 = input("What is the first number?:  ")
number2 = input("What is the second number?:  ")

if (operator == "*") : final = str(int(number1)*int(number2))
if (operator == "+") : final = str(int(number1)+int(number2))
if (operator == "-") : final = str(int(number1)-int(number2)) 
if (operator == "/") : final = str(int(number1)/int(number2)) 





#try :
print("The final answer should be " + final + "!")
print("Error with calculation? Make sure you let us know in the github repo: https://github.com/Laphatize/python-calculator/issues")
# except : print("I don't think you used valid inputs, please try again!")



print("Terminal Calculator application has finished!")
