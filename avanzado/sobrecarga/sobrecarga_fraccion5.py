from math import gcd

class Fraccion:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def __add__(self, otra_fraccion):
        nuevo_num = self.numerador * otra_fraccion.denominador + otra_fraccion.numerador * self.denominador #6
        nuevo_den = self.denominador * otra_fraccion.denominador #8
        comun_divisor = gcd(nuevo_num, nuevo_den) #Greatest commun divisor, Máximo común divisor

        #Se divide 6 y 8 entre el máximo comun divisor para obtener la fraccion mas pequeña posible
        return Fraccion(nuevo_num // comun_divisor, nuevo_den // comun_divisor) #Double slash para float division
    
    def __repr__(self):
        return f"{self.numerador}/{self.denominador}"


f1 = Fraccion(1, 4)
f2 = Fraccion(1, 2)
#f4 = Fraccion(1, 4)

f3 = f1 + f2 #Suma de fracciones gracias a __add__

#f3 = f3 + f4
print(f3)

print(gcd(6, 8))