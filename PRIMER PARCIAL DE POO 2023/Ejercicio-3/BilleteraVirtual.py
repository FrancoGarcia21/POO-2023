from Cuenta import Cuenta
    
class BilleteraVirtual(Cuenta):
        
        
    def __init__(self, dueno, nro_cuenta, saldo, cvu):
        super().__init__(dueno, nro_cuenta, saldo)
        self.__cvu = cvu
        
        
    def realizar_pago_debito(self,monto):## no estas aplicando bien el polimorfismo estos podrian tener cuerpo en la clase padre
        if self._saldo >= monto:## y luego lo redefinis
            self._saldo = self._saldo - monto
            print("La transaccion se a echo con exito")
        else:
            print("Saldo insuficiente")
            
    
    def realizar_pago_credito(self,monto,cantidad_cuotas):
        if cantidad_cuotas <= 3:
            print("No hay intereses")
            self._saldo = self._saldo - (monto/3)
            print("Se a descontado la primera cuota")
        else:
            print("Esta transaccion tiene intereses")
            interes = (cantidad_cuotas/100)*8
            self._saldo = (self._saldo - ((monto/cantidad_cuotas) + interes))   
        print(f"Su saldo actual es de {self._saldo} , y el interes es de  {interes}")
        
        