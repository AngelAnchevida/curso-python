a = [1,2,3,4,5]
b = a
print(a)
print(b)

#Todas las acciones que se hagan en a, afectarán a b porque
#apuntan al mismo espacion en memoria
del a[0]
print(id(a))
print(id(b))

#Si le damos a una variable el valor de una lista de esta manera
#podemos hacer que tenga otro espacio en memoria y las modificaciones
#siguientes a la lista original no afectarán a esta
c = a[:]

print(id(a))
print(id(b))
print(id(c))

a.append(6)

print(a)
print(b)
print(c)