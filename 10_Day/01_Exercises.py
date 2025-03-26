# PROGRAMAS DÍA 10

# Ejercicios: Nivel 1
print("Ejercicios: Nivel 1")

# Programa 1
# Iterate 0 to 10 using for loop, do the same using while loop.
print("Programa 1")
print("for loop")
for i in range(11):
    print(i)
print("while Loop")
i = 0
while i < 11:
    print(i)
    i += 1

# Programa 2
# Iterate 10 to 0 using for loop, do the same using while loop.
print("Programa 2")
print("for loop")
for i1 in range(10, -1, -1):
    print(i1)
print("while loop")
i1 = 10
while i1 >= 0:
    print(i1)
    i1 = i1 - 1

# Programa 3
# Write a loop that makes seven calls to print(), so we get on the output the following triangle:
print("Programa 3")
print("Usando foor loop")
for n in range(1,8):
    print("#" * n)
print("Usando while loop")
n = 1
while n <= 7:
    print("#" * n)
    n = n + 1

# Programa 4
# Use nested loops to create the following:
print("Programa 4")
m = 8
n = 8
for j in range(m):
    for i in range(n):
        print("#", end=" ")
    print()

# Programa 5
# Print the following pattern:
print("Programa 5")
for t in range(11):
    print(t , "x" , t , "=" , t * t)

# Programa 6 
# Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
print("Programa 6")
list = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for item in list:
    print(item)

# Programa 7 
# Use for loop to iterate from 0 to 100 and print only even numbers
print("Programa 7")
for e in range(101):
    if (e % 2 == 0):
        print(e)

# Programa 8 
# Use for loop to iterate from 0 to 100 and print only odd numbers
print("Programa 8")
for o in range(100):
    if (o % 2 == 0):
        o = o + 1
        print(o)
        