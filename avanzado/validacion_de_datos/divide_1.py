def divide(a: int, b: int) -> float:
    #Validar que ambos parametros sean enteros
    if not isinstance(a, int) or not isinstance(b, int):
        # print("Error:  ambos parametros deben ser enteros o flotantes")
        # return None
        raise TypeError("Ambos parámetros deben ser enteros.")
    
    #Verificamos que el divisor no sea 0
    if b == 0:
        # print("Error el divisor no puede ser 0")
        # return None
        raise ValueError("El divisor no puede ser 0.")
    
    return a/b

# res_1 = divide(10, '2')
#res_2 = divide(10,0)
#res_3 = divide(10,2)
#print(res_3)


#Ejemplo de uso
try:
    res = divide(10,'2') #Error de tipo
    print(res)
except TypeError as e:
    print(f"Error: {e}")

#Ejemplo de uso
try:
    res = divide(10, 0) #Error de división por cero
    print(res)
except ValueError as e:
    print(f"Error: {e}")

#Ejemplo de uso
try:
    res = divide(10, 2) 
    print(res)
except (ValueError, TypeError) as e:
    print(f"Error: {e}")