def decshvijenerssklpshtxt(cip, key):
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
  
  message = decshvijenerssklpshtxt
