class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    #El operador __q__ permite que el operador == compare dos personas por sus
    #atributos nombre y edad
    def __eq__(self, otra_persona):
        return self.nombre == otra_persona.nombre and self .edad == otra_persona.edad


p1 = Persona("Angel", 30)
p2 = Persona("Angel", 30)

print(p2 == p1)