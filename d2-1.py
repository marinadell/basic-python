# Liters to Gallons Conversion Program
# Inform the user about the purpose of this program
purpose = '''
This program will ask you to
enter the number of liters and
will display the number of gallons'''

print(purpose)

# Prompt the user to provide the number of liters
user_message = "Please enter the number \
of liters you want to convert to gallons: "
user_input = input(user_message)
user_message = "The number of liters you entered is:"
print(user_message, user_input)

# Convert the string value to float
liters = float(user_input)

#Store the conversion factor in a variable
CONVERSION_FACTOR = 0.264172052

# Convert liters to gallons using the conversion factor
gallons = liters * CONVERSION_FACTOR

rounded_gallons = round(gallons, 2)

# Display the result to the user
print(liters, "liters is equal to", gallons, "gallons.")
print(liters, "liters is equal to", rounded_gallons, "gallons rounded.")