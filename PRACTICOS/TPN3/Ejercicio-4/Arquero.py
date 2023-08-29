from Personaje import Personaje

class Arquero(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre,vida=90, nivelAtaque=120, nivelDefensa=30)
        #
        # self.__nombre = nombre
        
    def atacar(self,enemigo):
        super().atacar(enemigo)
        print("Enemigo se defiende")
        enemigo.defender(self._nivelAtaque)
        # return 
    
    #def defender(self,ataque):
    #   return super().defender()

    def defender(self,ataque):
        nivelDefensa = self._nivelDefensa
        if ataque >= nivelDefensa:
            self._vida -= (ataque-nivelDefensa)###puse que por ser arquero tiene menos defensa
            print(f"{self._nombre} se alcanzo a defender")
        print(f"La vida del persona bajo a {self._vida}")

