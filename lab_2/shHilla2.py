
import numpy as np

size = 2


def bukvn(elm):
  return (ord(elm) - ord('A'))

def numbkv(elm):
  return chr(elm + ord('A'))

keym = np.random.randint(0, 26, size=(size, size))
while np.linalg.det(keym) == 0:
  keym = np.random.randint(0, 26, size=(size, size))
invm = np.linalg.inv(keym)
keym = keym.astype(int)
invm = inv.astype(int)

def shHilla(message, key, n):
  mesbls = [message[i:i+n] for i in range(0, len(message), n)]
  cip = ""
  for mesbl in mesbls:
    if len(mesbl) < n:
      mesbl += "Z"*(n-len(mesbl))
    mesbl = [bukvn(elm) for elm in mesbl]
    mesbl = np.array(mesbl).reshape((n, 1))
    res = np.mod(np.dot(key, mesbl), 26)
    res = res.flatten().tolist()
    cip += "".join([numbkv(elm) for elm in res])
  return cip

def decshHilla(cipmessage, inv, n):
  cipbls = [cipmessage[i:i+n] for i in range(0, len(cipmessage), n)]
  ormessage = ""
  for cipbl in cipbls:
    cipbl = [bukvn(elm) for elm in cipbl]
    cipbl = np.array(cipbl).reshape((n, 1))
    res = np.mod(np.dot(inv, cipbl), 26)
    res = res.flatten().tolist()
    ormessage += "".join([numbkv(elm) for elm in res])

cip = shHilla('HELLO', keym, size)
print(cip, decshHilla(cip, invm, size
