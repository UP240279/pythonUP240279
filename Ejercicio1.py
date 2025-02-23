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
print("La pendiente entre los punros es " , pendiente)
print("La distancia euclidiana entre los puntos es " , distanciaEuclidiana)


