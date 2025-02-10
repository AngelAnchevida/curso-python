class Customer:
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name

class CustomerManagement:
    def __init__(self):
        self.customers = {}

    def add_customer(self, customer):
        """Agrega un nuevo cliente al sistema."""
        self.customers[customer.customer_id] = customer
        print(f'Cliente {customer.name} agregado')
        #self.customers.update({'id' : customer_id, 'customer' : customer})
        return self.customers

    def get_customer(self, customer_id):
    #    for customr in self.customers:
    #        if customer_id == customr.get('id'):
    #            return customr
        """Obtiene la información de un cliente por ID."""
        return self.customers.get(customer_id, "Cliente no encontrado")
    