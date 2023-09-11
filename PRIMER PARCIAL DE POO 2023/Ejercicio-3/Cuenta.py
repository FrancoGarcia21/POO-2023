from abc import ABC ,abstractmethod
class Cuenta(ABC):
    
    def __init__(self,dueno,nro_cuenta,saldo):
        self._dueno = dueno # estan en protected porque los heredo
        self._nro_cuenta = nro_cuenta
        self._saldo = saldo
        
    def get_saldo(self):
        return self._saldo
    
    @abstractmethod
    def realizar_pago_debito(self):# despues implementare cada uno en su respectiva clase
        pass
    
    @abstractmethod
    def realizar_pago_credito(self):### 
        pass
    """
    Estos metodos los puse en abstracto , luego a la mitad me di cuenta que tenia que haber echo las acciones basicas
    y luego extenderlo en las demas clases.
    No estoy exprimiendo al maximo esta herencia
    
    """