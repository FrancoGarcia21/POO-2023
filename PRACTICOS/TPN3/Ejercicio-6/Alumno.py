from Persona import Persona
class Alumno(Persona):
    
    def __init__(self, nombre, apellido):
        super().__init__(nombre, apellido)
        self._materias = []
        
    def get_materias(self):
        return self._materias
    
    def set_materias(self,materias):#creo que entra una lista
        self._materias = materias
        
    def agregar_materia(self,materia):
        self._materias.append(materia)
        
    def materia(self):
        msg = "El alumno se encuentra cursando las siguientes materias \n"
        for mat in self._materias:
            msg = '{} {} {}'.format(msg,mat,"\n")
        return msg