# -*- coding: utf-8 -*-
# Password generator functions

# Import stuff
import os
from random import choice
from base64 import b64encode

# Complex Charset including special char
charset1 = [
    'abcdefghijklmnopqrstuvwxyz',
    'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
    '0123456789',
    '^!\$%&/()=?{[]}+~#-_.:,;<>|\\',
    ]

# Simple Charset omitting potentially misleading chars
charset2 = [
    'abcdefghijkmnpqrstuvwxyz',
    'ABCDEFGHJKLMNPQRSTUVWXYZ',
    '123456789',
    '!$%&()=?[]#<>+-_',
]

def mkPassword(lenPassword=22):
    pwd = []
    charset = choice(charset1)
    while len(pwd) < lenPassword:
        pwd.append(choice(charset))
        charset = choice(list(set(charset1) - set([charset])))
    return ''.join(pwd)

def mkKey(lenKey=64):
     key = os.urandom(lenKey)
     token = b64encode(key).decode('utf-8')
     return token

# Uncomment to test the fuctions in file
# if __name__ == '__main__':
#    print(mkPassword())