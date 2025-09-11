# Kilometers to Miles Conversion Program
# Inform the user about the purpose of this program
purpose = '''
This program will ask you to
enter the number of kilometers and
will display the number of miles'''

print(purpose)

# Prompt the user to provide the number of liters
user_message = "Please enter the number \
of kilometers you want to convert to miles: "
user_input = input(user_message)
user_message = "The number of kilometers you entered is:"
print(user_message, user_input)

# Convert the string value to float
kilometers = float(user_input)

#Store the conversion factor in a variable
CONVERSION_FACTOR = 0.62137119224

# Convert liters to gallons using the conversion factor
miles = kilometers * CONVERSION_FACTOR

# Display the result to the user
print(kilometers, "kilometers is equal to", miles, "miles.")
