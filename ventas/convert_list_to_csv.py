import csv
import statistics

new_product = [
    {
        'month': 'Enero',
        'sales': 120
    },
    {
        'month': 'Febrero',
        'sales': 130
    },
    {
        'month': 'Marzo',
        'sales': 150
    },
    {
        'month': 'Abril',
        'sales': 170
    },
    {
        'month': 'Mayo',
        'sales': 160
    },
    {
        'month': 'Junio',
        'sales': 180
    },
    {
        'month': 'Julio',
        'sales': 190
    },
    {
        'month': 'Agosto',
        'sales': 200
    },
    {
        'month': 'Septiembre',
        'sales': 210
    },
    {
        'month': 'Octubre',
        'sales': 190
    },
    {
        'month': 'Noviembre',
        'sales': 185
    },
    {
        'month': 'Diciembre',
        'sales': 210
    }
]

#Creamos el archivo

with open('ventas\monthly_sales.csv', mode='w', newline='') as file:

    #Seleccionamos cuales son las keys para nuestro CSV
    csv_writter = csv.DictWriter(file, fieldnames = new_product[0].keys())
    #Escribimos las keys en el archivo
    csv_writter.writeheader()
    
    #Escribimos el contenido
    for month in new_product:
        csv_writter.writerow(month)