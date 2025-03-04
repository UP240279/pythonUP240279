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

# Programa 9 Recortar (slice) la primera palabra de la cadena Coding For All
print("Programa 9")
primPal = company[0:6]
print(primPal)

# Programa 10 Compruebe si la cadena Coding For All contiene una palabra Coding utilizando el método index, find u otros
print("Programa 10")
print(company.find("Coding"))
subcadena = "Coding"
print(company.index(subcadena))

# Programa 11 Reemplace la palabra 'Coding' en la cadena 'Coding For All' por Python
print("Programa 11")
print(company.replace("Coding" , "Python"))

# Programa 12 Cambie Python for All a Python for Everyone using the replace method or other methods
print("Programa 12")
print(company.replace("Python for All" , "Python for Everyone"))


