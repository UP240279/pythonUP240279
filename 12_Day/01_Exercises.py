# PROGRAMAS DÍA 12
print("PROGRAMAS DÍA 12")
print(" ")

# Ejercicios: Nivel 1
print("Ejercicios: Nivel 1")
print(" ")

import random
import string

# Programa 1 
# Write a function which generates a six digit/character random_user_id.
print("Programa 1")
def randomUserId():
    characters = string.ascii_letters + string.digits
    user = ''.join((random.choice(characters)) for j in  range (6))
    return user
print('Usuario:', randomUserId())


# Programa 2
# Modify the previous task. 
# Declare a function named user_id_gen_by_user. 
# It doesn’t take any parameters but it takes two inputs using input(). 
# One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
print("Programa 2")
def userIdGenByUser ():
    characters = string.ascii_letters + string.digits
    numCharacters = int(input("Ingrese el número de caracteres que quiere que tenga su usuario: "))
    numIDs = int(input("Ingrese el número de ID's que quiera: "))
    def generateRandomUser ():
        return ''.join((random.choice(characters))for p in range(numCharacters))
    print("Usuarios generados: ")
    for i in range (numIDs):
        print(generateRandomUser())
userIdGenByUser()


# Programa 3
# Write a function named rgb_color_gen. 
# It will generate rgb colors (3 values ranging from 0 to 255 each).
print("Programa 3")
def rgbColorGen ():
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    return (red,green,blue)
print("Colores RGB:" , rgbColorGen())
