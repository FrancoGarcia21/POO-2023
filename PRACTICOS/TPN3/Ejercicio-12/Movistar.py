from TarifaProveedor import TarifaProveedor

class Movistar(TarifaProveedor):
    
    
    def __init__(self,nombre):
        super().__init__()
        self._nombre = nombre
        
        
    def calcular(self, cantidad, minutos, gigas):
        cantidad=(cantidad +(cantidad*0.2))
        minutos=(minutos +(minutos*0.2))
        gigas = (gigas +(gigas*0.3))
        return super().calcular(cantidad, minutos, gigas)