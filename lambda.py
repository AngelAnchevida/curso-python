add = lambda a, b: a + b
print(add(10,4))


multiply = lambda a, b: a * b
print(multiply(10,4))


#Cuadrado de cada número
numbers = range(11)
numeros = (1,2,3,4,5,6,7,8,9,10)

print(numbers)

squared_numbers = list(map(lambda x: x**2, numbers))
#list(map(lambda x: formula, lista))
#Crea una lista con una condicional lambda a partir de un objeto interable


print("Cuadrados:", squared_numbers)

#Pares
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Pares:", even_numbers)

