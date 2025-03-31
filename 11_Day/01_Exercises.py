# PROGRAMAS DÍA 11
print("PROGRAMAS DÍA 11")
print(" ")

# Ejercicios: Nivel 1
print("Ejercicios: Nivel 1")
print(" ")


# Programa 1 
# Declare a function add_two_numbers. It takes two parameters and it returns a sum.
print("Programa 1")
def addTwoNumbers ():
    n1 = 5
    n2 = 4
    total = n1 + n2
    return total
print("El total es:" , addTwoNumbers()) 


# Programa 2
# Area of a circle is calculated as follows: area = π x r x r. 
# Write a function that calculates area_of_circle.
print("Programa 2")
import math
def areaOfCircle ():
    radio = 5
    area = math.pi * radio ** 2
    return area
print("El área del círculo con radio 5 es:" , areaOfCircle())


# Programa 3 
# Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. 
# Check if all the list items are number types. 
# If not do give a reasonable feedback.
print("Programa 3")
def addAllNums(*args):
    if all(isinstance(num,(int , float)) for num in args):
        return sum(args)
    else:
        return "Error: Los argumentos deben ser números"
print(addAllNums(1 , 2 , 3 , 4 , 5 , 6))
print(addAllNums("string" , 1 , 2 , 3))


# Programa 4
# Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. 
# Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
print("Programa 4")
def convertCelToFa (celsius):
    farenheit = (celsius * 9 / 5) + 32
    return farenheit
print("La temperatura en Farenheit es:" , convertCelToFa(35))


# Programa 5
# Write a function called check-season. 
# It takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
print("Programa 5")
def checkSeason (month):
     if month in ['January','February','March']:
        return 'Winter'
     elif month in ['April','May','June']:
        return 'Spring'
     elif month in ['July','August','September']:
        return 'Summer'
     else:
        return 'Otoño'
print("La temporada de August es:" , checkSeason(month = 'August'))


# Programa 6 
# Write a function called calculate_slope which return the slope of a linear equation
print("Programa 6")
print("x1 = 4")
print("x2 = 2")
print("y1 = 6")
print("y2 = 2")
def calculateSlope (x1, x2, y1, y2):
    m = (y2 - y1) / (x2 - x1)
    return m
print("La pendiente es:" , calculateSlope(4 , 2 , 6 , 2))


# Programa 7 
# Quadratic equation is calculated as follows: ax² + bx + c = 0. 
# Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
print("Programa 7")
print("a = 1")
print("b = 6")
print("c = 9")
def solveQuadraticEqn (a, b, c):
     d = b ** 2 - 4 * a * c
     if d > 0:
        x1 = (- b + d ** 0.5) / (2 * a)
        x2 = (- b - d ** 0.5) / (2 * a)
        return x1, x2
     elif d==0:
        x = - b / (2 * a)
        return x
     else:
        return 'No hay solución'
print("La solucuión de la ecuación es:" , "x =" , solveQuadraticEqn(1 , 6 , 9))


# Programa 8
# Declare a function named print_list. 
# It takes a list as a parameter and it prints out each element of the list.
print("Prohgrama 8")
def printList (list):
    for item in list:
        print(item)
drinks = ["milk" , "water" , "soda" , "juice"]
print("La lista es" )
printList (drinks)


# Programa 9 
# Declare a function named reverse_list. 
# It takes an array as a parameter and it returns the reverse of the array (use loops).
print("Programa 9")
fruits = ["lemon" , "strawberry" , "watermelon" , "orange"]
print("Lista:" , fruits)
def reverseList(array):
    reverseArray=[]
    for item in array:
        reverseArray.insert(0, item)
    return reverseArray
print("Lista invertida:" , reverseList(fruits))


# Programa 10
# Declare a function named capitalize_list_items. 
# It takes a list as a parameter and it returns a capitalized list of items
print("Programa 10")
countries = ["Mexico" , "Germany" , "Ireland" , "Italy" , "Japan"]
print("Lista:" , countries)
def capitalizeListItems (list): 
     return [item.upper() for item in list]
print("Elementos de la lista en mayúsculas:" , capitalizeListItems(countries))


# Programa 11
# Declare a function named add_item. 
# It takes a list and an item parameters. 
# It returns a list with the item added at the end.
print("Programa 11")
def addItem (list, item):
    list.append(item)
    return list
print("Nueva lista:" , addItem(drinks , 'coffee'))


# Programa 12
# Declare a function named remove_item. 
# It takes a list and an item parameters. 
# It returns a list with the item removed from it.
print("Programa 12")
def removeItem (list, item):
    list.remove(item)
    return list
print("La nueva lista es:" , removeItem(fruits , "watermelon"))


# Programa 13
# Declare a function named sum_of_numbers. 
# It takes a number parameter and it adds all the numbers in that range.
print("Programa 13")
def sumOfNumbers (number):
    sum = 0
    for i in range(1, number + 1):
        sum = sum + i
    return sum
print("Suma de los números del rango 10:" , sumOfNumbers(10))


# Programa 14
# Declare a function named sum_of_odds. 
# It takes a number parameter and it adds all the odd numbers in that range.
print("Programa 14")
def sumOfOdds (number):
    odds = 0
    for i in range(number + 1):
        if i%2 == 1:
            odds += i
    return odds
print("Suma de los números impares del rango 10:" , sumOfOdds(10))


# Programa 15
# Declare a function named sum_of_even. 
# It takes a number parameter and it adds all the even numbers in that range.
print("Programa 15")
def sumOfEven (number):
    even=0
    for i in range(number + 1):
        if i%2 == 0:
            even += i
    return even
print("Suma de los números pares del rango 10:" , sumOfEven(10))
