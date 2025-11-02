# Assignment 6.2: Grocery list
# Author: Amareya Allen-Dabney
# Date: October 19, 2025
# Purpose: This program is to assist users in creating a grocery list,
#         And assist them with checking things off of their list
#         Also, display the total cost of the grocery list

# Initialize empty lists to store items, prices, and quantities
item_list = []
price_list = []
quantity_list = []

# Welcome message and instructions
print("Welcome to the Grocery List Creator!")
print("Enter your grocery items with their quantities and prices.")
print("Type 'done' when you're finished adding items.\n")

# Loop to collect grocery items from the user
while True:
    # Prompt for item name
    item = input("Enter grocery item name (or 'done' to finish): ")
    
    # Check if user wants to finish
    if item.lower() == 'done':
        break
    
    # Check if item already exists in the list
    if item in item_list:
        print(f"'{item}' already exists in your list. Please enter a different item.\n")
        continue  # Skip to next iteration of the loop
    
    # Prompt for quantity with validation
    while True:
        quantity_input = input(f"Enter quantity for {item}: ")
        
        # Check if input is a valid number (digits only)
        if quantity_input.isdigit():
            quantity = int(quantity_input)
            if quantity < 0:
                print("Error: Quantity cannot be negative. Please try again.")
            else:
                break  # Valid quantity, exit the loop
        else:
            print("Error: Quantity must be a valid number. Please try again.")
    
    # Prompt for unit price with validation
    while True:
        price_input = input(f"Enter unit price for {item}: $")
        
        # Check if input is a valid number (can have one decimal point)
        # Remove one decimal point and check if remaining characters are digits
        if price_input.replace('.', '', 1).isdigit():
            price = float(price_input)
            if price < 0:
                print("Error: Price cannot be negative. Please try again.")
            else:
                break  # Valid price, exit the loop
        else:
            print("Error: Price must be a valid number. Please try again.")
    
    # Add values to respective lists
    item_list.append(item)
    quantity_list.append(quantity)
    price_list.append(price)
    
    print(f"'{item}' added to your list.\n")

print("\n")

# Display header
print(f"{'Item':<20} {'Quantity':<10} {'Price':<10} {'Subtotal':<10}")
print("="*50)

# Initialize grand total
grand_total = 0

# Iterate through the lists using indices
for i in range(len(item_list)):
    item = item_list[i]
    price = price_list[i]
    quantity = quantity_list[i]
    subtotal = quantity * price
    grand_total += subtotal
    # Now display the row in the table
    print(f"{item:<20} {quantity:<10} ${price:<9.2f} ${subtotal:<9.2f}")

# Display grand total
print("="*50)
print(f"{'Grand Total':<41} ${grand_total:.2f}")