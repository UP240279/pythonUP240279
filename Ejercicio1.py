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

#Programa 13 sílaba on en python y dragon
pythonContieneOn = 'on' in 'python'
dragonContieneOn = 'on' in 'dragon'
if pythonContieneOn and dragonContieneOn:
    resultado = "La sílaba 'on' se encuentra en ambas palabras"
else:
    resultado = "La sílaba 'on' no se encuentra en ambas palabras"
print(resultado)
