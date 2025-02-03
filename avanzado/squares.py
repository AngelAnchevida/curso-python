#Manera clásica pero lenta
numbers = [1, 2, 3, 4, 5]

squares = []

for number in numbers:
    square = number ** 2
    squares.append(square)

print(squares)

#Manera rápida
numbers = [1, 2, 3, 4, 5]

#List comprension
#Podemos usar un for u otra condicional para crear la lista
squares = [x**2 for x in numbers]
print(squares)

