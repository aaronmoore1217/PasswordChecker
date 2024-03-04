import thing

LOGIN_FILE = 'PasswordChecker\\passwords.csv'

def menu():
    while (inp := input('login, signup, or quit: ').lower()) not in ('login', 'signup', 'quit'):
        pass
    match(inp):
        case 'login':
            login()
        case 'signup':
            signup()
        case 'quit':
            quit()

def login():
    while success := not (thing.loginCheck(LOGIN_FILE, username:=input('Username: '), input('Password: '))):
        if input("login error, quit?: ").lower() == 'quit':
            break
    if not success:
        print('successful login')
        while  (inp:=input('Change Password? y/n: ')) not in ('y','n'):
            pass
        print(inp)
        match(inp):
            case 'y':
                while not thing.checkPassword(password:=input('New Password: ')):
                    pass
                thing.changePassword(LOGIN_FILE, username, password)
            case 'n':
                pass
    else:
        menu()
    
def signup():
    while not (thing.checkUsername(username := input('Username: ')) and thing.checkPassword(password := input('Must contain a lowercase, uppercase, a number and a special character.\nPassword: '))):
        if not thing.checkUsername(username):
            print('username error! retry!')
            continue
        print('password error! retry!')
    thing.userSignup(LOGIN_FILE, username, password)

menu()

'''while not loggedIn:
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
                print(f'incorrect password! {attempts} attempts remaining')
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
'''
'''
'''