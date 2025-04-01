# Ejercicios: Nivel 2
print("Ejercicios: Nivel 2")
print(" ")

import random

# Programa 1
# Write a function list_of_hexa_colors.
# Iteturns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. 
# Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. 
print("Programa 1")
def listOfHexaColors (num):
    hexaColor = []
    for j in range(num):
        randomColor = '#' + ''.join(random.choices('0123456789abcdef' , k = 6))
        hexaColor.append(randomColor)
    return hexaColor
print("Números de colores hexadecimales: ")
print(listOfHexaColors(5))


# Programa 2
# Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
print("Programa 2")
def listOfRgbColors (num):
    rgb = [] 
    for c in range(num):
        red = random.randint(0,255)
        green = random.randint(0,255)
        blue = random.randint(0,255)
        rgb.append(('rgb', red, green, blue))
    return rgb
print("Número de colores RGB en una matriz:" , listOfRgbColors(5))


# Programa 3
# Write a function generate_colors which can generate any number of hexa or rgb colors.
print("Programa 3")
def generateColors (type, num):
    colors = []
    if type == 'hexa':
        for j in range(num):
            randomColor = '#' + ''.join(random.choices('0123456789abcdef', k = 6))
            colors.append(randomColor)
        return colors
    else:
        for j in range(num):
            red = random.randint(0,255)
            green = random.randint(0,255)
            blue = random.randint(0,255)
            colors.append(('rgb', red, green, blue))
        return colors
print('Colores hexadecimales:', generateColors('hexa', 3))
print('Colores RGB:', generateColors('rgb', 2))
