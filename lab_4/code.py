from PIL import Image
import numpy
from copy import deepcopy
from math import sqrt

message = '110100001001110011010000101110001101000010111101110100001011100000101101110100001011111111010000101110001101000010110011'

def MSE(n, m, l, p_before, p_after):
    p_1 = 1 / (n * m)

    p_2 = 0
    for i in range(0, l):
        r = (p_before[i] - p_after[i]) **2
        p_2 += r
    
    result = p_1 * p_2
    return result

def PSNR(mse):
    result = 10 * ((255 ** 2) / mse)
    return result

def RMSE(mse):
    result = sqrt(mse)
    return result

def BER(b, b_er):
    result = b_er / b
    return result

def rgb_to_hex(r,g,b):
    return "#{:02x}{:02x}{:02x}".format(r,g,b)

def hex_to_dec(hex):
    return int(hex[1:], 16)

def dec_to_hex(dec):
    return hex(dec)[2:]

def hex_to_rgb(hex):
    while len(hex) < 6:
        hex += '0'
    return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))


def to_img(path, m, q):
    img = Image.open(path).convert('RGB')
    width, height = img.size
    pixels_rgb = list(img.getdata())
    pixels_dec = []

    for p in pixels_rgb:
        pixels_dec.append(hex_to_dec(rgb_to_hex(p[0], p[1], p[2])))

    original_pixels_dec = deepcopy(pixels_dec)

    for i in range(0, len(m)):
        new_pixel_in_dec = int((q * (pixels_dec[i] // q)) + ((q / 2) * int(m[i])))
        pixels_dec[i] = new_pixel_in_dec
        new_pixel_in_rgb = hex_to_rgb(dec_to_hex(new_pixel_in_dec))
        pixels_rgb[i] = new_pixel_in_rgb

    pixels = []

    for j in range(0, len(pixels_rgb), width):
        pixels.append(deepcopy(pixels_rgb[j:j+width]))


    pixels_array = numpy.array(pixels, dtype=numpy.uint8)
    new_image = Image.fromarray(pixels_array)
    new_image.save(path[:-4] + '_new.png')

    mse = MSE(width, height, len(pixels_dec), original_pixels_dec, pixels_dec)
    psnr = PSNR(mse)
    rmse = RMSE(mse)

    results = {
        'mse': mse,
        'psnr': psnr,
        'rmse': rmse,
    }

    return results



def from_img(path, q, l):
    global message

    img = Image.open(path)
    pixels_rgb = list(img.getdata())
    pixels_dec = []

    for p in pixels_rgb:
        pixels_dec.append(hex_to_dec(rgb_to_hex(p[0], p[1], p[2])))

    result = ''

    for i in range(0, l):
        trying_to_add_zero = (q * (pixels_dec[i] // q)) + ((q / 2) * 0)
        trying_to_add_one = (q * (pixels_dec[i] // q)) + ((q / 2) * 1)

        if abs(pixels_dec[i] - trying_to_add_zero) > abs(pixels_dec[i] - trying_to_add_one):
            result += '1'
        else:
            result += '0'

    return result


to_img("icon.png", message[:100], 100)

new_message = from_img("icon_new.png", 100, len(message[:100]))

nez = to_img("icon.png", message[:100], 100)
for i in nez:
  print(i + " " + str(nez[i]))

count = 0
m_n = list(message[:100])
for q in range(0, len(message[:100])):
  if (message[q] != new_message[q]):
    count += 1

ber = BER(len(message), count)

print('ber: ' + str(ber))
print('Неправильно извлеченных бит: ' + str(count))

if (message[:100] == new_message):
    print(1)
print(new_message)
