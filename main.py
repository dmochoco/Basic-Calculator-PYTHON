# menu based calculator program 

# ********************************************
# FUNCTIONS
# ********************************************

# menu function that returns choice user has entered
def menu():
    # text block that shows user
    # their menu options
    print("\nThis is a Menu for a Calculator!\n\nYour options are as follows:")
    print("A - Addition\nS - Subtraction\nM - Multiplication\nD - Division")
    print("\n")

    # prompts user to enter their choice 
    # note* userChoice is automatically capitilized
    userChoice = input("Please type in the corresponding letter to pick your option:").upper()
    print("\n")

    # returns choice that user made
    return userChoice

# number inputting function
def numInput():
    num1 = input("\nPlease enter the first number: ") 
    num2 = input("Please enter the next number: ")
    return num1, num2

# addition function that is used when the user selects addition
def addition():
    print("You have selected Addition (A) !")
    num1, num2 = numInput()
    sum = float(num1) + float(num2)
    print("\n{0} + {1} = {2}\n".format(num1, num2, sum))

# subtraction function that is used when the user selects subtraction
def subtraction():
    print("You have selected Subtraction (S) !")
    num1, num2 = numInput()
    difference = float(num1) - float(num2)
    print("\n{0} - {1} = {2}\n".format(num1, num2, difference))

# multiply function that is used when the user selects multiplication
def multiply():
    print("You have selected Multiplication (M) !")
    num1, num2 = numInput()
    product = float(num1) * float(num2)
    print("\n{0} * {1} = {2}\n".format(num1, num2, product))

# division function that is used when the user selects division
def division():
    print("You have selected Division (D) !")
    num1, num2 = numInput()
    quotient = float(num1) / float(num2)
    print("\n{0} / {1} = {2}\n".format(num1, num2, quotient))

# prompts user to see if they want to exit their program
def exit():
    exitChoice = input("Would you like to exit (Y/N)?").upper()
    if(exitChoice == "Y" or exitChoice == "y"):
        print("\n")
        quit()
    elif(exitChoice == "N" or exitChoice == "n"):
        pass
    else:
        print("Invalid option please select again")
        exit()

# algorithm that uses menu and arithemetic functions to perform calculations
def runMenu():
    # menu function is called to prompt menu and ask user to make a choice
    userChoice = menu()

    # condition block that shows what the user has selected
    if(userChoice == "A"): # if addition is selected
        addition()
    elif(userChoice == "S"): # if subtraction is selected
        subtraction()
    elif(userChoice == "M"): # if multiplication is selected
        multiply()
    elif(userChoice == "D"): # if division is selected
        division()
    else: # if an invalid option is selected, prompt user to pick another option, and loop back to starting menu
        print("\nYou have picked an invalid option please select again. ")
        runMenu()

# ********************************************
# DRIVER CODE
# ********************************************

foo = True
while(foo): # infinite while loop 
    runMenu() # run menu
    exit() # prompt exit