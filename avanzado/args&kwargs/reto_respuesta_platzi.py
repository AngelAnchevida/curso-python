"""
Crear una función que reciba una cantidad variable de productos y sus precios, 
calcule el total y aplique un descuento opcional si se proporciona como un argumento con nombre.


1. Usar args para recibir una lista de precios

2. Usar kwargs para aceptar un descuento opcional y aplicarlo al total.

""" 

def calcular_total(*args, **kwargs) -> float:
    total = 0 # Variable para llevar el total de la orden
    # Recorrer la lista de diccionarios de producto, cantidad y precio
    for p in args[0]:
        total += (p['cant'] * p['precio'])
    #Validar si hay descuento
    for key, value in kwargs.items():
        print(f'{key}: {value}')
        if key == 'descuento':
            total = total - (total * value/100)
    return total

# Ejemplo de uso

# Creo una orden, que sería un diccionario de productos con sus cantidades y precios
orden = [
    {'nombre': 'lapiz', 'cant': 2, 'precio': 3},
    {'nombre': 'cuaderno', 'cant': 5, 'precio': 5},
    {'nombre': 'compas', 'cant': 1, 'precio': 10},
    {'nombre': 'regla', 'cant': 1, 'precio': 2},
    {'nombre': 'sacapunta', 'cant': 2, 'precio': 5}
]

# Orden con descuento del 10%
print("El total de la compra con descuento es:", calcular_total(orden, descuento=10))

# Orden sin descuento
print("El total de la compra sin descuento es:", calcular_total(orden))
# ```"""Crear una función que reciba una cantidad variable de productos y sus precios, calcule el total y aplique un descuento opcional si se proporciona como un argumento con nombre.

# 1\. Usar args para recibir una lista de precios
# 2\. Usar kwargs para aceptar un descuento opcional y aplicarlo al total.
# """&#x20;
# def calcular\_total(\*args, \*\*kwargs) -> float:    total = 0 # Variable para llevar el total de la orden    # Recorrer la lista de diccionarios de producto, cantidad y precio    for p in args\[0]:        total += (p\['cant'] \* p\['precio'])    #Validar si hay descuento    for key, value in kwargs.items():        print(f'{key}: {value}')        if key == 'descuento':            total = total - (total \* value/100)    return total
# \# Ejemplo de uso
# \# Creo una orden, que sería un diccionario de productos con sus cantidades y preciosorden = \[    {'nombre': 'lapiz', 'cant': 2, 'precio': 3},    {'nombre': 'cuaderno', 'cant': 5, 'precio': 5},    {'nombre': 'compas', 'cant': 1, 'precio': 10},    {'nombre': 'regla', 'cant': 1, 'precio': 2},    {'nombre': 'sacapunta', 'cant': 2, 'precio': 5}]
# \# Orden con descuento del 10%print("El total de la compra con descuento es:", calcular\_total(orden, descuento=10))
# \# Orden sin descuentoprint("El total de la compra sin descuento es:", calcular\_total(orden))