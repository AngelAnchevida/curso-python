class Numbers:
    def __init__(self, x):
        self.x = x

    #Suma
    def __add__(self, other):
        return Numbers(self.x + other.x)
    
    #Resta
    def __sub__(self, other):
        return Numbers(self.x - other.x)

    #Multiplicación
    def __mul__(self, other):
        return Numbers(self.x * other.x)
    
    #División
    def __truediv__(self, other):
        return Numbers(self.x / other.x)
    
    #Para visualizar el valor de x
    def __repr__(self):
        return f"Vector({self.x})"

n1 = Numbers(20)
n2 = Numbers(5)

n3 = n1 + n2

print(n3)
