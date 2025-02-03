#Ejemplo de iterador

#Crear lista

my_list = [1,2,3,4]

#Obtener iterador
my_iter = iter(my_list)

print(my_iter)

#Usar el iterador
#Next nos va a ayudar a que podamos ir viendo los valores que se van guardando en memoria
#En resumen, nos imprime un elemento de la lista a la vez por cada print que hagamos
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

#En este caso lo podemos ejecutar 4 veces porque la lista solo tiene 4 elementos, 
# si se interna una quinta vez da un error de iteración