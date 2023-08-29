from Personaje import Personaje

class Mago(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre,vida=80, nivelAtaque=120, nivelDefensa=40)
    
    
    def atacar(self,enemigo):
        return super().atacar(enemigo) #* 0.5    ##aca se entinde simplemente sumandole danio al mago
                                ## en caso de sobrescribir redefiniria todo el codigo y no agregaria el super
    def defender(self,ataque):
        vas = self._nivelDefensa - ataque
        if vas < 0:##cosa vista en clase
            vida = vida + vas
            #vida = self._vida - vas
        if vida <= 0:
            self._vida=0
            print("Personaje murio")
        else:
            print(f'Te queda de vida {self._vida}')


##buscar excepcion par implementarla para ver si se murio el viejo