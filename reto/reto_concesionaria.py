class Vehicle:
    def __init__(self, model, brand, price):
        self.model = model
        self.brand = brand
        self.price = price
        self.available = True

    def sell(self):
        if self.available:
            self.available = False
            print(f"El auto {self.brand} {self.model} ha sido vendido por {'${:,.2f}'.format(self.price)}")
        else:
            print(f"El auto {self.brand} {self.model} no está disponible")
    
    def check_availability(self):
        return self.available

    def get_price(self):
        return self.price


class Client:
    def __init__(self, name, client_id):
        self.name = name
        self.client_id = client_id
        self.bought_Vehicles = []

    def buy_Vehicle(self, Vehicle):
        if Vehicle.available:
            Vehicle.sell()
            self.bought_Vehicles.append(Vehicle)
        else:
            print(f"El auto {Vehicle.brand} {Vehicle.model} no está disponible")
    
    def inquiere_car(self,Vehicle):
        if Vehicle.available:
            print(f"El auto {Vehicle.brand} {Vehicle.model} está disponible")
        else:
            print(f"El auto {Vehicle.brand} {Vehicle.model} no está disponible")


class Store:
    def __init__(self):
        self.Vehicles = []
        self.clients = []
    
    def add_Vehicle(self, Vehicle):
        self.Vehicles.append(Vehicle)
        print(f"El auto {Vehicle.brand} {Vehicle.model} ha sido agregado por {'${:,.2f}'.format(Vehicle.price)}")
    
    def register_client(self, client):
        self.clients.append(client)
        print(f"El usuario {client.name} ha sido registrado")

    def show_available_Vehicles(self):
        print(f"Autos disponibles en la concesionaria: ")
        for Vehicle in self.Vehicles:
            if Vehicle.available:
                print(f"{Vehicle.brand} {Vehicle.model} {'${:,.2f}'.format(Vehicle.price)}")


#Crear autos
Vehicle1 = Vehicle("Model S", "Tesla", 100000)
Vehicle2 = Vehicle("Model X", "Tesla", 70000)

#Crear usuario
client1 = Client("Angel","001")
client2 = Client("Ana","002")


#Crear concesionaria
store = Store()
#Agregar autos
store.add_Vehicle(Vehicle1)
store.add_Vehicle(Vehicle2)
store.register_client(client1)

#Mostrar autos
store.show_available_Vehicles()

#Realizar compra
client1.buy_Vehicle(Vehicle1)

#Mostrar autos
store.show_available_Vehicles()

#Realizar compra
client2.buy_Vehicle(Vehicle1)

#Mostrar autos
store.show_available_Vehicles()

#Mostrar vehiculo disponible
client1.inquiere_car(Vehicle2)