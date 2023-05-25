import math



ABC = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
shABC = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'
key23andetc = []
key13andetc = []

def shprz(message):
    '''
    Шифр простой замены (1)
    '''
    cip = ''
    for i in message:
        if i in ABC:
            cip += shABC[ABC.index(i)]
        else:
            cip += i
    return cip

def dec_shprz(cip):
    '''
    Расшифровка (1)
    '''
    message = ''
    for i in cip:
        if i in shABC:
            message += ABC[shABC.index(i)]
        else:
            message += i
    return message

def affsh(message, key1, key2):
    '''
    Аффинныый шифр (2)
    '''
    cip = ''
    for i in message:
        if i in ABC:
            cip += ABC[(key1 * ABC.index(i) + key2) % len(ABC)]
        else:
            cip += i
    return cip

def deckey1(key1):
    '''
    key1 ** (-1)
    '''
    for i in range(len(ABC)):
        if math.gcd(key1, len(ABC)) == 1:
            if (key1 * i) % len(ABC) == 1:
                return i

def dec_affsh(cip, key1, key2):
    '''
    Расшифровка (2)
    '''
    message = ''
    for i in cip:
        if i in ABC:
            message += ABC[(deckey1(key1) * (ABC.index(i) - key2)) % len(ABC)]
        else:
            message += i
    return message

def affsh_rec(message, key1, key2, key12, key22):
    '''
    Аффинный рекурентный шифр (3)
    '''
    cip = ''
    global key23andetc, key13andetc
    for i in range(len(message)):
        if i == 0:
            key13andetc.append(key1)
            key23andetc.append(key2)
        elif i == 1:
            key13andetc.append(key12)
            key23andetc.append(key22)
        else:
            key13andetc.append((key13andetc[i-2] * key13andetc[i-1]) % len(ABC))
            key23andetc.append((key23andetc[i-2] + key23andetc[i-1]) % len(ABC))
    for i in range(len(message)):
        if message[i] in ABC:
            cip += ABC[(key13andetc[i] * ABC.index(message[i]) + key23andetc[i]) % len(ABC)]
        else:
            cip += message[i]
    return cip

def dec_affsh_rec(cip, key1, key2, key12, key22):
    '''
    Расшифровка (3)
    '''
    message = ''
    deckey11andetc = []
    for i in key13andetc:
        deckey11andetc.append(deckey1(i))
    for i in range(len(cip)):
        if cip[i] in ABC:
            message += ABC[(deckey11andetc[i] * (ABC.index(cip[i]) - key23andetc[i])) % len(ABC)]
    return message

print(shprz('HELLO'), "-", dec_shprz(shprz('HELLO')))
print(affsh('HELLO', 1, 4), "-", dec_affsh(affsh('HELLO', 1, 4), 1, 4))
print(affsh_rec('HELLO', 1, 4, 3, 2), "-", dec_affsh_rec(affsh_rec('HELLO', 1, 4, 3, 2), 1, 4, 3, 2))
