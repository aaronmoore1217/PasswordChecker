import thing
# import csv
# username = 'balls'
# password = 'Fortnite123@'
# FILE_PATH = 'PasswordChecker\\passwords - Copy.csv'
# def changePassword(username, password):
#         lisp=[]
#         with open(FILE_PATH, 'r', newline='\n') as f:
#                 for x in f:
#                         p = x.strip().split(',')
#                         if p[0] == username:
#                                 p[1] = password
#                         lisp.append(p)
#                         print(p)
#         with open(FILE_PATH, 'w', newline='\n') as f:
#                 writer=csv.writer(f, delimiter=',')
#                 writer.writerows(lisp)
LOGIN_FILE = 'PasswordChecker\passwords.csv'
while success := not (thing.loginCheck(LOGIN_FILE, input('Username: '), input('Password: '))):
        if input("login error, quit?: ").lower() == 'quit':
                break
if not success:
        print('successful login')
else:
        quit()
