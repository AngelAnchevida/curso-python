from collections import defaultdict, Counter, deque
from enum import Enum

items = ['smartphone', 'earphone', 'tablet', 'TV', 'smartphone', 'earphone', 'tv']


def checkProduct(products: list[str]) -> defaultdict:
    count_products = defaultdict(int)
    for product in products:
        count_products[product] += 1
    return count_products

print("Tenemos en existencia: ", checkProduct(items))
print("Tenemos en existencia: ", Counter(items))

print(type(checkProduct(items)))

class OrderStatus(Enum):
    PENDING = 1 #Pendiente
    SHIPPED = 2 #Enviado
    DELIVERED = 3 #Entregado

def check_order_status(status: OrderStatus):
    # Comprueba el estado del pedido y devuelve un mensaje
    if status == OrderStatus.PENDING:
        return "Order is still pending."
    elif status == OrderStatus.SHIPPED:
        return "Order has been shipped."
    elif status == OrderStatus.DELIVERED:
        return "Order has been delivered."


def manage_delivery_queue() -> deque:
    #Crea una cola para gestionar entregas de productos
    delivery_queue = deque(["order_1", "order_2", "order_3"])
    return delivery_queue


queue = manage_delivery_queue()
print(queue)

#def PedirProducto(productList):











