# Create a program that ask for a sentence as input.
# Display the number of words, vowels and consonants in the input 
# ex. input: Bahala kayo dyan
# output
# words: 3
# vowels: 6
# consonants: 8

"""
VILLARIZA PYTHON PROGRAM
"""

senChar = input("\nEnter your SENTENCE in the space provided below.\n> ") # Sentence Character , and is used for input function.

def convoke(numWord = 0, numVwl = 0, numCons = 0):
    strLoop = senChar.upper() # Upper Function will be utilized to employ convenicence on the if-elif process.
    """
    String Loop, and used an .upper() function for an approachable if/elif code block statement.
    """
    for index in strLoop:
        if index in "AEIOU": # For every detected vowel on the index loop, there corresponds a numerical addition on the value of a string variable.
            numVwl += 1
        elif index in "BCDFGHJKLMNPQRSTVWXYZ": # For every detected consonant on the index loop, there corresponds a numerical addition on the value of a string variable.
            numCons += 1
    numWord = senChar.split() # Used split function to implement a tuple ordered list of values.
    return len(numWord), numVwl, numCons # Used len word to identify how many values are present on a tuple table from .split() function on numWord local variable.

# These three global variables shall present the recorded process that is programmed from the def convoke():
fnl_Word, fnl_Vwl, fnl_Cons = convoke() # Three Variables that will serves as the positional arguments (following left-to-right order sequence) for the parameters in def-function.

fnl_usrInput = '\nYour Input \n\"{}\" | is accounted on the Python program following a statistics in character sentence length.'.format(senChar)
fnl_Statement = '\nWords: {0} \nVowels: {1} \nConsonant: {2}\n'.format(fnl_Word, fnl_Vwl, fnl_Cons).center(60)
"""
Supplied some format functions in purpose for additional complexity in print method statement in the Python Program.
"""
print(fnl_usrInput)
print(fnl_Statement)