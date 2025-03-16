## Ejercicios: Nivel 2
print("Ejercicios: Nivel 2")

# Programa 1 Desempaquetar a hermanos y padres de familyMembers
print("Programa 1")
familyMembers = ('Gabriel', 'Orlando', 'Paulo', 'Montse', 'Mariel', 'Ivonne', 'Adriana', 'Carlos')
siblings = familyMembers[0:6]
print("Hermanos:" , siblings)
parents = familyMembers[6:]
print("Padres:" , parents)

# Programa 2 Crea tuplas de frutas, verduras y productos animales. Une las tres tuplas y asígnalas a una variable llamada foodStuffTp
print("Programa 2")
fruits = ("Apple", "Orange", "Watermelon", "Pineaple", "Banana")
vegetables = ("Lettuce", "Potato", "Carrot", "Onion")
animalProducts = ("Milk", "Eggs", "Meat", )
foodStuffTp = fruits + vegetables + animalProducts
print(foodStuffTp)

# Programa 3 Cambie la tupla de foodStuffTp a una lista foodStuffLt
print("Programa 3")
foodStuffLt = list(foodStuffTp)
print(foodStuffLt)

# Programa 4 Extraiga el elemento o los elementos del medio de la tupla foodStuffTp o de la lista foodStuffLt
print("Programa 4")
print(len(foodStuffLt))
print(foodStuffLt[5],",", foodStuffLt[6])

# Programa 5 Separe los primeros tres elementos y los últimos tres elementos de la lista foodStuffLt
print("Programa 5")
fisrstThree = foodStuffLt[0:3]
lastThree = foodStuffLt[9:12]
print("Los primeros tres elememntos son:" , fisrstThree)
print("Los últimos tres elementos son:" , lastThree)

# Programa 6 Eliminar la tupla foodStuffTp por completo
print("Programa 6")
del(foodStuffTp)
print("La tupla ya no existe")

# Programa 7 Comprobar si un elemento existe en una tupla
print("Programa 7")
nordicCountries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Tupla a comprobar:" , nordicCountries)

# Programa 7.1 Comprueba si 'Estonia' es un país nórdico
print("Programa 7.1")
if 'Estonia' in nordicCountries:
    print("Estonia es un país Nórdico")
else:
    print("Estonia no es un país Nórtdico")

# Programa 7.2 Comprueba si 'Iceland' es un país nórdico
print("Programa 7.2")
if 'Iceland' in nordicCountries:
    print("Islandia es un país Nórdico")
else:
    print("Islandia no es un país Nórtdico")
