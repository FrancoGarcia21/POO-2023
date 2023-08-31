from abc import ABC, abstractmethod


class Personaje(ABC):
    def __init__(self,nombre,vida,nivelAtaque,nivelDefensa):
        self._nombre = nombre
        self._vida = vida
        self._nivelAtaque = nivelAtaque
        self._nivelDefensa = nivelDefensa
        
    def atacar(self,enemigo):
        print(f"{self._nombre} Ataca a: {enemigo._nombre} !!!! ")
        enemigo._vida -= 30                                                                                    
    @abstractmethod
    def defender(self):
        pass
    
    
    def get_vida(self):
        return self._vida
    
    def get_nombre(self):
        return self._nombre
'''
class VidaCeroError(Exception):
    def __init__(self, personaje):
        self._personaje = personaje  
        super().__init__(f"{self._personaje.get_nombre()} ha perdido toda su vida")
    
    except VidaCeroError as e:
        print(e)
        break
        '''