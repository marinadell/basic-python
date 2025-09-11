# Program: Calculate the Area of a Triangle

# Display program purpose
print("""
This program will calculate the area of a triangle.
You will be asked to enter the base and height.
""")

# Prompt user for input
base_input = input("Please enter the base of the triangle: ")
height_input = input("Please enter the height of the triangle: ")

# Convert inputs to float
base = float(base_input)
height = float(height_input)

# Calculate the area
area = 0.5 * base * height

# Display the results
print("Base:", base)
print("Height:", height)
print("Area of the triangle:", area)
