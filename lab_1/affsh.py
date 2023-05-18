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
