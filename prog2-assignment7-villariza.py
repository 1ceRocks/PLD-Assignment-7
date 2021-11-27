# Create a program that check if password is valid
# The password is valid if all criteria are met:
# a. Greater than 15 letters
# b. Have at least one capital letter
# c. Have at least one number
# d. Have at least one special char (!@#$%^&*()_+ etc)
# ex. input: P@ssw0rd+P@ssw0rd
# ouput: Valid
import sys

count = 0
print("\nVillariza's Password Validator.\n \nCRITERA FOR VALIDATION\nA. Greater than \"15 characters\".\nB. Have at least \"one capital letter\". \nC. Have at least one \"number or digit\". \nD. Have at least \"one special chracter\" (e.g. !@#$%^&*()_+).\n")
usrInput = input("Enter a \"PASSWORD\" text down below on the space provided in order for Python to validate your input. \n> ")

while count < 15:
    for index in usrInput:
        fnl_count = count + 1
        count += 1
    if fnl_count < 15:
        print("Invalid. Criteria A.)")
        sys.exit()    

if fnl_count > 15:
    for index in usrInput:
        if index.isupper():
            for index in usrInput:
                if index.isdigit():
                    for index in usrInput:
                        if index in "!@#$%^&*()_+":
                            print("Valid.")
                            sys.exit()
                        else:
                            pass
                else:
                    pass
        else:
            pass
    print("Invalid.")