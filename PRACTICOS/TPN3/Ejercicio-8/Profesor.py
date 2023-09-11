#from abc import ABC, abstractmethod
class Profesor():
    
    def __init__(self,nombre,apellido,edad,horasTrabajadas,valorHora):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad
        self._horasTrabajadas = horasTrabajadas
        self._valorHora = valorHora
        
        
    def get_horas_trabajadas(self):
        return self._horasTrabajadas
    
    def get_nombre(self):
        return self._nombre
    
    def get_apellido(self):
        return self._apellido
    
    
    def get_remuneracion_mensual(self):## aca le doy cuerpo y lo lo extiedo en los demas
         return self._valorHora * self.get_horas_trabajadas()

    # @abstractmethod#lo redefino despues ya que no van a ser lo mismo para todos
    # def get_remuneracion_mensual(self):# esto es una forma si el problema fuera mas escalable
    #     pass
        
        