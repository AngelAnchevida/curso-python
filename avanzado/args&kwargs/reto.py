class Producto:
    def __init__(self, *price, ** discount):
        self.price = price
        self.discount = discount

    def show_total(self):
        print(f"El total de los productos es: {sum(self.price)}")
        if self.discount:
            #Se convierte el descuento de dict a lista para manipularlo
            #despues
            total_discount = list(dict.values(self.discount))
            total = sum(self.price) - ((sum(self.price) / 100) * total_discount[0])
            print(f"El total menos el descuento es: {total}")

product1 = Producto(1,2,3,4,5)
product2 = Producto(10,20,30,40,50, discount=40)
product1.show_total()
product2.show_total()




products = [
                {'Galletas': 18},
                {'Papitas': 20},
                {'Coca-cola': 22},
                {'product': 16}
           ]

def total_product(*productos, **discount) -> float:
    total_price = []

    #Se usa la posicion 0 de productos porque arg hace que se cree una
    #lista de listas y como solo tenemos una usamos la posición 0
    for prod in productos[0]:
            #Se convierten los precios de tipo dict a lista para poder
            #hacer un append a otra lista y guardar los numeros
            totalP = list(dict.values(prod))
            total_price.append(totalP[0])
    total = sum(total_price)

    #Si discount no existe se retorna el total
    if not discount:
        return f"El total de los productos es {total}"
    else:
        #Se hace la formula para saber el total final menos el descuento      
        disc = list(dict.values(discount))
        total = total - ((total/100) * disc[0])
        return f"El total de los productos menos el descuento es {total}"


products1 = total_product(products)
products2 = total_product(products, discount=50)

print(products1)
print(products2)