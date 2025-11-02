# Assignment 3.1: Sphere Calculator
# Author: Amareya Allen-Dabney
# Date: September 28, 2025
# Purpose: This program calculates the surface area and volume of a sphere,
#          as well as the ratio between volume and surface area.
# Documentation: https://docs.python.org/3/library/math.html

# Import the math module
import math

# Display program description to the user
purpose = '''
This program calculates the surface area and volume of a sphere.
and the ratio of volume to surface area.'''

print(purpose)

# Mathematical formulas used in this program:
# Surface area of a sphere = 4 * pi * radius^2
# Volume of a sphere = (4 * pi * radius^3) /3
# Ratio of volume to surface area = Volume / Surface area

# Get user input for sphere radius
radius_message = "Please enter the radius of the sphere: "
user_radius_input = input(radius_message)

# Convert the string value to float
radius = float(user_radius_input)

# Get the value of pi from the math module
pi = math.pi

# Calculate surface area using the formula: 4πr²
surface_area = 4 * pi * math.pow(radius, 2)
# Calculate volume using the formula: (4/3)πr³
volume = (4 * pi * math.pow(radius, 3)) /3
# Calculate the ratio of volume to surface area
ratio = volume / surface_area

# Round the results to 2 decimal places for better readability
surface_area = round(surface_area, 2)
volume = round(volume, 2)
# Round ratio to nearest integer since it's a relative measure
ratio = round(ratio)

# Convert numerical values to strings for output formatting
radius = str(radius)
surface_area = str(surface_area)
volume = str(volume)
ratio = str(ratio)

# Display the results in a formatted output
print("-------------ANSWER-------------------")
print(f"The radius of the sphere is: {radius}")
print(f"The surface area of the sphere is: {surface_area}")
print(f"The volume of the sphere is: {volume}")
print(f"The ratio of volume to surface area is: {ratio}")
