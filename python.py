print("~~~~CALCULATOR~~~~~")

num1 = int(input("Enter first number here: "))
num2 = int(input("Enter second number : "))

print("press 1 for additiomn \npress 2 for subtraction \npress 3 for multiplication \npress 4 for division :")

choice = int(input("enter your choice from 1-4: "))

if choice == 1 :
    print("The addition of given two numbers is ", num1 + num2)
    
elif choice == 2 :
    print("The subtraction of given two numbers is", num1 - num2)

elif choice == 3 :
    print("The multiplication of given two numbers is", num1 * num2)
elif choice == 4 :
    print("The division of given two numbers is", num1 / num2)
else:
    print("Invalid Input")
    