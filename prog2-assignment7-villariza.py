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

import sys # Importing Sys for then the if-elif inside the for-loop will be interrupt
import string

print("\n\033[33;1mVillariza's Password Validator\033[0m\n")
critTitle = '{Ttl}'.format(Ttl = "\033[32;1mCRITERIA FOR VALIDATION\033[0m\n")
varA = '{crtA}'.format(crtA = "\033[34;1mA.\033[0m Greater than \"\033[4m15 characters\033[0m\".\n")
varB = '{crtB}'.format(crtB = "\033[34;1mB.\033[0m Have at least \"\033[4mone capital letter\033[0m\". \n")
varC = '{crtC}'.format(crtC = "\033[34;1mC.\033[0m Have at least one \"\033[4mnumber or digit\033[0m\". \n")
varD = '{crtD}'.format(crtD = "\033[34;1mD.\033[0m Have at least \"\033[4mone special character\033[0m\" (e.g. \033[36m` ~ ! @ # $ % ^ & * ( ) - _ = + [ ] | ; : , < . > / ?\033[0m).\n")
print(f"{critTitle}{varA}{varB}{varC}{varD}")

try:
    # User Inputs will be stored within the identified global variables below.
    usrInput = input("\x1B[3m\033[1mInput\x1B[0m and \033[4;1mEnter ↵\033[0m a \"\033[36;1mPASSWORD\033[0m\" character text down below on the space provided for verification purposes. \n\n\033[34;1m>>>\033[0m\033[1m ")
    usrOutput = '\033[0m\033[1m{}\033[0m'.format(usrInput.center(80, " "))

    # Criteria A. - While, For, and If-Else Code-Block Program Statement Method.
    fnl_count = 0
    while fnl_count <= 15:
        for index in usrInput:
            if index.isspace() == True:
                spaceInVal = '\033[0m \n\033[33;1mInput Password\033[0m must not contain a \033[36;1mspace\033[0m\033[1m_\033[0m! Therefore, it is \033[31;1mINVALID\033[0m. \n\033[1mPlease try again.\033[0m\n'.center(90, " ")
                print(spaceInVal)
                sys.exit()  
            else:
                count = fnl_count + 1
                fnl_count += 1
        if count <= 15:
            print("\033[0m \n\033[33;1mPassword Status\033[0m \033[1m|\033[0m \033[31;1mINVALID\033[0m. \n\n\033[32;1mCRITERIA FOR VALIDATION\033[0m \n\033[34;1mA.\033[0m Greater than \"\033[4m15 characters\033[0m\" \033[36;1m(UNSETTLED)\033[0m. \n\033[1mPlease try again.\033[0m\n")
            sys.exit()
        else:
            break
    
    # Criteria B. - While, For, and If-Else Code-Block Program Statement Method.
    fnl_upper = False
    while not(fnl_upper):
        for index in usrInput:
            if index.isupper():
                fnl_upper = True
                break
            else:
                continue
        if index.isupper() == True:
            None
        else:
            print("\033[0m \n\033[33;1mPassword Status\033[0m \033[1m|\033[0m \033[31;1mINVALID\033[0m. \n\n\033[32;1mCRITERIA FOR VALIDATION\033[0m - \n\033[34;1mB.\033[0m Have at least \"\033[4mone capital letter\033[0m\" \033[36;1m(UNSETTLED)\033[0m. \n\033[1mPlease try again.\033[0m\n")
            sys.exit()

    # Criteria C. - While, For, and If-Else Code-Block Program Statement Method.
    fnl_digit = False
    while not(fnl_digit):
        for index in usrInput:
            if index.isdigit():
                fnl_digit = True
                break
            else:
                continue
        if (index.isdigit() or index.isnumeric or index.isdecimal()) == True:
            None
        else:
            print("\033[0m \n\033[33;1mPassword Status\033[0m \033[1m|\033[0m \033[31;1mINVALID\033[0m. \n\n\033[32;1mCRITERIA FOR VALIDATION\033[0m - \n\033[34;1mC.\033[0m Have at least one \"\033[4mnumber or digit\033[0m\" \033[36;1m(UNSETTLED)\033[0m. \n\033[1mPlease try again.\033[0m\n")     
            sys.exit()      

    # Criteria D. - While, For, and If-Elif-Else Code-Block Program Statement Method.
    fnl_splChar = False
    while not(fnl_splChar):
        for index in usrInput:
            if index in "`~!@#$%^&*()-_=+[]|;:,<.>/?":
                fnl_splChar = True
                break
            elif index.isspace():
                break
            else:
                continue
        if index in "`~!@#$%^&*()-_=+[]|;:,<.>/?":
            None
        elif index.isspace():
            spaceInVal = '\033[0m \n\033[33;1mInput Password\033[0m must not contain a \033[36;1mspace\033[0m\033[1m_\033[0m! Therefore, it is \033[31;1mINVALID\033[0m. \n\033[1mPlease try again.\033[0m\n'.center(90, " ")
            print(spaceInVal)
            sys.exit()    
        else:
            print(f"\033[0m \n\033[33;1mPassword Status\033[0m \033[1m|\033[0m \033[31;1mINVALID\033[0m. \n\n\033[32;1mCRITERIA FOR VALIDATION\033[0m - \n\033[34;1mD.\033[0m Have at least \"\033[4mone special character\033[0m\" \033[36;1m(UNSETTLED)\033[0m. \n\033[1mPlease try again.\033[0m\n")
            sys.exit()   

    # When all methods have been justified, the User Input will fall under the statement (PASSWORD VALID); thus, it will be present in the terminal as the center format is specified. 
    valPassOutput = '{val}'.format(val = "\" \033[33;1mPassword Status\033[0m \033[1m|\033[0m \033[32;1mVALID\033[0m \"".center(112, " "))
    print(f"\n\n{valPassOutput} \n\n\"{usrOutput}\"\n\n")

except EOFError or AssertionError as alpha:
    """
    When a defined or an ascertained error occurs on the Program method, it will automatically fall under except command.
    """
    progSlip = '\033[0m{}'.format(alpha)
    print(progSlip)     