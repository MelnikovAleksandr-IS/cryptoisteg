from PIL import Image
from math import sqrt


def char_to_bin(char): # Функция для получения двоичного представления символа
    return bin(ord(char))[2:].zfill(8)

def bin_to_char(binary): # Функция для получения символа из двоичного представления
    return chr(int(binary, 2))

def get_bit(number, index): # Функция для получения бита из двоичного представления числа
    binary = str(number)
    if index >= len(binary): # если индекс больше длины строки, то бита с таким индексом нет
        return None
    else:
        return int(binary[-(index+1)]) 

def set_bit(number, index, bit):
    binary = bin(number)[2:].zfill(32)  # Переводим число в двоичную систему счисления и дополняем нулями до 32 символов
    binary_list = list(binary)  # Преобразуем строку в список символов
    binary_list[-index-1] = str(bit)  # Устанавливаем заданный бит
    binary = ''.join(binary_list)  # Преобразуем список обратно в строку
    return int(binary, 2)

def embed_message(image_path, message): # Функция для внедрения сообщения в изображение
    image = Image.open(image_path)
    pixels = image.load()
    width, height = image.size
    binary_message = ''.join([char_to_bin(char) for char in message]) # Преобразуем сообщение в бинарный формат
    if len(binary_message) > width * height: # Проверяем, что сообщение можно внедрить в изображение
        raise ValueError('Сообщение слишком длинное для данного изображения')
    index = 0
    for y in range(height): # Внедряем сообщение в изображение
        for x in range(width):
            if index < len(binary_message):
                pixel = pixels[x, y]
                r, g, b = pixel
                r_bit = get_bit(r, 0) # Получаем младший бит красной компоненты
                message_bit = int(binary_message[index]) # Получаем значение бита из сообщения
                if r_bit != message_bit: # Если значения не совпадают, меняем младший бит красной компоненты
                    r = set_bit(r, 0, message_bit)
                pixels[x, y] = (r, g, b)
                index += 1
    image.save('embedded.png') # Сохраняем изображение с внедренным сообщением

def extract_message(image_path): # Функция для извлечения сообщения из изображения
    image = Image.open(image_path)
    pixels = image.load()
    width, height = image.size
    binary_message = ''
    for y in range(height):  # Извлекаем сообщение из изображения
        for x in range(width):
            pixel = pixels[x, y]
            r, g, b = pixel
            r_bit = get_bit(r, 0) # Получаем младший бит красной компоненты
            binary_message += str(r_bit) # Добавляем значение бита в сообщение
    message = ''
    for i in range(0, len(binary_message), 8): # Преобразуем бинарное сообщение в символьный формат
        message += bin_to_char(binary_message[i:i+8])
    return message










def MSE(N, M, l, pb, pa):
    p1 = 1 / (N * M)
    p2 = 0
    for i in range(0, l):
        if i + 1 > len(pa):
            r = 0
        else:
            r = (pb[i] - pa[i]) **2
        p2 += r
    res = p1 * p2
    return res

def PSNR(Mse):
    res = 10 * ((255 ** 2) / Mse)
    return res

def RMSE(Mse):
    res = sqrt(Mse)
    return res

def EC(l, N, M):
    res = l / (N * M)
    return res

def BER(b, bosh):
    res = bosh / b
    return res
