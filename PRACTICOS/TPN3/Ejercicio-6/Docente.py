from Persona import Persona
class Docente(Persona):
    
    def __init__(self, nombre, apellido,materia):
        super().__init__(nombre, apellido)
        self.__materia = materia
    
    def get_materia(self):
        return self.__materia
    
    def set_materia(self,materia):
        self.__materia = materia
        
    def materia(self):
        return "El Docente dicata la siguiente clase {} {}".format(self.__materia,"\n")