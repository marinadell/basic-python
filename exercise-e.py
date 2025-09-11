# Movie quote length program

# Inform the user about the purpose of this program
purpose = '''
This program will ask you to
enter your favorite movie quote
and the person who said it and 
will provide the length of those strings'''

print(purpose)

# ask the user what their favorite quote is 
quote_input = input("What is your favorite movie quote:")
movie_quote = quote_input

# ask the user who said their quote
character_input = input("Who said your favorite quote:")
character = character_input

print("Your favorite movie quote is", movie_quote, "by", character)

quote_length = len(movie_quote)
print("your favorite quote is:", quote_length, "characters long")

