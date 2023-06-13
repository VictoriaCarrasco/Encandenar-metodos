class Usuario:
    def __init__(self, nombre, email, balance):
        self.nombre = nombre
        self.email = email
        self.balance_cuenta = balance
        
        
    def hacer_deposito(self, amount):
        self.balance_cuenta += amount
        return self 

    def hacer_giro(self, amount):
        self.balance_cuenta -= amount
        return self 

    def transferir_dinero(self, other_user, amount):
        self.hacer_giro(amount)
        other_user.hacer_deposito(amount)
        return self

    def mostrar_balance_usuario (self):
        print(self.nombre,"$", self.balance_cuenta)
        return self


Usuario1=Usuario("Guido van Rossum", "guido@python.com", 900)     
Usuario2=Usuario("Adrien", "adrien@python.com", 400)  
Usuario3=Usuario("Benny Bob", "benny@python.com", 200)  


Usuario1.hacer_deposito(100).hacer_deposito(200).hacer_deposito(150).hacer_giro(50).mostrar_balance_usuario()

Usuario2.hacer_deposito(100).hacer_deposito(200).hacer_giro(150).hacer_giro(50).mostrar_balance_usuario()

Usuario3.hacer_deposito(200).hacer_giro(20).hacer_giro(40).hacer_giro(100).mostrar_balance_usuario()

#Realizar transferencia de dinero de usuario 1 a usuario 3
Usuario1.transferir_dinero(Usuario3, 200)
Usuario1.mostrar_balance_usuario()
Usuario3.mostrar_balance_usuario()