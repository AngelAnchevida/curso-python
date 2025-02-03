class BankAccount:
    def __init__(self, account_holder, balance):
        #Constructor
        self.account_holder = account_holder
        self.balance = balance
        self.is_active = True
        #Puedes darle valor a una de las propiedades del el constructor, por defecto
        #todos los objetos que crees sin especificar la propiedad tendrán el valor
        #que esta puesto en el constructor

    def deposit(self, amount):
        #Self hace referencia a si mismo, al objeto que usará la clase*
        if self.is_active:
            self. balance += amount
            print(f"Se ha depositado {amount}, saldo actual {self.balance}")
        else:
            print("No se puede depositar, Cuenta inactiva")

    def withdraw(self, amounth):
        if self.is_active:
            if amounth <= self.balance:
                self.balance -= amounth
                print(f"Se ha retirado {amounth} Saldo actual {self.balance}")
    
    def deactivate_account(self):
        self.is_active = False
        print(f"La cuenta ha sido desactivada")

    def activate_account(self):
        self.is_active = True
        print(f"La cuenta ha sido activada")


account1 = BankAccount("Angel",500)
account2 = BankAccount("Ana",1000)

#Llamada a los métodos
account1.deposit(200)
account2.deposit(100)

account1.deactivate_account()
account1.deposit(50)

account1.activate_account()
account1.deposit(50)

