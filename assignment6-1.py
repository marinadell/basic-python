# Assignment 6.1: Grocery list
# Author: Amareya Allen-Dabney
# Date: October 19, 2025
# Purpose: This program is to assist users in creating a grocery list,
#         And assist them with checking things off of their list

# Initialize empty lists to store grocery items
# item_list: stores all the items the user wants to buy
# picked_items: stores items the user has already picked up
item_list = []
picked_items = []

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
    
    # Check if the item already exists in the list to prevent duplicates
    if item in item_list:
        print(f"'{item}' already exists in your list.")
    else:
        # Add the new item to the list
        item_list.append(item)
        print(f"'{item}' added to your list.")

# Display the complete grocery list with numbered items
print("\n--- Your Grocery List ---")
for i, item in enumerate(item_list, 1):
    print(f"{i}. {item}")

# ===== PHASE 2: Picking items in the store =====
# Instructions for checking off items
print("\n--- Now let's check off items as you pick them! ---")
print("Enter items as you pick them or 'done' to finish.\n")

# Loop while there are still items in the grocery list
while item_list:
    # Prompt user to enter an item they picked
    item = input("Enter an item you picked or 'done' to finish: ")
    
    # Check if user wants to finish picking items
    if item.lower() == 'done':
        break  # Exit the loop
    
    # Check if the item is in the grocery list
    if item in item_list:
        # Remove item from grocery list and add to picked items
        item_list.remove(item)
        picked_items.append(item)
        print(f"'{item}' removed from your list.")
    else:
        # Item not found in the list
        print(f"'{item}' is not in your list.")

# Display all the items the user has picked
print("\n--- Items You Picked ---")
for i, item in enumerate(picked_items, 1):
    print(f"{i}. {item}")
