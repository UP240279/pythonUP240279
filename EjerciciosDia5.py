## PROGRAMAS DÍA 5

## Ejercicios: Nivel 1
print("Ejercicios: Nivel 1")

# Porgrama 1 Declarar una lista vacía
print("Programa 1")
emptyList = list()
print(len(emptyList))

# Programa 2 Declarar una lista con más de 5 elementos
print("Programa 2")
drinks = ["Leche" , "Jugo" , "Agua" , "Refresco" , "Café" , "Malteada" , "Té"]

# Programa 3 Encuentra la longitud de tu lista
print("Programa 3")
print(len(drinks))

# Programa 4 Obtener el primer elemento, el elemento del medio y el último elemento de la lista
print("Programa 4")
print(drinks[0])
print(drinks[3])
print(drinks[6])

# Programa 5 Declara una lista llamada mixedDataTypes, pon tu(nombre, edad, altura, estado civil, dirección)
print("Programa 5")
mixedDataTypes = ["Vanessa" , "18" , "1.65" , "Soltera" , "Rojo 160, Lomas de Vistabella"]

# Programa 6 Declare una variable de lista llamada itCompanies y asigne los valores iniciales Facebook, Google, Microsoft, Apple, IBM, Oracle y Amazon
print("Programa 6")
itCompanies = ["Facebook" , "Google" , "Microsoft" , "Apple" , "IBM" , "Oracle" , "Amazon"]

# Programa 7 Imprima la lista usando print()
print("Programa 7")
print(itCompanies)

# Programa 8 Imprima el número de empresas en la lista
print("Programa 8")
print(len(itCompanies))

# Programa 9 Imprima la primera, la segunda y la última empresa
print("Programa 9")
print(itCompanies[0])
print(itCompanies[1])
print(itCompanies[6])

# Programa 10 Imprima el listado después de modificar una de las empresas
print("Programa 10")
print(itCompanies)
itCompanies[0] = "Meta"
print(itCompanies)

# Programa 11 Añadir una empresa de TI a itCompanies
print("Programa 11")
itCompanies.append("Tesla")
print(itCompanies)

# Programa 12 Insertar una empresa de TI en el medio de la lista de empresas
print("Programa 12")
itCompanies.insert(4, "Intel")
print(itCompanies)

# Programa 13 Cambie uno de los nombres de itCompanies a mayúsculas
print("Programa 13")
itCompanies[2] = itCompanies[2].upper()
print(itCompanies)

# Programa 14 Unir itCompanies con una cadena '#;'
print("Programa 14")
print("#;".join(itCompanies))

# Programa 15 Comprueba si una determinada empresa existe en la lista itCompanies
print("Programa 15")
doesExist = "Oracle" in itCompanies
print(doesExist)

# Programa 16 Ordenar la lista usando el método sort()
print("Programa 16")
itCompanies.sort()
print(itCompanies)

# Programa 17 Invierta la lista en orden descendente utilizando el método reverse()
print("Programa 17")
itCompanies.reverse()
print(itCompanies)

# Programa 18 Separa las primeras 3 empresas de la lista
print("Programa 18")
print(itCompanies[3:9])

# Programa 19 Elimina las últimas 3 empresas de la lista
print("Programa 19")
del itCompanies[6:9]
print(itCompanies)

# Programa 20 Elimina de la lista las empresas de TI intermedias
print("Programa 20")
itCompanies.remove("Meta")
itCompanies.remove("MICROSOFT")
print(itCompanies)

# Programa 21 21 Eliminar la primera empresa de TI de la lista
print("Programa 21")
itCompanies.pop(0)
print(itCompanies)

# Programa 22 Eliminar la o las empresas de TI intermedias de la lista
print("Programa 22")
itCompanies.pop(1)
print(itCompanies)

# Programa 23 Eliminar la última empresa de TI de la lista
print("Programa 23")
del itCompanies[-1]
print(itCompanies)

# Programa 24 Eliminar todas las empresas de TI de la lista
print("Programa 24")
del itCompanies[0]
print(itCompanies)

# Programa 25 Destruir la lista de empresas de TI
print("Programa 25")
itCompanies.clear()
print(itCompanies)

# Programa 26 Une las listas
print("Programa 26")
frontEnd = ['HTML', 'CSS', 'JS', 'React', 'Redux']
backEnd = ['Node','Express', 'MongoDB']
join = frontEnd + backEnd
print(join)

# Programa 27 Copie la lista unida y asígnela a una variable fullStack, luego inserte Python y SQL después de Redux
print("Programa 27")
fullStack = join.copy()
fullStack.insert(5, "Python")
fullStack.insert(6, "SQL")
print(fullStack)

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

