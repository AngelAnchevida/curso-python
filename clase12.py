numbers = [1,2,3,4,5,6]

for i in numbers:
    print("Aquí i es igual a:",i)

#Esto imprime numeros del 0 al 10, puedes modiicar el inicio y final
for i in range(10):
    print(i)

fruits = ["manzana", "pera", "uva","naranja","tomate"]
for fruit in fruits:
    print(fruit)
    if fruit == "naranja":
        print("Naranaja encontrada")



x = 0

while x < 5:
    if x == 3:
        break
    print(x)
    x += 1


numbers = [1,2,3,4,5,6]

for i in numbers:
    if i == 3:
        break        
    print("Aquí i es igual a:",i)
