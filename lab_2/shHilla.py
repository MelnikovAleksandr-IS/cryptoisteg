import numpy as np


message1 = "CRYPTOGRAPHY"
key1 = np.array([[0, 12, 29], [16, 9, 14], [9, 8, 13]]) #Создание ключа-матрицы

cipbls1 = []
key_inv1 = np.linalg.inv(key1) #Обратная ключ-матрица
bls = []

def shhill(message, key):
  global cipbls1, bls
  '''
  Зашифровка шифра Хилла (1)
  '''
  blsize = len(key)                                                    #Разбиение сообщения на блоки
  bls =  [message[i: i+blsize] for i in range(0, len(message), blsize)]
  
  nbl = [[ord(j) - 65 for j in c] for c in bls] #Преобразуем буквенных блоков в блоки чисел
  
  cipn = [np.dot(key, c) % 26 for c in nbl] #Умножаем ключ-матрицу на блок чисел
  
  cipbls1 = [''.join([chr(n + 65) for n in c]) for c in cipn] #Преобразование чисел в буквы
  cip = ''.join(cipbls1)
  
  return cip

print(shhill(message1, key1))


def decshhilla(cipbls, key_inv):
  global bls, cipbls1
  '''
  Расшифровка (1)
  '''
  cipn = [[ord(j) - 65 for j in c] for c in bls] #Преобразование зашифрованных блоков в числа
  
  decn = [np.dot(key_inv, c) % 26 for c in cipn] #Умножение обратной матрицы ключа на блок чисел
  
  decbls = [''.join([chr(n + 65) for n in c]) for c in decn] #Преобразование расшифрованных чисел обратно в буквы
  dec = ''.join(decbls)
  
  return dec

print(decshhilla(cipbls1, key_inv1))
  
