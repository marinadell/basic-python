# Temperature Converter: Fahrenheit to Celsius
# This program takes a temperature in Fahrenheit as input and converts it to Celsius
# using the formula: Celsius = (Fahrenheit - 32) × 5/9

# Display program purpose to the user
welcome_message = '''
Temperature Converter
This program will convert a temperature
from Fahrenheit to Celsius
'''
print(welcome_message)

# Get temperature input from user
input_prompt = "Please enter the temperature in Fahrenheit: "
fahrenheit_str = input(input_prompt)

# Convert input string to float and validate
temperature_fahrenheit = float(fahrenheit_str)

# Echo back the input to confirm
print("Converting", temperature_fahrenheit, "°F to Celsius...")

# Perform temperature conversion
# Formula: Celsius = (Fahrenheit - 32) × 5/9
temperature_celsius = (temperature_fahrenheit - 32) * 5/9

# Round the result to 2 decimal places for better readability
temperature_celsius = round(temperature_celsius, 1)

# Display the conversion result
print(temperature_fahrenheit, "°F is equal to", temperature_celsius, "°C")
