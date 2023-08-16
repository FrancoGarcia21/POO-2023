class Transaccion:
    from CuentaCorriente import CuentaCorriente
    
    def __init__(self,numero,origen,destino,monto,motivo):
        self.__numero = numero
        self.__origen = origen
        self.__destino = destino 
        self.__monto = monto
        self.__motivo = motivo
        
    def get_info(self):
        print(f"numero $ {self.__numero}. Origen: ${self.__origen} . Destino: ${self.__destino} . Monto ${self.__monto} . Motivo: ${self.__motivo} ")
        
        ##en teoria esta clase esta completa