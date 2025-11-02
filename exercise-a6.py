# Create a list of four or five musical instruments of your choice.
instruments = ["Guitar", "Piano", "Bass", "Drums", "Saxophone"]
print(instruments)
# Show how you can add another musical instrument to this list.
instruments.append("Harmonica")
print(f"Instruments with Harmonica added to the list: {instruments}")
# Show how you can modify one of the musical instruments in this list.
instruments[1] = "Keyboard"
print(f"Instruments with changing piano to keyboard: {instruments}")
# Show how you can remove one of the musical instruments from this list.
instruments.remove("Drums")
print("After removing 'Drums':", instruments)
# Show how you can access a particular element/member of this list.
third_instrument = instruments[2]
print("The 3rd instrument in the list is:", third_instrument)
# Using the len() function, show the number of elements of this list.
list_length = len(instruments)
print("The number of instruments in the list is:", list_length)
# Using the len() function, access the last member of this list since the len() function will tell you how many members/elements this list has.
last_instrument = instruments[list_length - 1]
print("The last instrument in the list is:", last_instrument)