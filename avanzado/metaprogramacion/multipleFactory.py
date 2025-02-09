class MultipleFactory:

    #Crea una nueva instancia y desde aqui se controla la creación de los objetos
    #Cuando se usa new este va al principio
    def __new__(cls, factor: int):
        print(f"Creando instancia con factor {factor}")
        return super(MultipleFactory, cls).__new__(cls)

    def __init__(self, factor: int):
        print(f"Inicializando con factor {factor}")
        self.factor = factor

    def __call__(self, number: int) -> int:
        return number * self.factor


multiplier = MultipleFactory(5)

result = multiplier(10)

print(result)