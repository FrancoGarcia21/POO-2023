from Personaje import Personaje
import random 

class Paladin(Personaje):
    
    def __init__(self,nombre,arma):
        super().__init__(nombre,vida=150,nivelAtaque=90,nivelDefensa=80)
        self._arma = arma # quiero agregarle un atributo mas que sea tipo de arma como dato de color 
        
        
    def atacar(self, enemigo):
        super().atacar(enemigo)
        print(f"{self._nombre} hace grito de guerra ondeando su {self._arma}")
        ### cambio de lado
        print("Enemigo se intenta defender")
        enemigo.defender(self._nivelAtaque)
        #return ## preguntar como reformar esto
    #quiero que tenga mas ataque

    def defender(self,ataque):
        rand = random.randint(0, 2)
        nivelDefensa = self._nivelDefensa
        if ataque >= nivelDefensa:
            if rand > 1:
                self._vida -= (ataque-nivelDefensa+20)#tiene mas defensa porque es un paladin cuando se defiende
                print(f"{self._nombre} se alcanzo a defender")
            else:
                print("El enemigo no alcanzo a cubirse")
        print(f"La vida del personaje bajo a {self._vida}")
    