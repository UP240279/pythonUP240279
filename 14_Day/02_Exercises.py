# Ejercicios: Nivel 2
print("Ejercicios: Nivel 2")
print(" ")

from functools import reduce


# Programa 1
# Use map to create a new list by changing each country to uppercase in the countries list.
print("Programa 1")
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
print("Lista de países:" , countries)
def changeToUpper(country):
    return country.upper()
countriesUpperCased = map(changeToUpper, countries)
print("Lista de países en mayúsculas:" , list(countriesUpperCased))


# Programa 2
# Use map to create a new list by changing each number to its square in the numbers list.
print("Programa 2")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Lista de números:" , numbers)
def square(x):
    return x ** 2
numbersSquared = map(square, numbers)
print("Lista de los cuadrados de los números:" , list(numbersSquared))


# Programa 3
# Use map to change each name to uppercase in the names list.
print("Programa 3")
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
print("Lista de nombres:" , names)
def changeNamesToUpper(name):
    return name.upper()
namesUpperCased = map(changeNamesToUpper, names)
print("Lista de nombres en mayúsculas:" , list(namesUpperCased))


# Programa 4
# Use filter to filter out countries containing 'land'.
print("Programa 4")
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
print("Lista de países:" , countries)
def containsLand(country):
    if "land" in country:
        return True
    return False
countriesLand = filter(containsLand, countries)
print("Países que contienen la palabra 'land'" , list(countriesLand))


# Programa 5
# Use filter to filter out countries having exactly six characters.
print("Programa 5")
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
print("Lista de países:" , countries)
def isCountryLong(country):
    if len(country) == 6:
        return True
    return False
longCountries = filter(isCountryLong, countries)
print("Lista de países con 6 caracteres:" , list(longCountries))


# Programa 6
# Use filter to filter out countries containing six letters and more in the country list.
print("Programa 6")
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
print("Lista de países:" , countries)
def countryLong(country):
    if len(country) >= 6:
        return True
    return False
longCountries2 = filter(countryLong, countries)
print("Lista de países con 6 y más letras:" , list(longCountries2))


# Programa 7
# Use filter to filter out countries starting with an 'E'.
print("Programa 7")
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
print("Lista de países:" , countries)
countriesStartE = list(filter(lambda country: country.startswith("E"), countries))
print("Países que comienzan con E:" , countriesStartE)


# Programa 8
# Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback)).
print("Programa 8")
chainedList = list(map(str.upper, filter(lambda country: 'land' in country.lower(), countries)))
print("Países que contienen la palabra 'land' en la lista de países en mayúscula:" , chainedList)


# Programa 9
# 
print("Programa 9")
numbersAndFood = ("Soup" , "Meat" , 4 , 27 , "Nuts" , 18)
print("Lista:" , numbersAndFood)
def getStringLists(list):
    return [item for item in list if isinstance(item, str)]
print("Los elementos de cadena en la lista son:" , getStringLists(numbersAndFood))


# Programa 10
# Use reduce to sum all the numbers in the numbers list.
print("Programa 10")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Lista de números:" , numbers)
result = reduce(lambda x, y: x + y, numbers)
print("La suma de los números de la lista es:" , result)





