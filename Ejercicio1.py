# Programa 1 Edad
edad = 18

# Programa 2 Altura
miAltura = 1.65

# Programa 3 Número complejo
n = 4 + 3j

# Programa 4 Área del Triángulo
base = float(input("Ingresa la base del triángulo "))
altura = float(input('Ingresa la altura del triángulo '))
area = 0.5 * base * altura 
print("El área del triángulo es " , area)

# Programa 5 Perímetro del triángulo
ladoA = float(input('Ingrese la medida del lado a '))
ladoB = float(input('Ingrese la medida del lado b '))
ladoC = float(input('Ingrese la medida del lado c '))
perimetro = ladoA + ladoB + ladoC
print('El perímetro del triángulo es ' , perimetro)

# Programa 6 Área y perímetro de un rectángulo
longitud = float(input("Ingrese la longitud del rectángulo "))
ancho = float(input("Ingrese el ancho del rectángulo "))
areaRectangulo = longitud * ancho
print('El área del rectánculo es ' , areaRectangulo)
perimetroRectangulo = 2 * (longitud + ancho)
print('El perímetro del rectángulo es ' , perimetroRectangulo)

# Programa 7 Radio de un círculo
radioCirculo = float(input("Ingrese el radio del círculo "))
pi = 3.14
areaCirculo = pi * radioCirculo * radioCirculo
print("El área del círculo es " , areaCirculo)
circunferenciaCirculo = 2 * pi * radioCirculo
print("La circunferencia del círculo es " , circunferenciaCirculo)

# Programa 8 Pendiente e intersecciones con eye x y y de y=2x-2
m = 2
b = -2
interseccionEnX = -b / m    # cuando y = 0, 0 = mx + b
interseccionEnY = b    # cuando x = 0, y = b
print("La pendiente de la recta es " , m)
print("La intersección de la recta con el eje x es " , interseccionEnX)
print("La intersección de la recta con el eje y es " , interseccionEnY)

# Programa 9 Pendiente y distancia euclidiana entre el punto (2, 2) y el punto (6, 10)
import math
x1 = 2
y1 = 2
x2 = 6
y2 = 10
pendiente = (y2 - y1) / (x2 - x1)
distanciaEuclidiana = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("La pendiente entre los puntos es " , pendiente)
print("La distancia euclidiana entre los puntos es " , distanciaEuclidiana)

# Programa 10 Comparación de las pendientes de los programas 8 y 9
m1 = m
m2 = pendiente
if m1 == m2:
    resultado = "las pendientes son iguales"
else:
    resultado = "Las pendientes son diferentes"
print("La pendiente de la recta y = 2x - 2 es: " , m1)
print("La pendiente entre los puntos (2, 2) y (6, 10) es: " , m2)
print(resultado)

# Programa 11 Valor de y para la ecuación y = x^2 + 6x + 9
def calcularY(x):
    return x**2 + 6*x + 9
valoresX = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
valoresY = {x: calcularY(x) for x in valoresX}
print("Valores de y para diferentes valores de x:")
for x, y in valoresY.items():
    print("x = {x}, y = {y}")
x_0 = None
for x, y in valoresY.items():
    if y == 0:
        x_0 = x
print("\nEl valor de x en el que y es 0 es: {x_0}")

# Programa 12 Longitud de python y dragon
pythonLen = len("python")
dragonLen = len("dragon")
comparacionFalsa = pythonLen < dragonLen
print("La longitud de 'python' es: " , pythonLen)
print("La longitud de 'dragon' es: " , dragonLen)
print("La afirmación falsa es: ¿La longitud de 'dragon' es mayor que la de 'python'? " , comparacionFalsa)

#Programa 13 Sílaba "on" en python y dragon
pythonContieneOn = 'on' in 'python'
dragonContieneOn = 'on' in 'dragon'
if pythonContieneOn and dragonContieneOn:
    resultado = "La sílaba 'on' se encuentra en ambas palabras"
else:
    resultado = "La sílaba 'on' no se encuentra en ambas palabras"
print(resultado)

# Programa 14 "jargon" en oración
oracion = "I hope this course is not full of jargon"
if "jargon" in oracion:
    resultado = "La palabra 'jargon' se encuentra en la oración"
else:
    resultado = "La parabra 'jargon' no se encuentra en la oración"
print(resultado)

# Programa 15 No hay "on" en python ni dragon
pythonSinOn = "on" not in "python"
dragonSinOn = "on" not in "dragon"
if pythonSinOn and dragonSinOn:
    resultado = "La sílaba 'on' no se encuentra en 'dragon' ni en 'python'"
else:
    resultado = "La sílaba 'on' se encuentra en al menos una de las palabras"
print(resultado)

# Programa 16 Longitud de python, castear a float y string
longitudPython = len("python")
longitudPythonFlotante = float(longitudPython)
longitudPythonString = str(longitudPythonFlotante)
print("La longitud del texto 'Python' es: " , longitudPython)
print("La longitud como flotante es: " , longitudPythonFlotante)
print("La longitud como string es: " , longitudPythonString)

# Programa 17 Números pares divisibles entre 2
def esPar(numero):
    if numero % 2 == 0:
        return True  
    else:
        return False  
numero = int(input("Ingresa un número: "))
if esPar(numero):
    print("El número" , numero , "es par")
else:
    print("El número" , numero ,  "no es par")

# Program 18 División del floor de 7 por 3 es igual al valor int convertido de 2.7
divisionFloor = 7 // 3
casteoEntero = int(2.7)
if divisionFloor == casteoEntero:
    resultado = "La división del floor de 7 por 3 es igual al valor entero de 2.7"
else:
    resultado = "La división del floor de 7 por 3 no es igual al valor entero de 2.7"
print("División del floor de 7 por 3: " , divisionFloor)
print("Valor entero de 2.7: " , casteoEntero)
print(resultado)

# Programa 19 Comprobar si el tipo de "10" es igual a tipo de 10
tipo10String = type("10")
tipo10Float = type(10)
if tipo10String == tipo10Float:
    resultado = "El tipo de '10' es igual al tipo de 10"
else:
    resultado = "El tipo de '10' no es igual al tipo de 10"
print("El tipo de '10' es: " , tipo10String)
print("El tipo de 10 es: " , tipo10Float)
print(resultado)

# Programa 20 Comprobar si int('9.8') es igual a 10
valorConvertido = int(float('9.8'))
if valorConvertido == 10:
    resultado = "int('9.8') es igual a 10"
else:
    resultado = "int('9.8') no es igual a 10"
print("int('9.8') convertido es: " , valorConvertido)
print(resultado)

# Programa 21 Salario de la persona
horas = float(input("Ingrese las horas trabajadas: "))
tarifaPorHora = float(input("Ingrese la tarifa por hora: "))
salario = horas * tarifaPorHora
print("El salario de la persona es de " , salario)

# Programa 22 Cantidad de segundos que puede vivir una persona 
años = int(input("Ingrese la cantidad de años: "))
segundosPorAño = 3600
segundosTotales = años * segundosPorAño
print("Una persona que viva " , años , "años puede vivir " , segundosTotales , "segundos")



