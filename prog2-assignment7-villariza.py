# Create a program that check if password is valid
# The password is valid if all criteria are met:
# a. Greater than 15 letters
# b. Have at least one capital letter
# c. Have at least one number
# d. Have at least one special char (!@#$%^&*()_+ etc)
# ex. input: P@ssw0rd+P@ssw0rd
# ouput: Valid

import sys # Importing Sys for then the if-elif inside the for-loop will be interrupt

print("\nVillariza's Password Validator.\n \nCRITERA FOR VALIDATION\nA. Greater than \"15 characters\".\nB. Have at least \"one capital letter\". \nC. Have at least one \"number or digit\". \nD. Have at least \"one special chracter\" (e.g. !@#$%^&*()_+).\n")

try:
    usrInput = input("Enter a \"PASSWORD\" text down below on the space provided in order for Python to validate your input. \n> ")
    usrOutput = '{}'.format(usrInput)

    fnl_count = 0
    while fnl_count < 15:
        for index in usrInput:
            count = fnl_count + 1
            fnl_count += 1
        if count < 15:
            print("\nPassword INVALID. \nCriteria A. - \"Greater than 15 characters\" is not justified. \nPlease try again.\n")
            sys.exit()
    
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
            print("\nPassword INVALID. \nCriteria B. - \"Have at least one capital letter\" is not justified. \nPlease try again.\n")
            sys.exit()

    fnl_digit = False
    while not(fnl_digit):
        for index in usrInput:
            if index.isdigit():
                fnl_digit = True
                break
            else:
                continue
        if index.isdigit() == True:
            None
        else:
            print("\nPassword INVALID \nCriteria C. - \"Have at least one number\" is not justified. \nPlease try again.\n")     
            sys.exit()      

    fnl_splChar = False
    while not(fnl_splChar):
        for index in usrInput:
            if index in "!@#$%^&*()_+":
                fnl_splChar = True
                break
            else:
                continue
        if index in "!@#$%^&*()_+":
            None
        else:
            print("\nPassword INVALID. \nCriteria D. - \"Have at least one special char (!@#$%^&*()_+ etc)\" is not justified. \nPlease try again.\n")
            sys.exit()   

    print(f"\n\n\nPassword VALID. \n\"{usrOutput}\"\n".center(67, " "))

except EOFError or AssertionError as alpha:
    progSlip = '{}'.format(alpha)
    print(progSlip)     