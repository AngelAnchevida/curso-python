import csv

#Creamos un atajo de la ruta del archivo existente
file_path = 'manejo_archivos\csv\products.csv'
#Creamos un atajo con la ruta y nombre del archivo que vamos a crear
update_file_path = 'manejo_archivos\csv\products_updated.csv'

with open(file_path, mode='r') as file:
    #Creamos una variable que lea el archivo existente
    csv_reader = csv.DictReader(file)

    #Obtenemos los nombres de las columnas existentes a partir de la variable creada
    #Y le agregamos una columna mas
    fieldnames = csv_reader.fieldnames + ['total_value'] + ['type']

    
    with open(update_file_path, mode='w', newline='') as updated_file:
        #Mode='w' hace referencia a write(escribir)
        

        #Creamos una variable que está preparada para escribir en el archivo
        #DictWriter(archivo que recibe, que es lo que recibe)
        #Si el archivo no existe se crea automaticamente
        csv_writter = csv.DictWriter(updated_file, fieldnames=fieldnames)

        #Escribe los encabezados a partir de las columnas que ya existen
        #Necesita que DictWriter ya haya recibido los parametros correspondientes
        csv_writter.writeheader()

        #Se crea un for que lee todas las filas de csv_reader, el cual
        #contiene la información del archivo original
        for row in csv_reader:
            #Se le da valor a total-value en cada fila
            row['total_value'] = float(row['price']) * int(row['quantity'])
            row['type'] = "electronic"
            #Row ahora contiene las filas originales y le agrega valor a la ultima columna
            csv_writter.writerow(row)