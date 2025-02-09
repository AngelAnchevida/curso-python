class BaseClass:
    def __init__(self):
        #El guion bajo sirve para identificar que metodos son privados
        #aunque solo es en aparienia, solo sirve para ayudar a otros 
        #colabodadores a identificarlos pero no los vuelve privaos
        self._protected_variable = 'Protected'
        #El doble guión bajo vuelve una variable privada y solo se puede
        #acceder a ella en el mismo nivel de identación
        self.__private_variable = 'Privated'

    #Aplica lo mismo para el guion bajo en los metodos 
    def _protected_method(self):
        print("Este es un método protegido")
    #El doble guion vuelve un metodo privado y solo accesible en el
    #mismo nivel de identación
    def __private_method(self):
        print('Esto es un método privado')

    #Podemos acceder al método privado mediante un método publico
    #mientras esten al mismo nivel de identacion
    def public_method(self):
        self.__private_method()


base = BaseClass()
#print(base._protected_variable)

#base._protected_method()

base.public_method()

#print(base.__private_variable)