from collections import defaultdict

def count_products(orders: list[str]) -> defaultdict:
    #Crea un diccionario con valor por defecto 0 
    #Defaultdict está estableciendo que 0 es la información por defecto
    product_count = defaultdict(int) #Empieza en 0 por defecto
    for product in orders:
        #Le agrega el product count a cada producto de la lista pero si
        #el producto está repetido junta el count
        product_count[product] +=1
        #Esto sirve para contar productos repetidos
    return product_count

orders = ['laptop', 'smartphone', 'laptop', 'tablet']
count = count_products(orders)
print(count)