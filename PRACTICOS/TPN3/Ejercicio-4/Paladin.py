from Personaje import Personaje
import random 

class Paladin(Personaje):
    
    def __init__(self,nombre,arma):
        super().__init__(nombre,vida=100,nivelAtaque=80,nivelDefensa=150)
        self._arma = arma # agrege un atributo mas que sea tipo de arma como dato de color 

    def atacar(self, enemigo):
        super().atacar(enemigo)
        print(f"{self._nombre} hace grito de guerra ondeando su {self._arma}")
        print("Enemigo se intenta defender")
        enemigo.defender(self._nivelAtaque)

    def defender(self,ataque):
        rand = random.randint(0, 3)
        nivelDefensa = self._nivelDefensa
        vida = self._vida
        if ataque >= nivelDefensa:
            if rand > 1:
                self._vida -= (ataque-nivelDefensa+20)#tiene mas defensa porque es un paladin 
                print(f"{self._nombre} se alcanzo a defender")
            else:
                print("El enemigo no alcanzo a cubirse")
        if vida <= 0:### aqui deberia poner la excepcion por esta parte del codigo
            raise 
            #self._vida = 0
        #print(f"La vida del personaje bajo a {vida}")
    