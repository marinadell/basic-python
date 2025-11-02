# Letter and vowel counter

# Inform the user about the purpose of this program
purpose = '''
count the characters in a sentence, 
remove the vowels from the sentence
and count how many vowels are in the sentence'''

print(purpose)

vowels = "aeiou"
sentence = "The quick brown fox jumps over the lazy dog"
counter = 0
#add vowel counter
vowel_counter = 0
sentence_length = len(sentence)
print(f"The sentence \"{sentence}\" has {sentence_length} characters")
print(f"The sentence after vowels {vowels} are extracted:")

while counter < sentence_length:
    if sentence[counter] in vowels:
        #if vowel is found, add 1 to the vowel counter
        vowel_counter += 1
        counter += 1
        continue
    print(sentence[counter], end = "")
    counter += 1
print(f"\nThe sentence \"{sentence}\" has {vowel_counter} vowels")