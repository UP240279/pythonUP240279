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



