from TarifaProveedor import TarifaProveedor

class Personal(TarifaProveedor):
    
    
    def __init__(self,nombre):
        super().__init__()
        self._nombre = nombre
        
    def get_nombre(self):
        return self._nombre
        
    def calcular(self, cantidad, minutos, gigas):
        minutos = minutos + (minutos*0.2)
        gigas = gigas +(gigas*0.5)
        return super().calcular(cantidad, minutos, gigas)