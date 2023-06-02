import numpy as np
alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
def hill(text):
     res = ''
     key = np.array([[4, 5],
            [3, 4]])
     if len(text) % 2 != 0:
         text += 'Z'
     for i in range(0, len(text), 2):
         x = (alphabet.index(text[i]) * key[0][0] + alphabet.index(text[i+1]) * key[1][0]) % len(alphabet)
#         y = (alphabet.index(text[i]) * key[0][1] + alphabet.index(text[i+1]) * key[1][1]) % len(alphabet)
#         res += alphabet[x] + alphabet[y]
#     return res
# print(hill('NARUTO'))

#Расшифрование
# alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
# def obratnoe_chislo(x): # Функция по нахождению обратного числа
#     res = ''
#     for i in range(len(alphabet)):
#         if (x * i) % len(alphabet) == 1:
#             res += str(i)
#             break
#     return res
# def re_mat(mat): # Функция по нахождению обратной матрицы
#     det = int(np.linalg.det(mat))
#     det = int(obratnoe_chislo(det))
#     t_mat = np.transpose(mat)
#     res = [[],[]]
#     res[0].append((t_mat[1][1] * det) % len(alphabet))
#     res[0].append(((-1) * t_mat[1][0] * det) % len(alphabet))
#     res[1].append(((-1) * t_mat[0][1] * det) % len(alphabet))
#     res[1].append((t_mat[0][0] * det) % len(alphabet))
#     res = np.array(res)
#     return res
# def de_hill(en_text):
#     res = ''
#     key = np.array([[4, 5],
#                     [3, 4]])
#     re_key = re_mat(key)
#     for i in range(0, len(en_text), 2):
#         x = (alphabet.index(en_text[i]) * re_key[0][0] + alphabet.index(en_text[i+1]) * re_key[1][0]) % len(alphabet)
#         y = (alphabet.index(en_text[i]) * re_key[0][1] + alphabet.index(en_text[i+1]) * re_key[1][1]) % len(alphabet)
#         res += alphabet[x] + alphabet[y]
#     return res
# print(de_hill('ANYJOV'))



#Рекуррентный шифр Хилла 
#Зашифрование
# alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
# def recurrent_hill(text):
#     res = ''
#     key_1 = np.array([[3, 4, 3],
#            [2, 2, 1],
#            [1, 5, 1]])
#     key_2 = np.array([[4, 3, 1],
#            [1, 2, 3],
#            [3, 1, 1]])
#     key_3 = key_2.dot(key_1)
#     if len(text) % 3 == 2:
#         text += 'Z'
#         text += 'Z'
#     if len(text) % 3 == 1:
#         text += 'Z'
#     for i in range(0, len(text), 3):
#         x = (alphabet.index(text[i]) * key_1[0][0] + alphabet.index(text[i + 1]) * key_1[1][0] + alphabet.index(text[i + 2]) * key_1[2][0]) % len(alphabet)
#         y = (alphabet.index(text[i]) * key_1[0][1] + alphabet.index(text[i + 1]) * key_1[1][1] + alphabet.index(text[i + 2]) * key_1[2][1]) % len(alphabet)
#         z = (alphabet.index(text[i]) * key_1[0][2] + alphabet.index(text[i + 1]) * key_1[1][2] + alphabet.index(text[i + 2]) * key_1[2][2]) % len(alphabet)
#         res += alphabet[x] + alphabet[y] + alphabet[z]
#         break
#     for i in range(3, len(text), 3):
#         x1 = (alphabet.index(text[i]) * key_2[0][0] + alphabet.index(text[i + 1]) * key_2[1][0] + alphabet.index(text[i + 2]) * key_2[2][0]) % len(alphabet)
#         y1 = (alphabet.index(text[i]) * key_2[0][1] + alphabet.index(text[i + 1]) * key_2[1][1] + alphabet.index(text[i + 2]) * key_2[2][1]) % len(alphabet)
#         z1 = (alphabet.index(text[i]) * key_2[0][2] + alphabet.index(text[i + 1]) * key_2[1][2] + alphabet.index(text[i + 2]) * key_2[2][2]) % len(alphabet)
#         res += alphabet[x1] + alphabet[y1] + alphabet[z1]
#         break
#     for i in range(6, len(text), 3):
#         x1 = (alphabet.index(text[i]) * key_3[0][0] + alphabet.index(text[i + 1]) * key_3[1][0] + alphabet.index(text[i + 2]) * key_3[2][0]) % len(alphabet)
#         y1 = (alphabet.index(text[i]) * key_3[0][1] + alphabet.index(text[i + 1]) * key_3[1][1] + alphabet.index(text[i + 2]) * key_3[2][1]) % len(alphabet)
#         z1 = (alphabet.index(text[i]) * key_3[0][2] + alphabet.index(text[i + 1]) * key_3[1][2] + alphabet.index(text[i + 2]) * key_3[2][2]) % len(alphabet)
#         res += alphabet[x1] + alphabet[y1] + alphabet[z1]
#         break
#     return res
# print(recurrent_hill(list('ABONEMENT')))

# Расшифрование
# alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
# def obratnoe_chislo(x): # Функция по нахождению обратного числа
#     res = ''
#     for i in range(len(alphabet)):
#         if (x * i) % len(alphabet) == 1:
#             res += str(i)
#             break
#     return res
# def re_mat(mat): # Функция по нахождению обратной матрицы
#     det = int(np.linalg.det(mat))
#     det = int(obratnoe_chislo(det))
#     t_mat = np.transpose(mat)
#     res = [[],[],[]]
#     res[0].append(((t_mat[1][1] * t_mat[2][2] - t_mat[2][1] * t_mat[1][2]) * det) % len(alphabet))
#     res[0].append((((-1) * (t_mat[1][0] * t_mat[2][2] - t_mat[2][0] * t_mat[1][2])) * det) % len(alphabet))
#     res[0].append(((t_mat[1][0] * t_mat[2][1] - t_mat[2][0] * t_mat[1][1]) * det) % len(alphabet))
#
#     res[1].append((((-1) * (t_mat[0][1] * t_mat[2][2] - t_mat[2][1] * t_mat[0][2])) * det) % len(alphabet))
#     res[1].append(((t_mat[0][0] * t_mat[2][2] - t_mat[2][0] * t_mat[0][2]) * det) % len(alphabet))
#     res[1].append((((-1) * (t_mat[0][0] * t_mat[2][1] - t_mat[2][0] * t_mat[0][1])) * det) % len(alphabet))
#
#     res[2].append(((t_mat[0][1] * t_mat[1][2] - t_mat[1][1] * t_mat[0][2]) * det) % len(alphabet))
#     res[2].append((((-1) * (t_mat[0][0] * t_mat[1][2] - t_mat[1][0] * t_mat[0][2])) * det) % len(alphabet))
#     res[2].append(((t_mat[0][0] * t_mat[1][1] - t_mat[1][0] * t_mat[0][1]) * det) % len(alphabet))
#     res = np.array(res)
#     return res
# def de_recurrent_hill(en_text):
#     res = ''
#     key_1 = np.array([[3, 4, 3],
#                       [2, 2, 1],
#                       [1, 5, 1]])
#     key_2 = np.array([[4, 3, 1],
#                       [1, 2, 3],
#                       [3, 1, 1]])
#     re_key_1 = re_mat(key_1)
#     re_key_2 = re_mat(key_2)
#     re_key_3 = re_key_1.dot(re_key_2)
#
#     for i in range(0, len(en_text), 3):
#         x = (alphabet.index(en_text[i]) * re_key_1[0][0] + alphabet.index(en_text[i + 1]) * re_key_1[1][0] + alphabet.index(en_text[i + 2]) * re_key_1[2][0]) % len(alphabet)
#         y = (alphabet.index(en_text[i]) * re_key_1[0][1] + alphabet.index(en_text[i + 1]) * re_key_1[1][1] + alphabet.index(en_text[i + 2]) * re_key_1[2][1]) % len(alphabet)
#         z = (alphabet.index(en_text[i]) * re_key_1[0][2] + alphabet.index(en_text[i + 1]) * re_key_1[1][2] + alphabet.index(en_text[i + 2]) * re_key_1[2][2]) % len(alphabet)
         res += alphabet[x] + alphabet[y] + alphabet[z]
         break
     for i in range(3, len(en_text), 3):
         x = (alphabet.index(en_text[i]) * re_key_2[0][0] + alphabet.index(en_text[i + 1]) * re_key_2[1][0] + alphabet.index(en_text[i + 2]) * re_key_2[2][0]) % len(alphabet)
         y = (alphabet.index(en_text[i]) * re_key_2[0][1] + alphabet.index(en_text[i + 1]) * re_key_2[1][1] + alphabet.index(en_text[i + 2]) * re_key_2[2][1]) % len(alphabet)
         z = (alphabet.index(en_text[i]) * re_key_2[0][2] + alphabet.index(en_text[i + 1]) * re_key_2[1][2] + alphabet.index(en_text[i + 2]) * re_key_2[2][2]) % len(alphabet)
         res += alphabet[x] + alphabet[y] + alphabet[z]
         break
     for i in range(6, len(en_text), 3):
         x = (alphabet.index(en_text[i]) * re_key_3[0][0] + alphabet.index(en_text[i + 1]) * re_key_3[1][0] + alphabet.index(en_text[i + 2]) * re_key_3[2][0]) % len(alphabet)
         y = (alphabet.index(en_text[i]) * re_key_3[0][1] + alphabet.index(en_text[i + 1]) * re_key_3[1][1] + alphabet.index(en_text[i + 2]) * re_key_3[2][1]) % len(alphabet)
         z = (alphabet.index(en_text[i]) * re_key_3[0][2] + alphabet.index(en_text[i + 1]) * re_key_3[1][2] + alphabet.index(en_text[i + 2]) * re_key_3[2][2]) % len(alphabet)
         res += alphabet[x] + alphabet[y] + alphabet[z]
         break
     return res
print(de_recurrent_hill('QUPOHLSON'))
