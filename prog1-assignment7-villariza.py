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

import os # Importing Os so that the every Terminal Run would have an apparent and clear window space for user input.

os.system('cls')
print("\n\033[36;1mVILLARIZA\033[0m \033[1m|\033[0m \033[34;1mCharacter\033[0m \033[33;1mSentence\033[0m \033[1mEvaluator\033[0m\n")
senChar = input("\x1B[3m\033[1mInput\x1B[0m and \033[4;1mEnter ↵\033[0m a \"\033[36;1mSENTENCE\033[0m\" in the provided space below. \n\n\033[34;1m>>>\033[0m\033[1m ") # Sentence Character , and is used for input function.
os.system('cls')

def convoke(numWord = 0, numVwl = 0, numCons = 0):
    strLoop = senChar.upper() # Upper Function will be utilized to employ convenicence on the if-elif process.
    """
    String Loop, and used an .upper() function for an approachable if/elif code block statement.
    """
    try:
        for index in strLoop:
            if index in "AEIOU": # For every detected vowel on the index loop, there corresponds a numerical addition on the value of a string variable.
                numVwl += 1
            elif index in "BCDFGHJKLMNPQRSTVWXYZ": # For every detected consonant on the index loop, there corresponds a numerical addition on the value of a string variable.
                numCons += 1
        numWord = senChar.split() # Used split function to implement a tuple ordered list of values.
        return len(numWord), numVwl, numCons # Used len word to identify how many values are present on a tuple table from .split() function on numWord local variable.
    except EOFError or AssertionError as alpha:
        """
        When a defined or an ascertained error occurs on the Program method, it will automatically fall under except command.
        """
        progSlip = '\033[0m{}'.format(alpha)
        print(progSlip)  

# These three global variables shall present the recorded process that is programmed from the def convoke():
fnl_Word, fnl_Vwl, fnl_Cons = convoke() # Three Variables that will serves as the positional arguments (following left-to-right order sequence) for the parameters in def-function.

fnl_usrInput = '\n\033[36;1mSENTENCE INPUT\033[0m \n| \" \033[1m{}\033[0m \" | is accounted on the Python program following a \x1B[3m\033[32;1mstatistics\x1B[0m in \033[34;1mCharacter\033[0m \033[33;1mSentence\033[0m length.'.format(senChar)
fnl_Statement = '\n\033[34;1mWORD/S\033[0m        \033[34;1m:\033[0m  \033[32;1m{0}\033[0m \n\033[33;1mVOWEL/S\033[0m       \033[33;1m:\033[0m  \033[32;1m{1}\033[0m \n\033[1mCONSONANT/S\033[0m   \033[1m:\033[0m  \033[32;1m{2}\033[0m\n'.format(fnl_Word, fnl_Vwl, fnl_Cons)
"""
Supplied some format functions in purpose for additional complexity in print method statement in the Python Program.
"""
print(fnl_usrInput)
print(fnl_Statement)