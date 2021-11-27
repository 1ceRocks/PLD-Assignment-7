# Create a program that ask for a sentence as input.
# Display the number of words, vowels and consonants in the input 
# ex. input: Bahala kayo dyan
# output
# words: 3
# vowels: 6
# consonants: 8

sentence = input("\nEnter your SENTENCE in the space provided below.\n> ")
strLoop = sentence.upper() # strLoop = String Loop, and used an .upper() function for an approachable if/elif code block statement.
wordCount = {}
numWord = 1 # Number of Words = numerical string is set to 1. (for every space after a word, there corresponds an increment in the variable data in numWord.)
numVwl = 0 # Number of Vowels = numerical string is set to 0. (for each vowel character is satisfied through if/elif statement from for loop, there corresponds an increment in the variable data in numVwl.)
numCons = 0 # Number of Consonant = numerical string is set to 0. (for each consonant character is satisfied through if/elif statement from for loop, there corresponds an increment in the variable data in numVwl.)

for index in strLoop:
    if index in "AEIOU":
        numVwl += 1
    elif index in "BCDFGHJKLMNPQRSTVWXYZ":
        numCons += 1
    elif index in " ":
        numWord += 1

print(f"\nYour Input \n{sentence} | is accounted on the Python program following a statistics in character sentence length.")
print(f"\nWords: {numWord} \nVowels: {numVwl} \nConsonant: {numCons}\n")