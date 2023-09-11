from Personaje import Personaje
import random

class Arquero(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre,vida=80, nivelAtaque=150, nivelDefensa=50)
        
    def atacar(self,enemigo):
        super().atacar(enemigo)
        print("Enemigo se defiende")
        enemigo.defender(self._nivelAtaque)

    def defender(self,ataque):
        rand = random.randint(0,3)
        nivelDefensa = self._nivelDefensa
        vida = self._vida
        if ataque >= nivelDefensa:
            if rand > 2:
                self._vida -= (ataque-nivelDefensa)
                print(f"{self._nombre} alcanzo a esquivar el ataque")
            else:
                print(f"{self._nombre} no alcanzo a esquivar el ataque")       
        if vida <= 0:# por aqui deberia poner la excepcion 
            self._vida = 0
        print(f"La vida del persona bajo a {self._vida}")
        
        ## esta clase anda asi