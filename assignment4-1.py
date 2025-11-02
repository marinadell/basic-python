# Assignment 4.1:
# Author: Amareya Allen-Dabney
# Date: October 5, 2025
# Purpose: This program is a calculator simulator that performs basic arithmetic operations
#         and square root calculations based on user input.

# Import math library for advanced mathematical operations like square root
import math
# purpose of the program
purpose = '''
This program simulates a calculator
it will ask the user what operation they would like to perform then 
prompt the user to enter 2 integers one by one.
Perform the calculation and display the results.'''

print(purpose)

# Provide operation choices
print("Select the operation you want to perform:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. Exponentiation (^)")
print("6. Square Root (√)\n")

operation_choice = input("Enter the number corresponding to your choice (1-6): ")

# Validate if the user input is a numeric digit
if operation_choice.isdigit():
    # Handle square root operation separately as it only requires one input number
    # Check if user selected square root (option 6)
    if operation_choice == "6":
        num = input("Enter a number to find its square root: ")
        # confirm entry is a digit
        if num.isdigit():
            # convert to float
            num = float(num)
            # confirm the number is greater than 0 since you can;t have a square root of a negative number
            if num < 0:
                print("Error: Cannot calculate the square root of a negative number.")
            else:
                result = math.sqrt(num)
                print(f"The square root of {num} is {round(result, 2)}")
    # Handle all other operations that require two numbers (addition, subtraction, multiplication, division, exponentiation)
    elif operation_choice in ["1", "2", "3", "4", "5"]:
        # Get both numbers from user input
        num1 = input("Enter the first number: ")
        num2 = input("Enter the second number: ")

        # Validate that both inputs are numeric digits
        if num1.isdigit() and num2.isdigit():
            # Convert string inputs to floating point numbers for calculations
            num1 = float(num1)
            num2 = float(num2)
            # Perform addition if user selected option 1
            if operation_choice == "1":
                result = num1 + num2
                print(f"The result of addition is: {round(result, 2)}")
            # Perform subtraction if user selected option 2
            elif operation_choice == "2":
                result = num1 - num2
                print(f"The result of subtraction is: {round(result, 2)}")
            # Perform multiplication if user selected option 3
            elif operation_choice == "3":
                result = num1 * num2
                print(f"The result of multiplication is: {round(result, 2)}")
            # Perform division if user selected option 4
            elif operation_choice == "4":
                # Check for division by zero error
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                else:
                    result = num1 / num2
                    print(f"The result of division is: {round(result, 2)}")
            # Perform exponentiation if user selected option 5
            elif operation_choice == "5":
                result = num1 ** num2
                print(f"The result of exponentiation is: {round(result, 2)}")
            else:
                print("Invalid selection! Please restart the program and choose a valid operation (1-6).")
        # Handle case where one or both inputs are not valid numbers
        else:
            print(f"Either the first number {num1} or the second number {num2} are not digits, please enter an actual digit")
# Handle case where the initial operation choice is not a valid number
else:
    print("You did not provide a valid a operation choice, restart the program and choose a digit 1-6")