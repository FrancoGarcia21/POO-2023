'''
2. Defina la clase TarifaProveedor con un método calcular(totalSMS, totalMinutos,
totalGigas) que, dado la cantidad de mensajes, minutos de llamada y GB de consumo de
datos calcule el valor en pesos a pagar. El valor a retornar del método calcular debe ser
la suma de los resultados obtenidos en los métodos calcularSMS(totalSMS),
calcularMinutosDeLlamada(totalMinutos) y calcularConsumoGB(totalGigas)
Los valores por defecto de cada servicio son
● Mensajes de texto(SMS): $1
● Minuto de llamada: $15
● Gigas(GB) de internet: $20.
Además de los métodos anteriores, debe poseer un método abstracto getNombre() que
retorne el nombre del proveedor.
'''
from abc import ABC ,abstractmethod

class TarifaProveedor():
    
    def __init__(self):
        #self._nombre = nombre
        self._SMS = 1
        self._minutoPrecio = 1
        self._mintoLlamada = 15
        self._GBprecio = 20
        
    @abstractmethod
    def get_nombre(self):
        pass #return self._nombre
    
    def calcularSMS(self,cantidad):
        return cantidad * self._SMS
    
    def calcularMinutosDeLlamada(self,minutos):
        return minutos * self._minutoPrecio
    
    def calcularConsumoGB(self,gigas):
        return gigas * self._GBprecio
    
    def calcular(self,cantidad,minutos,gigas):
        total = self.calcularConsumoGB(gigas)+self.calcularMinutosDeLlamada(minutos)+self.calcularSMS(cantidad)
        return total
    
    ##f"El precio del total de los SMS es: {self.calcularSMS(cantidad)}. El precio de las llamadas realizadas es de: {self.calcularMinutosDeLlamada(minutos)} La cantidad de gigas consumidas fueron de: {self.calcularConsumoGB(gigas)} . Y el total es de {total}"