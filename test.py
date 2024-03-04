import csv
username = 'barks'
password = 'Fortnite123@'
FILE_PATH = 'PasswordChecker\\passwords.csv'
with open(FILE_PATH, 'a', newline='\n') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow([username, password])