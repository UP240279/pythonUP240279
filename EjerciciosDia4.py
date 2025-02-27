## PROGRAMAS DÍA 4

# Programa 1 Concatena la cadena 'Thirty', 'Days', 'Of' 'Python' en una sola cadena, 'Thirty Days Of Python'.
primeraPalabra = "Thirty"
segundaPalabra = "Days"
terceraPalabra = "Of"
cuartaPalabra = "Python"
espacio = " "
cadena1 = primeraPalabra + espacio + segundaPalabra + espacio + terceraPalabra + espacio + cuartaPalabra
print(cadena1)

# Programa 2 Concatenar la cadena 'Coding', 'For' , 'All' en una sola cadena, "Coding For All".
palabra1 = "Coding"
palabra2 = "For"
palabra3 = "All"
cadena2 = palabra1 + espacio + palabra2 + espacio + palabra3
print(cadena2)

# Programa 3 Declare una variable llamada company y asígnele un valor inicial "Coding For All"
company = "Coding For All"

# Programa 4 Imprima la variable empresa utilizando print()
print(company)

# Programa 5 Imprima la longitud de la cadena de la empresa utilizando el método len() y print()
lenCompany = len(company)
print(lenCompany)

# Programa 6 Cambie todos los caracteres a letras mayúsculas utilizando el método upper()
mayCompany = company.upper()
print(mayCompany)

# Programa 7 Cambie todos los caracteres a letras minúsculas utilizando el método lower()
minCompany = company.lower()
print(minCompany)

# Programa 8 Utilice los métodos capitalize(), title(), swapcase() para formatear el valor de la cadena Coding For All
print(company.capitalize())
print(company.title())
print(company.swapcase())

# Programa 9 Recortar (slice) la primera palabra de la cadena Coding For All
primPal = company[0:6]
print(primPal)

# Programa 10 Compruebe si la cadena Coding For All contiene una palabra Coding utilizando el método index, find u otros
print(company.find("Coding"))
subcadena = "Coding"
print(company.index(subcadena))

# Programa 11 Reemplace la palabra 'Coding' en la cadena 'Coding For All' por Python
print(company.replace("Coding" , "Python"))

# Programa 12
