# Ejercicios: Nivel 2
print("Ejercicios: Nivel 2")
print(" ")


# Programa 1
# Declare a function named evens_and_odds. 
# It takes a positive integer as parameter and it counts number of evens and odds in the number.
print("Programa 1")
def evenAndOdds (num):
    odds = 0
    evens = 0
    for i in range(num + 1):
        if i%2 == 1:
            odds = odds + 1
        else:
            evens = evens + 1
    return odds , evens
print("La cantidad de números pares e impares dentro del rango 100 es de:" , evenAndOdds(100))


# Programa 2
# Call your function factorial.
# It takes a whole number as a parameter and it return a factorial of the number.
print("Programa 2")
def factorial (num):
    factorial = 1
    if (num < 0):
        return "El factorial no está definido para números negativos"
    else:
        for i in range(1 , num + 1):
            factorial = factorial * i
            return factorial
print("El factorial del número 7 es:" , factorial(7))


# Programa 3
# Call your function is_empty.
# It takes a parameter and it checks if it is empty or not.
print("Programa 3")
list = []
def isEmpty (parameter):
    if len(parameter) == 0:
        return "Está vacío"
    else:
        return "No está vacío"
print("El parámetro:" , isEmpty(list))


# Programa 4
# Write different functions which take lists. 
# They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
print("Programa 4")
grades = [6, 8, 9, 7, 9, 8, 10, 8]
print("Calificaciones:" , grades)
from collections import Counter

def calculateMean(list):
    sum = 0
    for i in list:
        sum = sum + i
    mean = sum / len(list)
    return mean
print('Media:', round(calculateMean(grades), 2))

def calculateMedian(list):
    list.sort()
    median = list[int(len(list) / 2 + 1)]
    return median
print('Mediana:', calculateMedian(grades))

def calculateMode(list):
    cout = Counter(list)
    mode = cout.most_common(1)
    mode = mode[0]
    mode = mode[0]
    return mode
print('Moda:', calculateMode(grades))

def calculateRange(list):
    list.sort()
    range = list[-1] - list[0]
    return range
print('Rango:', calculateRange(grades))

def calculateVariance(list):
    sum = 0
    for i in list:
        sum = sum + i
    mean = sum / len(list)
    n = []
    for i in list:
        n.append((i - mean) ** 2)
    sumN = 0
    for i in n:
        sumN = sumN + i
    return sumN / len(list)
print('Varianza:', round(calculateVariance(grades), 2))

def calculateStd(list):
    sum = 0
    for i in list:
        sum= sum + i
    mean = sum / len(list)
    n = []
    for i in list:
        n.append((i - mean) ** 2)
    sumN = 0
    for i in n:
        sumN = sumN + i
    variance = round(sumN / len(list), 2)
    return variance * 0.5
print('Desviación estándar:', calculateStd(grades))
print("revisado")