class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    #Permite que instancias de una clase se puedan comparar con el menor que (<)
    def __lt__(self, otra_persona):
        return self.edad < otra_persona.edad


p1 = Persona("Ana", 25)
p2 = Persona("Angel", 28)

print(p1 < p2)