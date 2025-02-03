numbers = {1:"uno", 2:"dos",3:"tres"}

print(numbers)
print(numbers[2])

information = {"nombre": "Angel",
                "Apellido": "Anchevida",
                "Altura": 1.61,
                "Edad": 24
                }
print(information)
del information["Edad"]
print(information)


claves = information.keys()
print(claves)
#Obtenemos las claves de information
print(type(claves))
#Es de tipo diccionario

values = information.values()
print(values)

pairs = information.items()
print(pairs)
#Devuelve en tuplas el valor


#Diccionario de diccionarios
contacts = {"Angel":{"Apellido": "Anchevida",
                "Altura": 1.61,
                "Edad": 24
                },
                "Diego":{"Apellido": "Antezana",
                "Altura": 1.75,
                "Edad": 34
                }}
print(contacts)
print(contacts["Angel"])