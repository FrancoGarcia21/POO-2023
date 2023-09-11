from Cuenta import Cuenta
#from Cuenta import Impuesto ## pensaba usar impuesto en el pago / Pero me iba a complicar demasiado 
class Banco(Cuenta):
    
    
    def __init__(self, dueno, nro_cuenta, saldo, cbu):
        super().__init__(dueno, nro_cuenta, saldo)
        self._cbu = cbu
        
    def realizar_pago_debito(self,monto_pagar):# aca sera por debito
        reintegro=0
        if self._saldo > monto_pagar:
            reintegro = (monto_pagar * 0.1)
            self._saldo = self._saldo - monto_pagar + reintegro
        else:
            print("Saldo insuficiente para pagar")
        print(f"Su saldo actual es de {self._saldo} , se le hizo un reintegro de {reintegro}")
    
    
    
    def realizar_pago_credito(self,monto_pagar,cantidad_cuotas):# aca sera por credito / van a entrar difernetes parametros y actuaran de diferentes formas 
        # para mi deberia un if , pero como se saca a credito en mi logica podrias no tener saldo y endeudarte y quedaria saldo negativo 
        interes = 0
        if cantidad_cuotas <= 3:
            print("No hay intereses")
            self._saldo = self._saldo - (monto_pagar/3)
            print("Se a descontado la primera cuota")
        else:
            print("Esta transaccion tiene intereses")
            interes = (cantidad_cuotas/100)*2
            self._saldo = (self._saldo - ((monto_pagar/cantidad_cuotas) + interes))   
        print(f"Su saldo actual es de {self._saldo} , y el interes es de  {interes}")