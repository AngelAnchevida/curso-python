class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    #Permite sumar dos vectores
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    #Devuelve en string de una manera que se pueda recrear el objeto
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


v1 = Vector(2, 3)
v2 = Vector(4, 1)

#La suma crea un nuevo vector
v3 = v1 + v2 #Sobrecarga de '+'

print(v3)