# Ejercicios: Nivel 3
print("Ejercicios: Nivel 3")
print(" ")

import random

# Programa 1
# Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list.
print("Programa 1")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Lista original:" , numbers)
def shuffleList (list):
    random.shuffle(list)
    return list
print('Lista aleatoria:', shuffleList(numbers))


# Programa 2 
# Write a function which returns an array of seven random numbers in a range of 0-9. 
# All the numbers must be unique.
print("Programa 2")
def randomNum ():
    lstRandumNum = set()
    while (len(lstRandumNum) < 7):
        randomN = random.choice('123456789')
        lstRandumNum.add(randomN)
    return list(lstRandumNum)
print("Números aleatorios:" , randomNum())
