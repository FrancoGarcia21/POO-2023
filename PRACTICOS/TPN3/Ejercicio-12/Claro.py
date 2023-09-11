from  TarifaProveedor import TarifaProveedor

class Claro(TarifaProveedor):
    
    def __init__(self, nombre):
        super().__init__()
        self._nombre = nombre
        
    def get_nombre(self):
        return self._nombre
    
    
    def calcular(self, cantidad, minutos, gigas):
        extra = ((super().calcular(cantidad, minutos, gigas))*0.20)
        return (super().calcular(cantidad, minutos, gigas) + extra)
    
    