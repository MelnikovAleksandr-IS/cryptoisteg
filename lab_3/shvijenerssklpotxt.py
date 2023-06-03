message1 = 'WHYDOYOUWANT'
key1 = 'ABC'
while len(key1) < len(message1):
    for i in range(len(message1)):
        key1 += message1[i]

def shvijenerssklpotxt(message, key):
    cip = ''
    for i in range(len(message)):
        cip += chr(((ord(message[i]) - 65) + (ord(key[i]) - 65)) % 26 + 65)
    return cip

def decshvijenerssklpotxt(cip, key):
    ormessage = ''
    for i in range(len(cip)):
        ormessage += chr(((ord(cip[i]) - 65) - (ord(key[i]) - 65)) % 26 +65)
    return ormessage
  
cip = shvijenerssklpotxt(message1, key1)
print(cip, decshvijenerssklpotxt(cip, key1))
