import json

file_path = 'manejo_archivos\json\products.json'

new_product = {
    'name': 'Wireless Charger',
    'price': 75,
    'quantity': 100,
    'brand': 'ChargerMaster',
    'category': 'Accessories',
    'entry_date': '2025-01-22'
}

with open(file_path, mode='r') as file:
    products = json.load(file)


products.append(new_product)


with open(file_path, mode='w') as file:
    #Añade o aumenta información con dump
    json.dump(products, file, indent=4)
    #dump(informacion que queremos escribir en el archivo, el archivo, la identación)