import statistics
import csv

#Leer los datos de ventas mensuales desde un archivo CSV
monthly_sales = {}
with open('./ventas/monthly_sales.csv', mode = 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        month = row['month']
        sales = int(row['sales'])
        #Guardamos el valor de las ventas en el objeto vacio que creamos
        monthly_sales[month] = sales

#Obtener un valor especifico de un objeto con value para el contenido, keys es
#para el nombre de la propiedad
sales = list(monthly_sales.values())

print(sales)

#Hallar la media
mean_sales = statistics.mean(sales)
print(f"La media es : {mean_sales}")

#Hallar la mediana
median_sales = statistics.median(sales)
print(f"La mediana es : {median_sales}")

#Hallar la media
mode_sales = statistics.mode(sales)
print(f"La moda es : {mode_sales}")


#Desviación estandar
stdev_sales = statistics.stdev(sales)
print(f"La desviación estandar es: {stdev_sales}")

#Varianza
variance_sales = statistics.variance(sales)
print(f"La varianza es : {variance_sales}")


#Dato máximo
max_sales = max(sales)

#Dato mínimo
min_sales = min(sales)

range_sales = max_sales - min_sales

print(f"Rango de ventas; {range_sales}")