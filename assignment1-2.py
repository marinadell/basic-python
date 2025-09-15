#Hours, minutes, and seconds converter
# This program takes a hours, minutes and seconds as input and converts it to seconds

# Display program purpose to the user
welcome_message = '''
Hours, Minutes, and Seconds Converter
This program will convert a time
from hours, minutes, and seconds to seconds
'''
print(welcome_message)

# Get time input from user
hours_input = input("Please enter the number of hours: ")
minutes_input = input("Please enter the number of minutes: ")
seconds_input = input("Please enter the number of seconds: ")

# Convert inputs to float
hours = float(hours_input)
minutes = float(minutes_input)
seconds = float(seconds_input)

# Convert to seconds
total_seconds = (hours * 60 * 60) + (minutes * 60) + seconds

# Display the result
print(hours, "hours,", minutes, "minutes, and", seconds, "seconds is equal to", total_seconds, "seconds")
