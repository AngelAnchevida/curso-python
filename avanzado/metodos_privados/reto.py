class CuentaBancaria:
    def __init__(self, id, contraseña):
        self.id = id
        self.contraseña = contraseña
        self.saldo = 0
    
    #Verificamos que el usuarioId y contraseña existan
    def verificar_usuario(self):
        for us in users:
            if self.id == us.get('id'):
                if self.contraseña == us.get('contraseña'):
                    return True
        return False

    def verificar_saldo(self):
        for us in users:
            if self.id == us.get('id'):
                return print(f"Saldo disponible: {us.get('saldo')}")

    def _actualizar_saldo(self, sld):
        for us in users:
            if self.id == us.get('id'):
                old = us.get('saldo')
                #Actualizamos el valor de saldo en el diccionario
                us.update({'saldo' : sld})
                #Agregamos la información de la transacción a una lista
                movements.append({'transaccion client id' : self.id, 'saldo' : f'from {old} to {sld}'})
                return print(f"El nuevo saldo es {sld}")

    def __registrar_transaccion():
        print(movements)

    def public_transaction(self):
        self.__registrar_transaccion()


users = [   
            {'id' : 1, 'contraseña' : '12345', 'saldo' : 500},
            {'id' : 2, 'contraseña' : '34567', 'saldo' : 600}
        ]

movements = []

u1 = CuentaBancaria(1, '12345')

if __name__ == '__main__':

    while True:
        print("Bienvenido a banco platzi")
        print("Escoga la acción que desea realizar")
        print("1. Verificar saldo")
        print("2. Actualizar saldo")
        print("3. Consultar actualizaciones de saldos")
        print("4. Salir")
        userInput = input("Ingrese su opción: ")

        match userInput:
            case "1":
                u1.verificar_usuario()
                if u1.verificar_usuario():
                    print("Acceso autorizado")
                    print("Verificando saldo...")
                    u1.verificar_saldo()
                    input()
                else:
                    print("Usuario y/o contraseña incorrectos")
                    input()

            case "2":
                sld = int(input("Ingrese el saldo nuevo: "))
                u1._actualizar_saldo(sld)
                #print(u1._actualizar_saldo(sld))
                print(users)
                input()

            case "3":
                print(movements)
                input()
    
            case "4":
                print("Saliendo")
                break

            case _:
                print("Opçion invalida")