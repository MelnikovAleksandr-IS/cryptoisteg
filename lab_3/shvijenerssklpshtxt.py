message1 = 'WHYDOYOUWANT'
key1 = 'A'

def shvijenerssklpshtxt(message, key):
    global key1
    cip = ''
    for i in range(len(message)):
      cip += chr(((ord(message[i]) - 65) + (ord(key1[i]) - 65)) % 26 + 65)
      key1 += cip[i]
    return cip

def decshvijenerssklpshtxt(cip, key):
  ormessage = ''
  for i in range(len(cip)):
    ormessage += chr(((ord(cip[i]) - 65) - (ord(key[i]) - 65)) % 26 +65)
  return ormessage

cip = shvijenerssklpshtxt(message1, key1)
print(cip, decshvijenerssklpshtxt(cip, key1))
