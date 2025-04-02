## PROGRAMAS DÍA 6

#Ejercicios: Nivel 1
print("Ejercicios: Nivel 1")

# Programa 1 
# Crear una tupla vacía
print("Programa 1")
emptyTuple = tuple()
print(len(emptyTuple))

# Programa 2 
# Crea una tupla que contenga los nombres de tus hermanas y tus hermanos
print("Programa 2")
brothers = ("Gabriel", "Orlando", "Paulo")
print(brothers)
sisters = ("Montse", "Mariel", "Ivonne")
print(sisters)

# Programa 3 
# Unir tuplas de hermanos y hermanas y asignarlas a hermanos
print("Programa 3")
siblings = brothers + sisters
print(siblings)

# Programa 4 
# ¿Cuántos hermanos tienes?
print("Programa 4")
print("La cantidad de hermanos que tengo es:" , len(siblings))

# Programa 5 
# Modifica la tupla de hermanos y agrega el nombre de tu padre y madre y asígnalo a familyMembers
print("Programa 5")
parents = ("Adriana", "Carlos")
familyMembers = siblings + parents
print(familyMembers)
print("revisado")