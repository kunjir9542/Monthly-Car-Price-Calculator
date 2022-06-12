loginPWD = input("Hello, please enter your password to see your passwords")
print("Login Successful")

passwords = []


def homePage():
    print("------------------------------------------------------------------------------------")
    print("Your saved passwords are: ")

    for x in passwords:
        print(x)

    print("------------------------------------------------------------------------------------")
    inp = input("Do you want to add or remove a password, or do you want ot log out?  (A/R/L)")
    if inp == "L":
        print("Logging Out...")
        print("------------------------------------------------------------------------------------")

        loginScreen()

    if inp == "A":
        addPWD()

    if inp == "R":
        removePWD()


def loginScreen():
    pwdMatch = False
    while not pwdMatch:

        reloginPWD = input("Hello, please enter your password to see your passwords")
        if reloginPWD == loginPWD:
            pwdMatch = True
            print("Login Successful")
            homePage()
        else:
            print("Sorry, incorrect password. Please try again")
            print("------------------------------------------------------------------------------------")

def addPWD():
    print("------------------------------------------------------------------------------------")
    newPWD = input("Enter a password to add to your list")
    passwords.append(newPWD)
    homePage()

def removePWD():
    print("------------------------------------------------------------------------------------")
    removePassword = input("Enter a password to remove from your list")
    passwordExist = False
    for x in passwords:
        if removePassword == x:
            passwordExist = True

    if passwordExist == False:
        print("Password does not exist, try again")
        removePWD()
    else:
        print("Password removed successfully")
        passwords.remove(removePassword)
        homePage()

homePage()
