class Puesto:

    def __init__(self,nombre):
        self.__nombre = nombre
        
    def get_puesto(self):
        return self.__nombre
    
    def set_puesto(self,nombre):
        self.__nombre = nombre