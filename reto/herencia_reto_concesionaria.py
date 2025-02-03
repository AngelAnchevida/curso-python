class Vehicle:
    def __init__(self, brand, model, price):
        #Encapsulación
        #Variables de instancia que contienen los datos privados del objetos
        self.brand = brand
        self.model = model
        self.price = price
        self.is_available = True

    def sell(self):
        if self.is_available:
            self.is_available = False
            print(f"El vehiculo {self.brand} ha sido vendido")
        else:
            print(f"El vehiculo {self.brand} no está disponible")
    
    #Abstracción
    #Solo se puede accedera a las varaibles de instancia mediante estos metodos
    def check_availability(self):
        return self.is_available

    #Abstracción
    def get_price(self):
        return self.price
    
    #Polimorfismo
    #Hace referencia que podemos tener muchas formas de darle un valor a una función o variable
    def start_engine(self):
        raise NotImplementedError("Este metodo debe ser implementado por la subclase")
    
    def stop_engine(self):
        raise NotImplementedError("Este metodo debe ser implementado por la subclase")

#Herencia
#Auto esta heredando de la clase padre Vehicle todos sus atributos
class Car(Vehicle):
    #Polimorfismo
    #Hace referencia que podemos tener muchas formas de darle un valor a una función o variable
    def start_engine(self):
        if not self.is_available:
            return f"El motor del coche {self.brand} está en marcha"
        else:
            return f"El coche {self.brand} no está disponible"
    
    def stop_engine(self):
        if self.is_available:
            return f"El motor del coche {self.brand} se ha detenido"
        else:
            return f"El coche {self.brand} no está disponible"

class Bike(Vehicle):
    def start_engine(self):
        if not self.is_available:
            return f"La bicicleta {self.brand} está en marcha"
        else:
            return f"La bicicleta {self.brand} no está disponible"
    
    def stop_engine(self):
        if self.is_available:
            return f"La bicicleta {self.brand} se ha detenido"
        else:
            return f"La bicicleta {self.brand} no está disponible"

class Truck(Vehicle):
    def start_engine(self):
        if not self.is_available:
            return f"El motor del camón {self.brand} está en marcha"
        else:
            return f"El camión {self.brand} no está disponible"
    
    def stop_engine(self):
        if self.is_available:
            return f"El motor del camón {self.brand} se ha detenido"
        else:
            return f"El camión {self.brand} no está disponible"

class Customer:
    def __init__(self, name):
        self.name = name
        self.purchased_vehicles = []

    def buy_vehicle(self, vehicle: Vehicle):
        if vehicle.check_availability():
            vehicle.sell()
            self.purchased_vehicles.append(vehicle)
        else:
            print(f"Lo siento, {vehicle.brand} no está disponible")
    
    def inquiere_vehicle(self, vehicle: Vehicle):
        if vehicle.check_availability():
            availability = "Disponible"
        else:
            availability = "No disponible"
        print(f"El {vehicle.brand} está {availability} y cuesta {vehicle.get_price()}")


class Dealership:
    def __init__(self):
        self.inventory = []
        self.customers = []

    def add_vehicles(self, vehicle: Vehicle):
        self.inventory.append(vehicle)
        print(f"El {vehicle.brand} ha sido añadido al inventario")

    def register_customers(self, customer: Customer):
        self.customers.append(customer)
        print(f"El cliente {customer.name} ha sido añadido")

    def show_available_vehicle(self):
        print("Vehiculos disponibles en la tienda")
        for vehicle in self.inventory:
            if vehicle.check_availability():
                print(f"- {vehicle.brand} por {vehicle.get_price()}")




car1 = Car("Toyota", "Corolla", 20000)
bike1 = Bike("Yamaha", "MT-07", 7000)
truck1 = Truck("Volvo", "FH16", 80000)

customer1 = Customer("Angel")


dealership = Dealership()
dealership.add_vehicles(car1)
dealership.add_vehicles(bike1)
dealership.add_vehicles(truck1)

#Mostrar vehiculos disponibles
dealership.show_available_vehicle()

#Cliente consulta un vehiculo
customer1.inquiere_vehicle(car1)

#Cliente comprar un vehiculo
customer1.buy_vehicle(car1)

#Mostrar vehiculos disponibles
dealership.show_available_vehicle()



