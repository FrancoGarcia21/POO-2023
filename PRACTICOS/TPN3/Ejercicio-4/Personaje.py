from abc import ABC, abstractmethod

class Personaje(ABC):
    def __init__(self,nombre,vida,nivelAtaque,nivelDefensa):
        self._nombre = nombre
        self._vida = vida
        self._nivelAtaque = nivelAtaque
        self._nivelDefensa = nivelDefensa
        
    def atacar(self,enemigo):
        #self.__enemigo
        print(f"{self._nombre} Ataca a: {enemigo._nombre} !!!! ")#### tambien pense que en vez de atacar deberia tener un
        enemigo._vida -= 30                                    #### metodo que sea absorver danio ? no se bien como seria la logica
                                                            ### o pode haceerlo todo en un metodo unico
    @abstractmethod
    def defender(self):
        pass