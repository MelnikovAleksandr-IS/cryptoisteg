message1 = 'WHYDOYOUWANT'
key1 = 'ABC'

def shvijenerssklpotxt(message, key):
    cip = ''
    for i in range(len(message)):
        elm = message[i]
        if elm.isalpha():
            sdvig = ord(key[i]) - ord('A')
            cip += chr((ord(elm) - ord('A') + sdvig) % 26 + ord('A'))
            key += cip[-1]
        else:
            cip += elm
    return cip       
  
def decshvijenerssklpotxt(cip, key):
    ormessage = ''
    for i in range(len(cip)):
        elm = cip[i]
        if elm.isalpha():
            sdvig = ord(key[i]) - ord('A')
            ormessage += chr((ord(elm) - ord('A') - sdvig) % 26 + ord('A'))
            key += cip[i]
        else:
            ormessage += elm
    return ormessage
  
cip = shvijenerssklpotxt(message1, key1)
print(cip)
