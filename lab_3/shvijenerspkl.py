message1 = 'Why do you want me to pass?'
key1 = 'Kirillitsa'


def shvijenerspkl(message, key):
    key = key * (len(message) // len(key) + 1)
    cip = ''
    for i in range(len(message)):
        elm = message[i]
        if elm.isalpha():
            sdvig = ord(key[i]) - ord('a')
            if elm.isupper():
                cip += chr((ord(elm) - ord('A') + sdvig) % 26 + ord('A'))
            else:
                cip += chr((ord(elm) - ord('a') + sdvig) % 26 + ord('a'))
        else:
            cip += elm
    return cip
  
def decshvijenerspkl(cipmessage, key):
    key = key * (len(cipmessage) // len(key) + 1)
    ormessage = ''
    for i in range(len(cipmessage)):
        elm = cipmessage[i]
        if elm.isalpha():
            sdvig = ord('a') - ord(key[i])
            if elm.isupper():
                ormessage += chr((ord(elm) - ord('A') + sdvig) % 26 + ord('A'))
            else:
                ormessage += chr((ord(elm) - ord('a') + sdvig) % 26 + ord('a'))
        else:
            ormessage += elm
    return ormessage

cip = shvijenerspkl(message1, key1)
print(cip, decshvijenerspkl(cip, key1))
