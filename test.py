import re
usernameRegex = re.compile('[a-zA-Z0-9]')
print(re.match(usernameRegex, 'fA1rt').group())