# Create a program that check if password is valid
# The password is valid if all criteria are met:
# a. Greater than 15 letters
# b. Have at least one capital letter
# c. Have at least one number
# d. Have at least one special char (!@#$%^&*()_+ etc)
# ex. input: P@ssw0rd+P@ssw0rd
# ouput: Valid

"""
VILLARIZA PYTHON PROGRAM
"""

import sys # Importing Sys for then the if-elif inside the for-loop will be interrupt.
import os # Importing Os so that the every Terminal Run would have an apparent and clear window space for user input.

"""
PROGRAM PREFACE, GUIDELINES, AND INSTRUCTIONS
"""
os.system('cls')
print("\n\033[33;1mVillariza's Password Validator\033[0m\n")
critTitle = '{Ttl}'.format(Ttl = "\033[32;1mCRITERIA FOR VALIDATION\033[0m\n")
varA = '{crtA}'.format(crtA = "\033[34;1mA.\033[0m Greater than \"\033[4m15 characters\033[0m\".\n")
varB = '{crtB}'.format(crtB = "\033[34;1mB.\033[0m Have at least \"\033[4mone capital letter\033[0m\". \n")
varC = '{crtC}'.format(crtC = "\033[34;1mC.\033[0m Have at least one \"\033[4mnumber or digit\033[0m\". \n")
varD = '{crtD}'.format(crtD = "\033[34;1mD.\033[0m Have at least \"\033[4mone special character\033[0m\" (e.g. \033[36m` ~ ! @ # $ % ^ & * ( ) - _ = + [ ] | ; : , < . > / ?\033[0m).\n")
print(f"{critTitle}{varA}{varB}{varC}{varD}")

"""
PYTHON FORMAT OUTPUT PERIPHERALS FOR PRINT-FUNCTION CONVENIENCE
"""
opt_Ttl = '{inpt_Ttl}'.format(inpt_Ttl = "\033[0m \n\033[33;1mPassword Status\033[0m \033[1m|\033[0m \033[31;1mINVALID\033[0m. \n\n\033[32;1mCRITERIA FOR VALIDATION\033[0m")
opt_varSpc = '{inpt_varSpc}'.format(inpt_varSpc = "\033[0m \n\033[33;1mInput Password\033[0m must not contain a \033[36;1mspace\033[0m\033[1m_\033[0m! Therefore, it is \033[31;1mINVALID\033[0m.")
opt_varA = '{inpt_varA}'.format(inpt_varA = "\n\033[34;1mA.\033[0m Greater than \"\033[4m15 characters\033[0m\" \033[36;1m(UNSETTLED)\033[0m.")
opt_varB = '{inpt_varB}'.format(inpt_varB = "\n\033[34;1mB.\033[0m Have at least \"\033[4mone capital letter\033[0m\" \033[36;1m(UNSETTLED)\033[0m.")
opt_varC = '{inpt_varC}'.format(inpt_varC = "\n\033[34;1mC.\033[0m Have at least one \"\033[4mnumber or digit\033[0m\" \033[36;1m(UNSETTLED)\033[0m.")
opt_varD = '{inpt_varD}'.format(inpt_varD = "\n\033[34;1mD.\033[0m Have at least \"\033[4mone special character\033[0m\" \033[36;1m(UNSETTLED)\033[0m.")
opt_lastMsg = '{inpt_lastMsg}'.format(inpt_lastMsg = "\n\n\033[1mPlease try again.\033[0m\n")

try:
    # User Inputs will be stored within the identified global variables below.
    usrInput = input("\x1B[3m\033[1mInput\x1B[0m and \033[4;1mEnter ↵\033[0m a \"\033[36;1mPASSWORD\033[0m\" character text down below on the space provided for verification purposes. \n\n\033[34;1m>>>\033[0m\033[1m ")
    usrOutput = '\033[0m\033[1m{}\033[0m'.format(usrInput.center(80, " "))
    opt_usrPword = '\n\n\" \033[0m\033[1m{}\033[0m \"\n'.format(usrInput)
    os.system('cls')

    # List of Global Variables that will be Used During While-For-Loop among If-Elif-Else Code-Block Statement.
    fnl_validation = False
    fnl_count = 0
    progSpace = False 
    progChrCount = False 
    progUpper = False 
    progDigit = False 
    progSpecialChr = False

    while not(fnl_validation):
        # Check if User Input Includes a Space in the Password Validator.
        for index in usrInput:
            if index.isspace():
                progSpace = True
                break
            else:
                continue
        # Criteria A. - For Loop within While Loop and If-Elif-Else Code-Block Program Statement Method.
        for index in usrInput:
            fnl_count += 1
            if fnl_count >= 15:
                progChrCount = True
                break
            else:
                continue
        # Criteria B. - For Loop within While Loop and If-Else Code-Block Program Statement Method.
        for index in usrInput:
            if index.isupper():
                progUpper = True
                break
            else:
                continue
        # Criteria C. - For Loop within While Loop and If-Else Code-Block Program Statement Method.
        for index in usrInput:
            if (index.isdigit() or index.isnumeric() or index.isdecimal()):
                progDigit = True
                break
            else:
                continue
        # Criteria D. - For Loop within While Loop and If-Else Code-Block Program Statement Method.
        for index in usrInput:
            # Only certain Special Characters (typically found on the Keyboard Output) will only be considered in this Program Statement Method.
            if index in "`~!@#$%^&*()-_=+[]|;:,<.>/?":
                progSpecialChr = True
                break
            else:
                continue
        # Password Invalid - Space Error
        if progSpace == True:
            print(opt_Ttl, opt_usrPword, opt_varSpc, opt_lastMsg)
            sys.exit()

        # MULTIPLE SELECTIONS - {ABCD} CODE-BLOCK STATISTICAL COMBINATION
        # Criteria A : progChrCount
        # Criteria B : progUpper
        # Criteria C : progDigit
        # Criteria D : progSpecialChr
        # When a Variable is False, it will be automatically justified as (UNSETTLED); and exact opposite if it is True.
        elif progChrCount == True:
            if progUpper == True:
                if progDigit == True:
                    if progSpecialChr == True:
                        fnl_validation = True
                        break
                    else:
                        # 1: CRITERIA D IS MISSING!
                        print(opt_Ttl, opt_usrPword, opt_varD, opt_lastMsg)
                        sys.exit()
                else:
                    if progSpecialChr == True:
                        # 2: CRITERIA C IS MISSING!
                        print(opt_Ttl, opt_usrPword, opt_varC, opt_lastMsg)
                        sys.exit()
                    else:
                        # 3: CRITERIA C AND D IS MISSING!
                        print(opt_Ttl, opt_usrPword, opt_varC, opt_varD, opt_lastMsg)
                        sys.exit()
            else:
                if progDigit == True:
                    if progSpecialChr == True:
                        # 4: CRITERIA B IS MISSING!
                        print(opt_Ttl, opt_usrPword, opt_varB, opt_lastMsg)
                        sys.exit()
                    else:
                        # 5: CRITERIA B AND D IS MISSING!
                        print(opt_Ttl, opt_usrPword, opt_varB, opt_varD, opt_lastMsg)
                        sys.exit()
                else:
                    if progSpecialChr == True:
                        # 6: CRITERIA B AND C IS MISSING!
                        print(opt_Ttl, opt_usrPword, opt_varB, opt_varC, opt_lastMsg)
                        sys.exit()
                    else:
                        # 7: CRITERIA B, C, AND D IS MISSING!
                        print(opt_Ttl, opt_usrPword, opt_varB, opt_varC, opt_varD, opt_lastMsg)
                        sys.exit()
        else:
            if progUpper == True:           
                if progDigit == True:
                    if progSpecialChr == True:
                        # 8: CRITERIA A IS MISSING!
                        print(opt_Ttl, opt_usrPword, opt_varA, opt_lastMsg)
                        sys.exit()
                    else:
                        # 9: CRITERIA A AND D IS MISSING!
                        print(opt_Ttl, opt_usrPword, opt_varA, opt_varD, opt_lastMsg)
                        sys.exit()
                else:
                    if progSpecialChr == True:
                        # 10: CRITERIA A AND C IS MISSING!
                        print(opt_Ttl, opt_usrPword, opt_varA, opt_varC, opt_lastMsg)
                        sys.exit()
                    else:
                        # 11: CRITERIA A, C, AND D IS MISSING!
                        print(opt_Ttl, opt_usrPword, opt_varA, opt_varC, opt_varD, opt_lastMsg)
                        sys.exit()
            else:
                if progDigit == True:
                    if progSpecialChr == True:
                        # 12: CRITERIA A AND B IS MISSING!
                        print(opt_Ttl, opt_usrPword, opt_varA, opt_varB, opt_lastMsg)
                        sys.exit()
                    else:
                        # 13: CRTERIA A, B, AND D IS MISSING!
                        print(opt_Ttl, opt_usrPword, opt_varA, opt_varB, opt_varD, opt_lastMsg)
                        sys.exit()
                else:
                    if progSpecialChr == True:
                        # 14: CRITERIA A, B, AND C IS MISSING!
                        print(opt_Ttl, opt_usrPword, opt_varA, opt_varB, opt_varC, opt_lastMsg)
                        sys.exit()
                    else:
                        # 15: ALL CRITERIA IS MISSING!
                        print(opt_Ttl, opt_usrPword, opt_varA, opt_varB, opt_varC, opt_varD, opt_lastMsg)
                        sys.exit()

    # When all variable methods given in the program have been confirmed True, the User Input will fall under the statement (PASSWORD VALID); thus, it will be present in the terminal as the center format is specified. 
    valPassOutput = '{val}'.format(val = "\" \033[33;1mPassword Status\033[0m \033[1m|\033[0m \033[32;1mVALID\033[0m \"".center(112, " "))
    print(f"\n\n{valPassOutput} \n\n\"{usrOutput}\"\n\n")

except EOFError or AssertionError as alpha:
    """
    When a defined or an ascertained error occurs on the Program method, it will automatically fall under except command.
    """
    progSlip = '\033[0m{}'.format(alpha)
    print(progSlip) 