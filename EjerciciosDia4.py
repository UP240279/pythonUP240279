## PROGRAMAS DÍA 4

# Programa 1 Concatena la cadena 'Thirty', 'Days', 'Of' 'Python' en una sola cadena, 'Thirty Days Of Python'
print("Programa 1")
primeraPalabra = "Thirty"
segundaPalabra = "Days"
terceraPalabra = "Of"
cuartaPalabra = "Python"
espacio = " "
cadena1 = primeraPalabra + espacio + segundaPalabra + espacio + terceraPalabra + espacio + cuartaPalabra
print(cadena1)

# Programa 2 Concatenar la cadena 'Coding', 'For' , 'All' en una sola cadena, "Coding For All"
print("Programa 2")
palabra1 = "Coding"
palabra2 = "For"
palabra3 = "All"
cadena2 = palabra1 + espacio + palabra2 + espacio + palabra3
print(cadena2)

# Programa 3 Declare una variable llamada company y asígnele un valor inicial "Coding For All"
print("Programa 3")
company = "Coding For All"

# Programa 4 Imprima la variable empresa utilizando print()
print("Programa 4")
print(company)

# Programa 5 Imprima la longitud de la cadena de la empresa utilizando el método len() y print()
print("Programa 5")
lenCompany = len(company)
print(lenCompany)

# Programa 6 Cambie todos los caracteres a letras mayúsculas utilizando el método upper()
print("Programa 6")
mayCompany = company.upper()
print(mayCompany)

# Programa 7 Cambie todos los caracteres a letras minúsculas utilizando el método lower()
print("Programa 7")
minCompany = company.lower()
print(minCompany)

# Programa 8 Utilice los métodos capitalize(), title(), swapcase() para formatear el valor de la cadena Coding For All
print("Programa 8")
print(company.capitalize())
print(company.title())
print(company.swapcase())

# Programa 9 Recortar (slice) la primera palabra de la cadena "Coding For All"
print("Programa 9") 
primPal = company[0:6]
print(primPal)

# Programa 10 Compruebe si la cadena Coding For All contiene una palabra "Coding" utilizando el método index, find u otros
print("Programa 10")
print(company.find("Coding"))
subcadena = "Coding"
print(company.index(subcadena))
print("La cadena sí contiene la palabra 'Coding' en el índice 0")

# Programa 11 Reemplace la palabra 'Coding' en la cadena 'Coding For All' por Python
print("Programa 11")
print(company.replace("Coding" , "Python"))

# Programa 12 Cambie Python for All a Python for Everyone utilizando el método de replace u otros métodos
print("Programa 12")
print(company.replace("Coding For All" , "Python for Everyone"))

# Programa 13 Divida la cadena 'Coding For All' usando el espacio como separador (split())
print("Programa 13")
print(company.split( ))

# Programa 14 "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" divide la cadena en la coma
print("Programa 14")
programas = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(programas.split(", "))

# Programa 15 ¿Cuál es el caracter en el índice 0 en la cadena "Coding For All"?
print("Programa 15")
print("El caracter en el índice 0 de la cadena es" , company[0])

# Programa 16 ¿Cuál es el último índice de la cadena "Coding For All"?
print("Programa 16")
print("El último índice de la cadena es" , company[-1])

# Programa 17 ¿Qué caracter está en el índice 10 en la cadena "Coding For All"?
print("Programa 17")
print("El caracter en el índice 10 es" , company[10])
print("(El caracter 10 es un espacio)")

# Programa 18 Crea un acrónimo o una abreviatura para el nombre 'Python For Everyone'
print("Programa 18")
nombre = 'Python For Everyone'
acronimo = nombre.split()
print(acronimo[0][0] + acronimo[1][0] + acronimo[2][0])

# Programa 19 Crea un acrónimo o una abreviatura para el nombre 'Coding For All'
print("Programa 19")
nombre2 = 'Coding For All'
acronimo2 = nombre2.split()
print(acronimo2[0][0] + acronimo2[1][0] + acronimo2[2][0])

# Programa 20 Utilice el index para determinar la posición de la primera aparición de C en 'Coding For All'
print("Programa 20")
print(company.index("C"))

# Programa 21 Utilice el index para determinar la posición de la primera aparición de F en 'Coding For All'
print("Programa 21")
print(company.index("F"))

# Programa 22 Utilice rfind para determinar la posición de la última aparición de l en 'Coding For All People'
print("Programa 22")
oracion = "Coding For All People"
print(oracion.rfind("l"))

# Programa 23 Utilice index o find para encontrar la posición de la primera aparición de la palabra 'because' en la siguiente oración:
# 'You cannot end a sentence with because because because is a conjunction'
print("Programa 23")
sentence = 'You cannot end a sentence with because because because is a conjunction'
sentenceSplit = sentence.split( )
print(sentenceSplit.index("because"))

# Programa 24 Utilice rindex para encontrar la posición de la primera aparición de la palabra 'because' en la siguiente oración:
# 'You cannot end a sentence with because because because is a conjunction'
print("Programa 24")
word = "because"
print(sentenceSplit.rindex(word))



