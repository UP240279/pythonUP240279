# Ejercicios: Nivel 3
print("Ejercicios: Nivel 3")
print(" ")


# Programa 1
# Write a function called is_prime, which checks if a number is prime.
def isPrime (num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True 
print("¿El número 17 es primo?" , isPrime(17))


# Programa 2
# Write a functions which checks if all items are unique in the list.
print("Programa 2")
list = [1, 2, 3, 4, 5, 3]
print("Lista:" , list)
def itemsUnique (list):
    for i in list:
        if list.count(i) > 1:
            return False
    return True
print("¿Todos los elementos de la lista son únicos?" , itemsUnique(list))


# Programa 3
# Write a function which checks if all the items of the list are of the same data type.
print("Programa 3")
list = [1, 2, 3, 4, 5]
print("Lista:" , list)
def sameDataType (list):
    types = []
    for i in list:
        types.append(type(i))
    if len(set(types)) == 1:
        return True
    return False
print("¿Todos los elementos de la lista son del mismo tipo de datos?" , sameDataType(list))


# Programa 4
# Write a function which check if provided variable is a valid python variable
print("Programa 4")
def isPythonVariable (variable):
    typ = type(variable)
    types = [str, complex, int, float, bool, list, tuple, set, dict]
    if typ in types:
        return True
    return False
print("¿La variable proporcionada es una variable de Python válida?" , isPythonVariable(4))


# Programa 5
# Go to the data folder and access the countries_data.py file.
print("Programa 5")
import countries_data as datac
data = datac.countries


# Programa 5.1
# Create a function called the most_spoken_languages in the world. 
# It should return 10 or 20 most spoken languages in the world in descending order.
print("Programa 5.1")
from collections import Counter
def mostSpokenLanguages (dict):
    allLanguages = [lang for country in dict for lang in country['languages']] 
    cout = Counter(allLanguages)
    top10 = cout.most_common(10)
    return top10
print("Los 10 idiomas más hablados son:" , mostSpokenLanguages(data))


# Programa 5.2
# Create a function called the most_populated_countries. 
# It should return 10 or 20 most populated countries in descending order.
print("Programa 5.2")
def mostPopulatedCountries (dict):
    mostPopulated = []
    top10Countries = sorted(dict, key=lambda x: x["population"], reverse=True)[:10]
    print('Los 10 países más poblados son:')
    for country in top10Countries:
        mostPopulated.append(f"{country['name']} - {country['population']}")
    return mostPopulated
print(mostPopulatedCountries(data))
print("revisado")