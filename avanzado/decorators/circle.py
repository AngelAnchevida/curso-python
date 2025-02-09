class Circle:

    def __init__(self, radius: float):
        self._radius = radius

    @property
    def area(self) -> float:
        return 3.1416 * (self._radius ** 2)
    
    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, value: float):
        if value < 0:
            raise ValueError("El radio no puede ser negativo")
        self._radius = value
    
#Creamos una intancia y directamente podemos usar un método de la clase
#No usamos los paréntesis porque se usa como una propiedad y no un método
circle = Circle(5)
# print(circle.area)


#El setter sirve para modificar información que tenemos dentro de la clase
circle.radius = -10
print(circle.area)