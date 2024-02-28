import thing

def userCheck(username, password):
    if thing.checkUsername(username):
        if thing.checkPassword(password):
            return True
        return 3
    return 2

loggedIn = False

attempts = 5

while not loggedIn:
    inp = input("login, signup, or quit: ").lower()
    while inp != 'login' and inp != 'signup' and inp != 'quit':
        inp = input('bad input! login, signup, or quit: ').lower()

    if inp == 'login':
        username = input("Username: ").lower()
        while username not in thing.csvToDict('PasswordChecker\\passwords.csv'):
            username = input("Username not found! Username: ")
        while attempts > 0:
            password = input("Password: ")
            if thing.csvToDict('PasswordChecker\\passwords.csv')[username] == password:
                print('successful login!')
                quit()
            else:
                attempts -= 1
                print('incorrect password! ' + f'{attempts}' + " attempts remaining")
        print('5 unsuccessful attempts, quitting')
        quit()
    while inp == 'signup':
        username = input("Username: ")
        password = input("Choose a password\nmust have an uppercase, lowercase, number, special character, and 8 or more characters: ")
        if username in thing.csvToDict('PasswordChecker\\passwords.csv'):
            RorC = input('user already exists! Return(R) or continue(C): ').lower()
            if RorC == 'c':
                continue
            if RorC == 'r':
                break
        else:
            Check = userCheck(username, password)
            print(Check)
            while Check != True:
                if Check == 3:
                    password = input("Password Incorrect, ReEnter: ")
                else:
                    username = input("Username Incorrect, ReEnter: ")
                Check = userCheck(username, password)
                print(Check)
            if Check == True:
                f = open('PasswordChecker\\passwords.csv', 'a')
                f.write('\n' + username.lower() + ',' + password)
                f.close()
                quit()
            
            continue
    if inp == 'quit':
        quit()