# Gallons to Liters Conversion Program
# Inform the user about the purpose of this program
purpose = '''
This program will ask you to
enter the number of gallons and
will display the number of liters'''

print(purpose)

# Prompt the user to provide the number of liters
user_message = "Please enter the number \
of gallons you want to convert to liters: "
user_input = input(user_message)
user_message = "The number of liters you entered is:"
print(user_message, user_input)

# Convert the string value to float
gallons = float(user_input)

#Store the conversion factor in a variable
CONVERSION_FACTOR = 3.785411784

# Convert liters to gallons using the conversion factor
liters = gallons * CONVERSION_FACTOR

# Display the result to the user
print(gallons, "gallons is equal to", liters, "liters.")
