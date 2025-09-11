# Simple Python program with some errors

# What is the error here?
# added in trailing double quote
name = input("Enter your name")

# What is the error here?
# fixed indentation
age = input("Enter your age: ")

# What is the error here?)
# added in second parenthesis
print ("Hello, " + name + ". You are " + age + " years old.")

# What is the error here?
# updated trailing double quote (") to single quote (')
favorite_color = input('Enter your favorite color: ')

# What is the error here? 
# semantics error, asking for height but using favorite color variable
print("Your favorite color is", favorite_color)

# What is the error here?
# no variable turquoise to reassign here, changed turquoise to a string
my_favorite_color = "turquoise"
print("My favorite color is", my_favorite_color)

# What is the error here?
# no varaible height so created one, that is an input
height = input("What is your height?")
print("Your height is", height)
