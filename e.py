# Calculate the Hypotenuse of a Triangle
import math

# Inform the user about the purpose of this program
purpose = '''
imports the math module and uses it to calculate the hypotenuse 
(the longest side) of a right triangle. 
The user will provide the base and height of the triangle.'''

print(purpose)

base_input_message = "Please input the base of the triangle:"
base = input(base_input_message)
# convert the string to a float
base = float(base)

height_input = "Please input the height of the triangle:"
height = input(height_input)
# convert the string to a float
height = float(height)

base_square = math.pow(base, 2)
height_square = math.pow(height, 2)

hypo_square = base_square + height_square

hypotenuse = math.sqrt(hypo_square)
print("The hypotenuse of the triangle with base", base , "and height", height, "is: ", hypotenuse)

rounded_hypotenuse = round(hypotenuse, 2)
print("The rounded hypotenuse is: ", rounded_hypotenuse)

string_hypotenuse = str(rounded_hypotenuse)
print("The string hypotenuse is: " + string_hypotenuse)
