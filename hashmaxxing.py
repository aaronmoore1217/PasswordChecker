from pyargon2 import hash
from pyargon2 import Argon2Error
def hashPassword(password):
    salt = hash(password, salt=password)
    hashWord = hash(password, salt)
    return hashWord

def verifyPassword(password, hashe):
    salt = hash(password, password)
    hashWord = hash(password, salt)
    return hashWord == hashe

