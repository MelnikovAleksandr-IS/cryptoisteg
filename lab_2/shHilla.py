import numpy as np

'''
Зашифровка шифра Хилла (1)
'''
key = np.array([1, 3, 5], [2, 4, 6], [7, 8, 9]) #Создание матрицы ключа

message = "CRYPTOGRAPHY"
blsize = len(key)                                                    #Разбиение сообщения на блоки
bls =  [message[i: i+blsize] for i in range(0, len(message), blsize)]

nbl = [[ord(j) - 65 for j in c] for c in bls] #Преобразуем буквенных блоков в блоки чисел

cipn = [np.dot(key, c) % 26 for c in nbl] #Умножаем ключ-матрицу на блок чисел

cipbls = ''.join([chr(n + 65) for n in c]) for c in cipn] #Преобразование чисел в буквы
cip = ''.join(cipbls)

print(cip)

'''
Расшифровка (1)
'''
key_inv = np.linalg.inv(key) #Обратная ключ-матрица

cipbls = ['EDC', 'RFT', 'OFW']
cipn = [[ord(j) - 65 for j in c] for c in cipbls] #Преобразование зашифрованных блоков в числа

decn = [np.dot(key_inv, c) % 26 for c in cipn] #Умножение обратной матрицы ключа на блок чисел

decbls = [''.join([chr(n + 65) for n in c]) for c in decn] #Преобразование расшифрованных чисел обратно в буквы
dec = ''.join(decbls)

print(dec) 
