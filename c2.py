# Area and perimeter of geometric shape calculator 
# This programs allows a user to select a shape (Triangle, circle, square or rectangle)
# enter it's measurements 
# It will then calculate the area and perimeter of that shape

import math

purpose = '''
This program is to calculate the area of different shapes '''
print(purpose)

# Allow the user to choose shape
# assigning specific shapes because program can only handle theses shapes
print("Choose a shape:")
print("1. Triangle")
print("2. Circle")
print("3. Square")
print("4. Rectangle")

choice = input("Enter your choice (1-4): ")
shape_choice = float(choice)

# print statement to confirm what is happening
print(f"shape choice: {shape_choice}")

if shape_choice == 1:
    print(f"You chose {shape_choice}: Triangle, please provide the measurements for the 3 sides")
    side_a = float(input("enter side a:"))
    side_b = float(input("enter side b:"))
    side_c = float(input("enter side c:"))

    semi_perimeter = (side_a + side_b + side_c) / 2
    a = semi_perimeter - side_a
    b = semi_perimeter - side_b
    c = semi_perimeter - side_c

    triangle_area = math.sqrt(semi_perimeter * a * b * c)
    triangle_perimeter = side_a + side_b + side_c

    print(f"Triangle Area is {round(triangle_area, 2)}")
    print(f"Triangle Perimeter is {round(triangle_perimeter, 2)}")

elif shape_choice == 2:
    print(f"You chose {shape_choice}: Circle, please provide the radius")
    radius = float(input("Enter radius: "))

    circle_area = math.pi * math.pow(radius, 2)
    circle_perimeter = 2 * math.pi * radius

    print(f"Circle Area is {round(circle_area, 2)}")
    print(f"Circle Perimeter is {round(circle_perimeter, 2)}")

elif shape_choice == 3 or shape_choice == 4:
    if shape_choice == 3:
        shape = "Square"
        print(f"You chose {shape_choice}: Square, please provide the width and length (this should be the same number twice)")
    elif shape_choice == 4:
        shape = "Rectangle"
        print(f"You chose {shape_choice}: Rectangle, please provide the width and length")
    
    width = float(input("enter the height:"))
    length = float(input("enter the length:"))

    area = length * width
    perimeter = 2 * (length + width)

    print(f"{shape} Area is {round(area, 2)}")
    print(f"{shape} Perimeter is {round(perimeter, 2)}")
else:
    print(f"Sorry you entered {shape_choice}, and we currently do not have a shape for that number, try 1-4")


