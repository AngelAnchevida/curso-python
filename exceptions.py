try:
    divisor = int(input("Ingresa un numero divisor: "))
    result = 100/divisor
    print(result)
except Exception as EXCEP:
    print("Error:",EXCEP)
#Este sirve para todos lo errores que existem
except ZeroDivisionError as e:
    print("Error: El divisor no puede ser 0")
    print("Ha ocurrido un error: ", e)
except ValueError:
    print("Error: Debes introducir un número válido")