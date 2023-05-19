import numpy as np


message = "HELLOWORLD"
key = np.array([[3, 8], [2, 5]])
inv = np.linalg.inv(key)
cipns = []
cip = ""

def messagen(message):
   mesn = []
   for bukva in message:
      if bukva == " ":
         mesn.append(0)
      else:
         mesn.append(ord(bukva) - 64)
   return mesn

def numberm(numbers):
   messagetxt = ""
   for number in numbers:
      if number == 0:
         messagetxt += " "
      else:
         messagetxt.append(chr(number) + 65)
   return messagetxt
   
def shHilla(message, key):
global cipns, cip
   messagens = messagen(message)
   blsize = int(np.sqrt(key.size))
   raznitsa = len(messagens) % len(blsize)
   if raznitsa != 0:
      messagens.extend([0]*(blsize - raznitsa))
   mesmatritsa = np.array(messagens).reshape(-1, blsize)
   cipmatritsa = np.dot(key, mesmatritsa) % 26
   cipns = cipmatritsa.flatten().tolist()
   cip = numberm(cipns)
   return cip
   
def decshHilla(cip, inv):
   cipmatritsa = np.array(cipns).reshape(-1, blsize)
   mesmatritsa = np.dot(inv, cipmatritsa) % 26
   messagens = mesmatritsa.flatten().tolist()
   message = numberm(messagens)
   return message

print("Зашиврованный текст:", shHilla(message, key))
print("Расшифрованный текст:", decshHilla(cip, inv))
