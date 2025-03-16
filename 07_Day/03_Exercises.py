## Ejercicios: Nivel 3
print("Ejercicios: Nivel 3")

# Sets
age = [22, 19, 24, 25, 26, 24, 25, 24]
print("Lista:" , age)

# Programa 1 Convierte las edades en un set y compara la longitud de la lista y el set, ¿cuál es más grande?
print("Programa 1")
ages = set(age)
print(ages)
print("Longitud del set" , len(ages))
print("Longitud de la lista:" , len(age))
if len(ages) > len(age):
    print("La longitud del set es más grande")
else:
    print("La longitud de la lista es más grande")

# Programa 2 Explique la diferencia entre los siguientes tipos de datos: cadena, lista, tupla y set
print("Programa 2")
print ("La cadena se encierra solo entre comillas y no se puede modificar después de ser creada")
print("'Ejemplo de cadena'")
print("La lista es un conjunto de elementos entre corchetes, se pueden cambiar, agregar y eliminar elementos")
print([1, 2, 3, 3, 5])
print("La tupla es similar a la lista, se encierra entre paréntesis y no se pueden modificar los elementos")
print((1, 2, 3, 3, 5))
print("El set es un conjunto de elementos que no se repiten pero sí se pueden modificar, se encierra entre llaves")
print({1, 2, 3, 5})

# Programa 3 ¿Cuántas palabras únicas se han usado en la oración? Usa los métodos de split y set para obtener las palabras únicas.
print("Programa 3")
sentence = "I am a teacher and I love to inspire and teach people"
print(sentence)
words = sentence.split()
uniqueWords = set(words)
print("Palabras únicas:" , len(uniqueWords) , uniqueWords)

