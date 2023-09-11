from Profesor import Profesor

class ProfesorTitular(Profesor):
    
    def __init__(self, nombre, apellido, edad, horasTrabajadas, valorHora,antiguedad,valorAntiguedad):
        super().__init__(nombre, apellido, edad, horasTrabajadas, valorHora)
        self.__antiguedad = antiguedad
        self.__valorAntiguedad = valorAntiguedad
        
        
    def get_antiguedad(self):
        return self.__antiguedad    
        
    def get_remuneracion_antiguedad(self):
        return self.__valorAntiguedad * self.get_antiguedad()
    
        
    def get_remuneracion_mensual(self):## aca extiendo por eso hago la herencia entonces agrego la logica del titular
        super().get_remuneracion_mensual() * self.get_remuneracion_antiguedad()
        