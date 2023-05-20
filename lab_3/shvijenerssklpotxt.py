message1 = 'Why do you want me to pass?'
key1 = 'Kirillitsa'

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
            sdvig = ord(key[i]) - ord('a')
            if elm.isupper():
                ormessage += chr((ord(elm) - ord('A') - sdvig) % 26 + ord('A'))
            else:
                ormessage += chr((ord(elm) - ord('a') - sdvig) % 26 + ord('a'))
            key += cip[i]
        else:
            ormessage += elm
    return ormessage
  
cip = shvijenerssklpotxt(message1, key1)
print(cip, decshvijenerssklpotxt(cip, key1))
