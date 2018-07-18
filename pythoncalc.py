# © Pranav Ramesh (Laphatize) 2018-2019
# Please use with credit!

import time

# Initial Loading Prompt
print("© Pranav Ramesh (Laphatize) 2018-2019")
print("Loading...")
time.sleep(3)
print("Welcome to Terminal Calculator!")


# Check if this is users first time.
startup = input("First Time? (y/n): ")
if (startup == "y") :
    print("[PRO TIP] Ensure your numbers are valid and aren't decimals.")
    print("  ")

# Get prompts needed to do computation
operator = input("What is the operation you want to do? (*,/,-,+):  ")
number1 = input("What is the first number?:  ")
number2 = input("What is the second number?:  ")

# Do what the user wanted.
if (operator == "*") : final = str(int(number1)*int(number2))
if (operator == "+") : final = str(int(number1)+int(number2))
if (operator == "-") : final = str(int(number1)-int(number2)) 
if (operator == "/") : final = str(int(number1)/int(number2)) 




# Error handling + display final answer.
try :
    print("  ")
    print("The final answer should be " + final + "!")
    print(" ")
    print("Error with calculation? Make sure you let us know in the github repo: https://github.com/Laphatize/python-calculator/issues")

except : print("I don't think you used valid inputs, please try again!")

 
