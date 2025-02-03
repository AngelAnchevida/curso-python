#Crear iterador para los numeros impares
#Se puede modificar para que muestra pares

#Limite
limit = 10

#Crear iterador
odd_itter = iter(range(1, limit + 1, 2))
#Solo muestra los impares porque el salto está cada dos numeros
# y empieza en 1 que es impar

#Usar iterador
for num in  odd_itter:
    print(num)