from Cuenta import Cuenta
class Impuesto:
    
    def __init__(self,nombre,monto,periodo,estado):
        self.__nombre = nombre
        self.__monto = monto
        self.__periodo = periodo
        self.__estado = estado
        
    def verificar_pago(self,monto,periodo):
        if self.__monto == monto and self.__periodo == periodo:
            print("El impuesto fue pagado ")
            self.__estado = True
        else:
            print("El impuesto no fue pagado")
            self.__estado = False
    
    def mostrar_impuesto(self):
        return f'Nombre : {self.__nombre} Monto: {self.__monto} Periodo: {self.__periodo} Estado: {self.__estado}'
    
    def get_monto(self):
        return self.__monto
    
    def get_periodo(self):
        return self.__periodo
    
    
    def set_periodo(self,valor):
        self.__periodo = valor
    
    # def set_estado(self,estado):
    #     self.__estado = estado # Pensaba utilizar el set para setearlo cuando se haga el pago 