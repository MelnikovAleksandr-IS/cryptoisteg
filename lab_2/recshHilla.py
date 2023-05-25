
import numpy as np


key = np.array([[2, 5], [3, 8]])
size = 2

def bukvn(elm):
  return (ord(elm) - ord('A'))

def numbkv(elm):
  return chr(elm + ord('A'))
  
def recshHilla(message, key, n):
  mesbls = [message[i:i+n] for i in range(0, len(message), n)]
  cip = ''
  res = []
  proshmatr = np.identity(n) 
  for mesbl in mesbls:
    if len(mesbl) < n:
      mesbl += Z * (n - len(mesbl))
    mesbl = [bukvn(elm) for elm in mesbl]
    mesbl = np.array(mesbl).reshape((n, 1))
    key = (key + proshmatr) % 26
    proshmatr = key
    reselm = np.mod(np.dot(key, mesbl), 26)
    res.append(reselm)
    res = res.flatten().tolist()
    cip += "".join([numbkv(elm) for elm in res])
  return cip 

def decshHilla(cipmessage, key, n):
  cipbls = [cipmessage[i:i+n] for i in range(0, len(cipmessage), n)]
  ormessage = ""
  res = []
  proshmatr = np.identity(n)
  for cipbl in cipbls:
    cipbl = [bukvn(elm) for elm in cipbl]
    cipbl = np.array(cipbl).reshape((n, 1))
    key = (key + proshmatr) % 26
    proshmatr = key
    inv = np.linalg.inv(key) % 26
    reselm = np.mod(np.dot(inv, cipbl), 26)
    res.append(reselm)
    res = res.flatten().tolist()
    ormessage += "".join([numbkv(elm) for elm in res])
  return ormessage 
    
  
