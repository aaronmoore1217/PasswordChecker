import thing
import hashmaxxing
import csv
lisp=[]
with open('PasswordChecker\\passwords.csv', 'r', newline='\n') as f:
        for x in f:
                p = x.strip().split(',')
                print(hashmaxxing.verifyPassword('Fortnite213!', p[1]))
#                 lisp.append(p)
# with open('PasswordChecker\passwords.csv', 'w', newline='\n') as f:
#         writer=csv.writer(f, delimiter=',')
#         writer.writerows(lisp)