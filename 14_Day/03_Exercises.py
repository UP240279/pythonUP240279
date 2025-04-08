# Ejercicios: Nivel 3
print("Ejercicios: Nivel 3")
print(" ")


# Programa 1 
# Use the countries_data.py and follow the tasks below:

import countries_data as datac
data = datac.countries


# Programa 1.1
# Sort countries by name, by capital, by population.
print("Programa 1.1")

print("Por nombre:")
sortedByName = sorted(data, key = lambda x: x["name"])
for country in sortedByName:
    print(country["name"])

# Ordenar por capital
print("Por capital:")
sortedByCapital = sorted(data, key = lambda x: x["capital"])
for country in sortedByCapital:
    print(country["capital"])

# Ordenar por población
print("Por población")
sortedByPopulation = sorted(data, key = lambda x: x["population"])
for country in sortedByPopulation:
    print(country['name'] , "Población:" , country['population'])


# Programa 1.2
# Sort out the ten most spoken languages by location.
print("Programa 1.2")
sortedLanguages = sorted(data, key=lambda x: x["population"], reverse = True)
print("Los 10 idiomas más hablados por ubicación:")
top10Spoken = sortedLanguages[:10]
for language in top10Spoken:
    print(language['languages'] , ({language['name']}) , "lo hablan:" ,  language['population'] , "habitantes")


# Programa 1.3
# Sort out the ten most populated countries.
print("Programa 1.3")
sortedCountries = sorted(data, key=lambda x: x["population"], reverse=True)
top10Populated = sortedCountries[:10]
print("Los 10 países más poblados son:")
for country in top10Populated:
    print(country["name"]) , country["population"]

print("Revisado")