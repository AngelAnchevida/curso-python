class Producto:
    def __init__(self, id, name, price, stock):
         self.id = id
         self.name = name
         self._price = price
         self._stock = stock

    @property
    def product(self):
        return self.id, self.name, self._price, self._stock
    
    @product.setter
    def product(self, newProduct):
        #Se usa una tupla para pasar los datos y se usan sus posiciones
        if newProduct[0] < 0 or newProduct[1] < 0:
            raise ValueError("El precio y/o stock no pueden ser negativos")
        self._price = newProduct[0]
        self._stock = newProduct[1]

    @product.deleter
    def product(self):
        print(f"El producto {self.name} ha sido eliminado")
        del self

    def calcular_valor(self):
        total = self._price * self._stock
        return print(f"El valor total del inventario es {total}")
        
#Instancia de producto
prod1 = Producto(1, "Huevo", 3, 20)
print(prod1.product)

#Solo se pueden pasar los datos en tupla o en listas
prod1.product = (5, 10)
print(prod1.product)

#del prod1.product
#print(prod1.product)

prod1.calcular_valor()