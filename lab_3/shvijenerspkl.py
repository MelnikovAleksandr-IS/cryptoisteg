message1 = 'WHYDO YOU WANT'
key1 = 'ABC'


def shvijenerspkl(message, key):
    key = key * (len(message) // len(key) + 1)
    cip = ''
    for i in range(len(message)):
        elm = message[i]
        if elm.isalpha():
            sdvig = ord(key[i]) - ord('A')
            cip += chr((ord(elm) - ord('A') + sdvig) % 26 + ord('A'))
        else:
            cip += elm
    return cip
  
def decshvijenerspkl(cipmessage, key):
    key = key * (len(cipmessage) // len(key) + 1)
    ormessage = ''
    for i in range(len(cipmessage)):
        elm = cipmessage[i]
        if elm.isalpha():
            sdvig = ord('A') - ord(key[i])
            ormessage += chr((ord(elm) - ord('A') + sdvig) % 26 + ord('A'))
        else:
            ormessage += elm
    return ormessage

cip = shvijenerspkl(message1, key1)
print(cip, decshvijenerspkl(cip, key1))
