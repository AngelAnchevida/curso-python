#Suma todos los numeros que le pasemos a la funcion
def sum_numbers(*args):
    return sum(args)


print(sum_numbers(1,2,3,4,5)) #No son argumentos posicionales, son tuplas

print(sum_numbers(1,2))

print(sum_numbers(1,2,3,4,5,7,8,9))

