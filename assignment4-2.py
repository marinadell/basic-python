# Assignment 4.2:
# Author: Amareya Allen-Dabney
# Date: October 5, 2025
# Purpose: This program calculates either compound interest or simple interest for a user

# Import the math module
import math

# Display program description to the user
purpose = '''
This program calculates the compound amount at the end of
the investment period or the simple interest'''

print(purpose)

# Allow the user to choose simple interest savings or compound interest investment
print("Would you like to calculate Simple interest saving or Compound interest investment:")
print("1. Simple interest saving")
print("2. Compound interest investment")

choice = input("Enter your choice (1 or 2): ")
choice = float(choice)

# Ask the user to provide the principal amount (P)
principal_message = "Please provide the principal amount to be invested: "
user_input_principal = input(principal_message)
# Store this in a variable with an appropriate name
principal = float(user_input_principal)
# Ask the user to provide the annual interest rate (r)
interest_message = "Please provide the annual interest rate as a percentage: "
user_input_interest = input(interest_message)
interest_percentage = float(user_input_interest)
#convert interest to a decimal
interest_decimal = interest_percentage / 100
# Ask the user to provide the number of years the investment is being made (t)
years_message = "Please provide the number of years the investment is being made: "
user_input_years = input(years_message)
years = float(user_input_years)

if choice == 1:
    rate_time = interest_decimal * years
    one_rt = 1 + rate_time
    accrued_amount = principal * one_rt

    accrued_amount = round(accrued_amount, 2)

    #display the results
    print("\n+-----------------------------+----------------+")
    print("|          Description         |      Value     ")
    print("+------------------------------+----------------+")
    print(f"| Principal Amount             | ${principal}")
    print(f"| Interest Rate (%)            |  {interest_percentage} %")
    print(f"| Investment Duration (Years)  |  {years}")
    print(f"| Accrued amount               | ${accrued_amount}")
    print("+------------------------------+----------------+")

elif choice == 2: 
    # only for compound
    # Ask the user to provide the number of times per year the interest is compounded (n)
    months_message = "Please provide the number of months per year interest is compounded: "
    user_input_months = input(months_message)
    months = float(user_input_months)

    # A = P(1+r/n)^nt
    interest_earned = interest_decimal / months
    compound_interest = 1 + interest_earned
    total_months = months * years
    compound_amount = principal * math.pow(compound_interest, total_months)

    # Use round() to display the results with 2 decimal places
    principal = round(principal, 2)
    interest_percentage = round(interest_percentage, 2)
    months = round(months, 2)
    years = round(years, 2)
    compound_amount = round(compound_amount, 2)


    #display the results
    print("\n+-----------------------------+----------------+")
    print("|          Description         |      Value     ")
    print("+------------------------------+----------------+")
    print(f"| Principal Amount             | ${principal}")
    print(f"| Interest Rate (%)            |  {interest_percentage} %")
    print(f"| Times Compounded Per Year    |  {months}")
    print(f"| Investment Duration (Years)  |  {years}")
    print(f"| Compound Amount              | ${compound_amount}")
    print("+------------------------------+----------------+")
else:
    print("You did not provide 1 of the 2 choices, try again")