import reports

#Generar reportes de ventas y gastos usando funciones del módulo
sales_report = reports.generate_sales_report('October', 10000)
expenses_report = reports.generate_expenses_report('October', 5000)

print(sales_report)
print(expenses_report)