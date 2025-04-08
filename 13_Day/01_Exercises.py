# PROGRAMAS DÍA 13
print("PROGRAMAS DÍA 13")
print(" ")


# Programa 1
# Filter only negative and zero in the list using list comprehension.
print("Programa 1")
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
print("Lista de números:" , numbers)
negativeAndZero = [i for i in numbers if i <= 0]
print("Lista de números negativos y cero:" , negativeAndZero)


# Programa 2
# Flatten the following list of lists of lists to a one dimensional list.
print("Programa 2")
listOfLists = [[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
print("Lista de listas:" , listOfLists)
flattenedList = [number for row in listOfLists for number in row]
flattenedList = [number for row in flattenedList for number in row]
print("Lista aplanada:" , flattenedList) 


# Programa 3
# Using list comprehension create the following list of tuples:
print("Programa 3")
listOfTuples = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(0,11)]
print("Lista generada:" , listOfTuples)


# Programa 4
# Flatten the following list to a new list:
print("Programa 4")
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
print("Lista de listas de países:" , countries)
flattenedCountries = [[country.upper(), country[:3].upper(), capital.upper()] for [(country, capital)]in countries]
print("Lista de países aplanada:" , flattenedCountries)


# Programa 5
# Change the following list to a list of dictionaries:
print("Programa 5")
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
print("Lista de listas de países:" , countries)
listDictionaries = [{'country': item[0][0].upper(), 'city': item[0][1].upper()} for item in countries]
print("Lista convertida a diccionario:" , listDictionaries)


# Programa 6
# Change the following list of lists to a list of concatenated strings:
print("Programa 6")
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
print("Lista de nombres:" , names)
concatenatedNames = [name[0][0] + " " + name[0][1] for name in names]
print("Lista de nombres concatenados:" , concatenatedNames)


# Programa 7
# Write a lambda function which can solve a slope or y-intercept of linear functions.
print("Programa 7")
print("Los valores son: 3, 7, 6, 12")
slope = lambda x1, x2, y1, y2: (y2-y1)/(x2-x1)
print("La pendiente es:" , slope(3, 7, 6, 12))
print("Revisado")