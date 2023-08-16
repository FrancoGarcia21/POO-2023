class CuentaCorriente:
    from Persona import Persona
    
    def __init__(self,numero,persona,saldo):
        self.__persona = persona
        self.__numero = numero
        self.__saldo = saldo
    
    def depositar(self,monto):
        if monto > 0:
            print(f"Depositado ${monto}. Nuevo saldo: & {self.saldo}")
        else:
            print("Monto depositado no valido")
            
    def retirar(self,monto):
        if 0 < monto <= self.saldo:
            self.saldo -= monto
            print(f"Retira $ {monto}. Nuevo saldo: ${self.saldo}")
        else:
            print("Saldo insuficiente o monto no valido")
        
    def get_saldo(self):
        return self.saldo 
    
    ##en teoria esta clase esta completa 