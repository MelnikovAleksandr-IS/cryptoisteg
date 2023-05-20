import numpy as np

size = 2


def bukvn(elm):
  return (ord(elm) - ord('A'))

def numbkv(elm):
  return chr(elm + ord('A'))

keym = np.random.randint(0, 26, size=(size, size))
while np.linalg.det(key) == 0:
  keym = np.random.randint(0, 26, size=(size, size))
inv = np.linalg.inv(key)
key = key.astype(int)
inv = inv.astype(int)

def shHilla(message, key, n):
  mesbls = [message[i:i+n] for i in range(0, len(message), n)]
  cip = ""
  for mesbl in mesbls:
    if len(mesbl) < n:
      mesbl += "Z"*(n-len(mesbl))
    mesbl = [bukvn(elm) for elm in mesbl]
    mesbl = np.array(mesbl).reshape((n, 1))
    res = np.mod(np.dot(keym, mesbl), 26)
    res = res.flatten().tolist()
    cip += "".join([numbkv(elm) for elm in res])
  return cip
  
