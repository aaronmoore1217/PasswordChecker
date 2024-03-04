import csv
from re import match
def loginCheck(filename, username, password):
    with open(filename, newline='\n') as csvfile:
        dipt = csv.reader(csvfile, delimiter=',')
        login = [username, password]
        return login in dipt
    
def userSignup(filename, username, password):
    with open(filename, 'a') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow([username, password])
        
def changePassword(filename, username, password):
        lisp=[]
        with open(filename, 'r', newline='\n') as f:
                for x in f:
                        p = x.strip().split(',')
                        if p[0] == username:
                                p[1] = password
                        lisp.append(p)
        with open(filename, 'w', newline='\n') as f:
                writer=csv.writer(f, delimiter=',')
                writer.writerows(lisp)
    
def checkUsername(username): 
    return ' ' not in username if len(username) >= 3 else False

def checkPassword(password):
    return bool(match("^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$", password))

''' def checkPassword(password):
    regex = ({'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'}, 
{'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' '},
{'1', '2', '3', '4', '5', '6', '7', '8', '9'}, {'!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '.','{', '}', '\'', '\"', ','})
    if '\'' in password or '\"' in password or ',' in password:
         return False
    correct = False
    if len(password) < 8:
         return False
    for y in regex:
        for x in password:
            if x in y:
                correct = True
                break
            correct = False
        if not correct:
            break
    return correct
'''
''' def checkUsername(username):
# 
#     if ' ' in username or len(username) < 3:
#         return False
#     else: 
#         return True
'''
''' def csvToDict(filename):
    # try:
    #     file = open(filename, 'r')
    # except:
    #     print('file error!')
    #     quit()
    # else:
    #     for x in file:
    #         key = x.strip('\n').split(',')
    #         dipt[key[0]] = key[1]
    #     file.close()
    #     return dipt
'''