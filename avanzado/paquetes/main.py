#Importar las funciones de los modulos dentro del paquete
from ecommerce.inventory.stock import add_product, remove_product
from ecommerce.sales.orders import product_sale

add_product('Laptop', 10)
remove_product('Laptop')
product_sale('Laptop', 2)