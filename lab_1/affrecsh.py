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
  
def deckey1(key1):
    '''
    key1 ** (-1)
    '''
    for i in range(len(ABC)):
        if math.gcd(key1, len(ABC)) == 1:
            if (key1 * i) % len(ABC) == 1:
                return i

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
