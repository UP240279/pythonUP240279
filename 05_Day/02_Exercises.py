## Ejercicios: Nivel 2
print("Ejercicios: Nivel 2")

# Programa 0 lista de edades 
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Programa 0.1 Ordena la lista y encuentra la edad mínima y máxima
print("Programa 0.1")
ages.sort()
print(ages)
print(ages[0], "," ,ages[len(ages)-1])

# Programa 0.2 Agregue la edad mínima y la edad máxima nuevamente a la lista
print("Programa 0.2")
ages.insert(0, 19)
ages.insert(-1, 26)
print(ages)

# Programa 0.3 Encuentra la edad media (un elemento intermedio o dos elementos intermedios divididos por dos)
print("Programa 0.3")
medianAge = (ages[5] + ages[6]) / 2
print("La edad media es:" , medianAge)

# Programa 0.4 Encuentra la edad promedio (suma de todos los elementos dividida por su número)
print("Programa 0.4")
average = sum(ages) / len(ages)
print("El promedio es:" , average)

# Programa 0.5 Encuentra el rango de edades (máximo menos mínimo)
print("Programa 0.5")
range = ages[-1] - ages[0]
print("El rango de edades es de:" , range)

# Programa 0.6 Compare el valor de (mín - promedio) y (máx - promedio), use el método abs()
print("Programa 0.6")
min = abs(ages[0] - average)
max = abs(ages[-1] - average)
print(min)
print(max)
comparison = (min and max)
print("El resultado de la comparación es:" , comparison)

# Programa 1 Encuentre el país o los países intermedios en la lista de países
print("Programa 1")
import countries as c
print(len(c.countries)) 
media = int(len(c.countries) / 2)
print(media)
print(c.countries[media] + ", " + c.countries[media + 1]) 
if 'Mexico' in c.countries:
    print("México está en:" , c.countries.index('Mexico'))
else:
    print('No está')

# Programa 2 Dividir la lista de países en dos listas iguales si es par o no hay un país más para la primera mitad
print("Programa 2")
print(int(len(c.countries) / 2))
list1 = c.countries[0:96]
list2 = c.countries[96:193]
print("Longitud de la primera lista:" , len(list1))
print('Primera lista:' , list1)
print("Longitud de la segunda lista:" , len(list2))
print('Segunda lista:' , list2)

# Programa 3 ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark'] Desglose los primeros tres países y el resto como países escandinavos
print("Programa 3")
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
scandicCountries = countries[3:]
print(scandicCountries)
