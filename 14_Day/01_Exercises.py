# PROGRAMAS DÍA 14
print("PROGRAMAS DÍA 14")
print(" ")

# Ejercicios: Nivel 1
print("Ejercicios: Nivel 1")
print(" ")


# Programa 1
# Explain the difference between map, filter, and reduce.
print("Programa 1")
mapFunction = "Toma una función y un iterable como parámetros. Devuelve un iterable con los elementos transformados."
filterFunction = "Filtra los elementos de un iterable según una condición (devuelve True o False). Devuelve un iterable con los elementos que cumplen la condición"
reduceFunction = "Acumula o reduce los elementos de un iterable a un solo valor mediante una función. No devuelve otro iterable, sino un único valor"
print("map:" , mapFunction)
print("filter:" , filterFunction)
print("reduce:" , reduceFunction)


# Programa 2
# Explain the difference between higher order function, closure and decorator.
print("Programa 2")
higherOrderFunction = "Puede tomar una o más funciones como parámetros, puede ser devuelta como resultado de otra función, se puede modificar, se puede asignar una función a una variable"
closureFunction = "Es una función que 'recuerda' las variables de su entorno externo incluso después de que la función externa termine su ejecución."
decoratorFunction = "Patrón de diseño que permite añadir nuevas funciones a un objeto existente sin modificar su estructura. Toma una función como argumento, le agrega funcionalidad y devuelve una nueva función."
print("higher order function:" , higherOrderFunction)
print("closure:" , closureFunction)
print("decorator:" , decoratorFunction)


# Programa 3
# Define a call function before map, filter or reduce, see examples.
print("Programa 3")
def double(x):
    return x * 2
numbers = [1, 2, 3, 4, 5]
print("Lista de números:" , numbers)
doubledNumbers = map(double, numbers)
print("Lista del doble de los números:" , list(doubledNumbers))


# Programa 4
# Use for loop to print each country in the countries list.
print("Programa 4")
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
print("Países en la lista:")
for country in countries:
    print(country)


# Programa 5
# Use for to print each name in the names list.
print("Programa 5")
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
print("Nombres en la lista:")
for name in names:
    print(name)


# Programa 6
# Use for to print each number in the numbers list.
print("Programa 6")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Números en la lista:")
for number in numbers:
    print(number)
print("Revisado")