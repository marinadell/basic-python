# Assignment 7.1: Grocery list
# Author: Amareya Allen-Dabney
# Date: October 26, 2025
# Purpose: This program is to assist users in creating a grocery list,
#         And assist them with checking things off of their list

# Initialize empty dictionaries to store grocery items
# grocery_items: stores all items with their quantities (pending items)
# picked_items: stores all items that have been picked
# Key: item name, Value: quantity (number)
grocery_items = {}
picked_items = {}

# ===== PHASE 1: Gathering grocery list =====
# Welcome message and instructions for the user
print("Welcome to the Grocery List Creator!")
print("Enter grocery items one at a time.")
print("Type 'done' when you're finished adding items.\n")

# Loop continuously to collect items until user types 'done'
while True:
    # Prompt user to enter an item
    item = input("Enter a grocery item or 'done' to finish: ")
    
    # Check if user wants to finish adding items
    if item.lower() == 'done':
        break  # Exit the loop
    
    # Check if the item already exists in the dictionary to prevent duplicates
    if item in grocery_items:
        print(f"'{item}' already exists in your list with quantity: {grocery_items[item]}.")
        continue  # Skip to next iteration without adding to dictionary
    
    # Prompt user to enter quantity for the item
    while True:
        try:
            quantity = int(input(f"Enter quantity for '{item}': "))
            if quantity <= 0:
                print("Quantity must be greater than 0. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    # Add the new item to the dictionary with its quantity
    grocery_items[item] = quantity
    print(f"'{item}' (quantity: {quantity}) added to your list.")

# Display the complete grocery list with numbered items
print("\n--- Your Grocery List ---")
for i, (item, quantity) in enumerate(grocery_items.items(), 1):
    print(f"{i}. {item} - Quantity: {quantity}")

# ===== PHASE 2: Picking items in the store =====
# Instructions for checking off items
print("\n--- Now let's check off items as you pick them! ---")
print("Enter items as you pick them or 'done' to finish.\n")

# Loop while there are still items remaining
while grocery_items:
    # Prompt user to enter an item they picked
    item = input("Enter an item you picked or 'done' to finish: ")
    
    # Check if user wants to finish picking items
    if item.lower() == 'done':
        break  # Exit the loop
    
    # Check if the item is in the grocery list
    if item in grocery_items:
        # Prompt user for quantity being picked
        while True:
            try:
                quantity_picked = int(input(f"Enter quantity of '{item}' being picked: "))
                if quantity_picked <= 0:
                    print("Quantity must be greater than 0. Please try again.")
                    continue
                if quantity_picked > grocery_items[item]:
                    print(f"Only {grocery_items[item]} {item} available. Please try again.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        
        # Add to picked_items dictionary
        if item in picked_items:
            picked_items[item] += quantity_picked
        else:
            picked_items[item] = quantity_picked
        
        # Reduce quantity from grocery_items
        grocery_items[item] -= quantity_picked
        print(f"'{item}' - Picked: {quantity_picked}, Remaining: {grocery_items[item]}")
        
        # If quantity reaches 0, remove the item from grocery_items
        # Check if item exists in dictionary before attempting to delete
        if item in grocery_items and grocery_items[item] == 0:
            del grocery_items[item]
            print(f"'{item}' completed and removed from your list.")
    else:
        # Item not found in the list
        print(f"'{item}' is not in your list.")

# Display all picked items
print("\n--- Items You Picked ---")
if picked_items:
    for i, (item, quantity) in enumerate(picked_items.items(), 1):
        print(f"{i}. {item} - Quantity: {quantity}")
else:
    print("No items have been picked yet.")

# Display remaining items (if any)
if grocery_items:
    print("\n--- Remaining Items ---")
    for i, (item, quantity) in enumerate(grocery_items.items(), 1):
        print(f"{i}. {item} - Quantity: {quantity}")
