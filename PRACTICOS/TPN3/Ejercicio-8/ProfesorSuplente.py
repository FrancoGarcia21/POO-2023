from Profesor import Profesor
class ProfesorSuplente(Profesor):
    
    def __init__(self, nombre, apellido, edad, horasTrabajadas, valorHora):
        super().__init__(nombre, apellido, edad, horasTrabajadas, valorHora)
        
    # def get_remuneracion_mensual(self):
    #     return self._valorHora * self.get_horas_trabajadas()