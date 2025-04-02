## Ejercicios: Nivel 2
print("Ejercicios: Nivel 2")

# Sets
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
print("Set 1:" , A)
print("Set 2:" , B)

# Programa 1 
# Unir A y B
print("Programa 1")
union = A.union(B)
print(union)

# Programa 2 
# Encuentra la intersección de A y B
print("Programa 2")
intersection = A.intersection(B)
print(intersection)

# Programa 3 
# Es A un subset de B
print("Programa 3")
subset = A.issubset(B)
print(subset)

# Programa 4 
# ¿Son A y B sets disjuntos?
print("Programa 4")
disjoint = A.isdisjoint(B)
print(disjoint)

# Programa 5 
# Unir A con B y B con A
print("Programa 5")
unionAB = A.union(B)
print("Unión AB:" , unionAB)
unionBA = B.union(A)
print("Unión BA:" , unionBA)

# Programa 6 
# ¿Cuál es la diferencia simétrica entre A y B?
print("Programa 6")
symmetricDifference = A.symmetric_difference(B)
print(symmetricDifference)

# Programa 7 
# Eliminar los sets por completo
print("Programa 7")
del A
del B
print("Los sets ya no existen")

print("revisado")