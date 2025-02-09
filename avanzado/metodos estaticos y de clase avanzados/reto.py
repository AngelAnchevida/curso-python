class Order:
    global_discount = 50

    @staticmethod
    def verify_order(amount):
        if amount < 50:
            return False
        else:
            return True
    
    @classmethod
    def order_discount(cls, amount):
        total = amount - (amount * (cls.global_discount / 100))
        return total

orders = [
            {'order' : 1, 'amount' : 70},
            {'order' : 2, 'amount' : 80},
            {'order' : 3, 'amount' : 60}
         ]

if __name__ == '__main__':
    #Hacemos un forma para leer cada una de las ordenes
    for order in orders:
        #Accedemos a los objetos uno por uno
        #con get obtenemos el valor de las keys dadas
        if Order.verify_order(order.get('amount')):
            current_order = order.get('amount')
            total_order = Order.order_discount(current_order)
            print(f"El total de la orden {order.get('order')} menos el descuento es {total_order}")