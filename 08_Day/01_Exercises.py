## PROGRAMAS DÍA 8 

# Programa 1 
# Create an empty dictionary called dog
print("Programa 1")
dog = {}
print(len(dog))

# Programa 2 
# Add name, color, breed, legs, age to the dog dictionary
print("Programa 2")
dog = {
    "name" : "Dante",
    "color" : "Gray",
    "breed" : "Schnauzer",
    "legs" : 4,
    "age" : 6
}
print(dog)

# Programa 3 
# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    "firstName" : "Vanessa",
    "lastName" : "Ríos",
    "gender" : "Female",
    "age" : 18,
    "maritalSatatus" : "Single",
    "skills" : ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    "country" : "México",
    "city" : "Aguascalientes",
    "address" : {
        "sreet" : "Red street",
        "zipcode" : "20209"
    }
}
print(student)

# Programa 4 
# Get the length of the student dictionary
print("Programa 4")
print(len(student))

# Programa 5 
# Get the value of skills and check the data type, it should be a list
print("Programa 5")
skillsValue = student["skills"]
print(skillsValue)
print(type(skillsValue))

# Programa 6 
# Modify the skills values by adding one or two skills
print("Programa 6")
student["skills"].append('HTML')
student["skills"].append('CSS')
print(student)

# Programa 7 
# Get the dictionary keys as a list
print("Programa 7")
keysList = student.keys()
print("Keys:" , keysList)

# Programa 8 
# Get the dictionary values as a list
print("Programa 8")
valuesList = student.values()
print("Values:" , valuesList)

# Programa 9 
# Change the dictionary to a list of tuples using items() method
print("Programa 9")
tuples = student.items()
print("Tuples:" , tuples)

# Programa 10 
# Delete one of the items in the dictionary
print("Programa 10")
student.popitem()
print(student)

# Programa 11 
# Delete one of the dictionaries
print("Programa 11")
del dog
print("El diccionario 'dog' ya no existe")

print("revisado")