# Create a program that ask for a sentence as input.
# Display the number of words, vowels and consonants in the input 
# ex. input: Bahala kayo dyan
# output
# words: 3
# vowels: 6
# consonants: 8

senChar = input("\nEnter your SENTENCE in the space provided below.\n> ") # Sentence Character , and is used for input function.

def convoke(numWord = 1, numVwl = 0, numCons = 0):
    strLoop = senChar.upper()
    """
    String Loop, and used an .upper() function for an approachable if/elif code block statement.
    """
    for index in strLoop:
        if index in " ":
            numWord += 1
        elif index in "AEIOU":
            numVwl += 1
        elif index in "BCDFGHJKLMNPQRSTVWXYZ":
            numCons += 1
    return numWord, numVwl, numCons

fnl_Word, fnl_Vwl, fnl_Cons = convoke()

fnl_usrInput = '\nYour Input \n\"{}\" | is accounted on the Python program following a statistics in character sentence length.'.format(senChar)
fnl_Statement = '\nWords: {} \nVowels: {} \nConsonant: {}\n'.format(fnl_Word, fnl_Vwl, fnl_Cons)
print(fnl_usrInput)
print(fnl_Statement)