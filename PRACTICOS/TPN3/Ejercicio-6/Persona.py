from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self,nombre,apellido):
        self._nombre = nombre
        self._apellido = apellido
        
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self,nombre):
        self.__nombre = nombre
        
    def get_apellido(self):
        return self.__apellido
    
    def set_apellido(self,apellido):
        self.__apellido = apellido
        
    @abstractmethod
    def materia():
        pass