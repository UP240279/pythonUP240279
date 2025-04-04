# PROGRAMAS DÍA 15
print("PROGRAMAS DÍA 15")
print(" ")


# Programa 1
# Open you python interactive shell and try all the examples covered in this section.
print ("Programa 1: Ejemplos")

# Ejemplo 1
# SyntaxError
print("Ejemplo 1: SyntaxError")
# print"Hola mundo"    # Error: Faltan los paréntesis para que se pueda imprimir.
print('Hola mundo')    


# Ejemplo 2
# NameError
print("Ejemplo 2: NameError")
# print(age)     # Error: No está definida la variable.
age = 18
print(age)


# Ejemplo 3
# IndexError
print("Ejemplo 3: IndexError")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(numbers[10])     # Error: El índice está fuera de rango.
print(numbers[9])


# Ejemplo 4
# ModuleNotFoundError
print("Ejemplo 4: ModuleNotFoundError")
# import maths     # Error: No hay módulo llamado 'maths'.
import math


# Ejemplo 5
# AttributeError
print("Ejemplo 5: AttributeError")
# pi = math.PI     # Error: 'math' no tiene atributo 'PI'.
pi = math.pi
print(pi)


# Ejemplo 6
# KeyError
print("Ejemplo 6: KeyError")
user = {'name':'Vanessa', 'age':18, 'country':'Mexico'}
# print(user['county'])     # Error: La clave es incorrecta (no está bien escrito).
print(user["country"])


# Ejemplo 7
# TypeError
print("Ejemplo 7: TypeError")
# print(5 + "7")     # Error: No se puede sumar un entero y una cadena.
print(5 + int("7"))


# Ejemplo 8
# ImportError
print("Ejemplo 8: ImportError")
# from math import power     # Error: No existe "power" en "math".
from math import pow
print(pow(4, 5))


# Ejemplo 9
# ValueError
print("Ejemplo 9: ValueError")
# print(int("34c"))     # Error: "34c" no es un número válido porque tiene la letra "c".
print(int("34"))


# Ejemplo 10
# ZeroDivisionError
print("Ejemplo 10: ZeroDivisionError")
# print(2 / 0)     # Error: No se puede dividir por 0.
print(2 / 1)
