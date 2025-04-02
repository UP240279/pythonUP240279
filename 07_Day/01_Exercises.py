## PROGRAMAS DÍA 7

# Ejercicios: Nivel 1
print("Ejercicios: Nivel 1")

# Sets
itCompanies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print("Set:" , itCompanies)

# Programa 1 
# Encuentra la longitud del set itCompanies
print("Programa 1")
print("Longitud:" , len(itCompanies))

# Programa 2 
# Añade 'Twitter' a itCompanies
print("Programa 2")
itCompanies.add("Twitter")
print(itCompanies)

# Programa 3 
# Insertar varias empresas de TI a la vez en el set itCompanies
print("Programa 3")
itCompanies.update(["Intel", "Tesla", "Samsung", "Adobe"])
print(itCompanies)

#Programa 4 
# Eliminar una de las empresas del set itCompanies
print("Programa 4")
itCompanies.remove("Apple")
print(itCompanies)

# Programa 5 
# ¿Cuál es la diferencia entre eliminar y descartar? (remove y discard)
print("Programa 5")
itCompanies.remove("Intel")
print("Si el elemento no existe en el set, el comando remove generará error")
itCompanies.discard("Oracle")
print("Si el elemento no existe en el set, el comando discard no gererará ningún error")
print(itCompanies)
print("revisado")