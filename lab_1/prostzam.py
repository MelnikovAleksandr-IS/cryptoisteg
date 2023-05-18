def shprz(message, shABC):
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

def dec_shprz(cip, shABC):
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
