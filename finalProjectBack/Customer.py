from User import User


class Customer(User):
    def __init__(self, id, full_name, phone_number, customer_id, customer_name, customer_email, customer_password):
        super().__init__(id, full_name, phone_number)
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.customer_email = customer_email
        self.customer_password = customer_password

    def create_customer(self):
        #crear cliente
        pass

    def list_customer(self):
        #listar clientes
        pass

    def delete_customer(self):
        #eliminar cliente
        pass
