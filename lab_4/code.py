from PIL import Image


def char_to_bin(char): # Функция для получения двоичного представления символа
    return bin(ord(char))[2:].zfill(8)

def bin_to_char(binary): # Функция для получения символа из двоичного представления
    return chr(int(binary, 2))

def get_bit(number, index): # Функция для получения бита из двоичного представления числа
    return (number >> index) & 1

def set_bit(number, index, bit): # Функция для установки бита в двоичном представлении числа
    mask = 1 << index
    return (number & ~mask) | (bit << index)

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
