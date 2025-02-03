to_do = ["Dirigirnos al hotel", 
        "Ir a almorzar",
        "Ir al museo",
        "Volver al hotel"]

print(to_do)

numbers = [1,2,3,4,"cinco"]
print(type(numbers))
mix = ["uno",2, 3.14, True, [1,2,3]]
print(mix)

print(len(mix))
print("Primer elemento:", mix[0])
print("Segundo elemento:", mix[1])
print("Ultimo elemento:", mix[-1])

string = "Hola Mundo"

print("Primer elemento:", string[0])
print("Segundo elemento:", string[1])
print("Ultimo elemento:", string[-1])

print(mix[0:2])
print(mix[:2])
print(mix[2:])
print(mix[1:4])
print(mix[0:])


#append agrega al final de la lista
mix.append(False)
print(mix)

#Puedes agregar cualquier tipo de dato
mix.append(["a","b"])
print(mix)

#Con insertar podemos dar la posición donde queremos hacer el insert y luego el dato
mix.insert(1,["a","b"])
print(mix)

#Con index podemos buscar la posición donde está el elemento, si el elemento
#se repite va a devolver la primera aparición del elemento
print(mix.index(["a","b"]))

numbers = [1,2,100.01,3,90.45,4,5]
print(numbers)
#Con max y min puedes encontrar
print("Mayor:", max(numbers))
print("Menor:", min(numbers))

#Podemos eliminar una porción de la lista o la lista completa
del numbers[-1]
print(numbers)
del numbers[:2]
print(numbers)
del numbers