import random

#Generar un numero entero aleatorio
random_number = random.randint(1,10)
print(random_number)

#Elegir colores aleatorios
colors = ['rojo','azul','verde']

random_color = random.choice(colors)#Elige aleatoriamente un elemento de una lista
print(random_color)


#Barajar una lista de cartas
cartas = ['AS', 'Rey', 'Reyna', 'Jota', '10']
random.shuffle(cartas)#Revuelve aleatoriamente una lista
print(cartas)