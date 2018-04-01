# -*- coding: utf-8 -*-
# Password and headline generator bit ya know

# Import stuff
import os
from random import choice, randrange
from base64 import b64encode

charset2 = [
    'abcdefghijkmnpqrstuvwxyz',
    'ABCDEFGHJKLMNPQRSTUVWXYZ',
    '123456789',
    '!$%&()=?[]#<>+-_',
]

lead1 = [
    'Welcome to passwd.studio, your strong password is:',
    'Passwd.studio has generated some loot for you:',
    'Password123, I dont think so. Maybe try out:',
    ]

def mkKey(lenKey=64):
     key = os.urandom(lenKey)
     token = b64encode(key).decode('utf-8')
     return token

def mkLead():
    index = randrange(0,len(lead1))
    lead = lead1[index]
    return lead

def mkPasswordWeb(lenPassword=16):
    pwd = []
    charset = choice(charset2)
    while len(pwd) < lenPassword:
        pwd.append(choice(charset))
        charset = choice(list(set(charset2) - set([charset])))
    return ''.join(pwd)

# Uncomment to test the fuctions in file
# if __name__ == '__main__':
#    print(mkLead())
    
