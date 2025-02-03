import json

with open('manejo_archivos\json\products.json', mode='r') as file:
    #Lee el archivo con .load
    products = json.load(file)

#Mostrar el contenido
for product in products:
    #Imprime tal cual el json
    # print(product)

    print(f"Product: {product['name']}, Price: {product['price']}")