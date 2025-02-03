import csv

new_product = {
    'name': 'Wireless Charger',
    'price': 75,
    'quantity': 100,
    'brand': 'ChargerMaster',
    'category': 'Accessories',
    'entry_date': '2025-01-22'
}


#Agrega información a un archivo existente
with open('manejo_archivos\csv\products.csv', mode='a', newline='') as file:
    #mode = 'a' hace referencia hacia append
    
    #file.write('\n') #Hace un salto de linea para que no se solape con el ultimo elemento
    #sin embargo tambien provoca que cada elemento agregado tenga un salto de pagina
    #pero solo pasa si lo ejecutas muchas veces
    csv_writter = csv.DictWriter(file, fieldnames = new_product)
    csv_writter.writerow(new_product)