import csv

#Leer archivo
#Muestra el archivo fila por fila
with open('manejo_archivos\csv\products.csv', mode='r') as file:
    #Mode='r' hace referencia a read(leer)
    csv_reader = csv.DictReader(file)
    #Creamos una variable que lee el archivo
    for row in csv_reader:
        print(row)



#Mostar la informacion por columnas
with open('manejo_archivos\csv\products.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(f"El producto: {row['name']}, Precio: {row['price']}")