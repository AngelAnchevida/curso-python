import csv

import json

filepath = 'manejo_archivos/reto/products.csv'

converter_file_path = 'manejo_archivos/reto/products_converter.json'


filepath2 = 'manejo_archivos/reto/products.json'

converter_file_path2 = 'manejo_archivos/reto/products_converter.csv'


#Convertir csv a json
with open(filepath, mode='r') as file:
    csv_reader = csv.DictReader(file)
    
    #Primera forma de convertir csv a lista
    # datos_csv = []
    # i = 0
   
    # for row in csv_reader:
        
    #     datos_csv.append(row)
    #     print(datos_csv[i])
    #     i += 1

    #Segunda forma, mucho más optima y rapida
    datos_csv = list(csv_reader)
    

    print("Fin de CSV a JSON")

with open(converter_file_path, mode='w') as converted_file:
    json.dump(datos_csv, converted_file, indent=4)




#Convertir json a csv


with open(filepath2, mode='r') as file:
    json_reader = json.load(file)
    #json_reader contiene todo el contenido del json en objetos
    
    with open(converter_file_path2, mode='w', newline = '') as coverted_file:
        json_writer = csv.DictWriter(coverted_file, fieldnames = json_reader[0].keys())
        #para obtener los titulos de las columnas equivalentes de json a csv
        #usamos json_reader[0].keys() esto obtiene las keys del primer elemento
        #y las replica en las demas

        json_writer.writeheader()
        #creamos los headers del csv a partir del fieldname

        json_writer.writerows(json_reader)
        #escribimos elo resto del contenido