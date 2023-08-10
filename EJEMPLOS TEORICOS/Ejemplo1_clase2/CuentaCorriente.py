class CuentaCorriente:
    from Persona import Persona
    from Banco import Banco
    def __init__(self,persona,saldo,banco):
        self.persona = persona
        self.saldo = saldo
        self.banco = banco
    
    def depositar(self,monto):
        if monto > 0:
            self.saldo += monto
            print(f"Depositado ${monto}. Nuevo saldo: ${self.saldo}")
        else:
            print("Monto depositado invalido")
            
    def retirar(self, monto):
        if 0 < monto <= self.saldo:
            self.saldo -= monto
            print(f"Retira ${monto}. Nuevo saldo: ${self.saldo}")
        else:
            print("Saldo insufienciente o monto invalido")
    
    def get_saldo(self):
        return self.saldo     

    def datos_dueno(self):
        self.persona.imprimir_datos()
        
    def datos_banco(self):
       self.banco.obtener_datos_banco()
    
