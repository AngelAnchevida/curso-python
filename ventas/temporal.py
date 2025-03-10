import statistics
import csv

#Leer los datos de ventas mensuales desde un archivo CSV
monthly_sales = {}
with open('./ventas/monthly_sales.csv', mode = 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        month = row['month']
        sales = int(row['sales'])
        monthly_sales[month] = sales


sales = list(monthly_sales.values())

print(sales)
