"""
4. Defina la clase abstracta Personaje con los atributos vida, nivelAtaque, nivelDefensa y los
métodos atacar():Integer y defender(Integer puntos). Implemente el método atacar pero
no el método defender(). Luego, cree dos clases hijas donde ambas implementan el
método defenderse y al menos una de ellas extiende el método atacar. Cada clase debe
establecer una cantidad de puntos de vida por defecto
En un ataque se deben realizar cierta cantidad de puntos de daño y en la defensa se
debe reducir esa cantidad de puntos de daños. El resultado final de los puntos de ataque
debe descontar la misma cantidad de puntos de vida del personaje que defiende.

class VidaCeroError(Exception):
    def __init__(self, personaje):
        self.personaje = personaje
        super().__init__(f"{self.personaje._nombre} ha perdido toda su vida.")


"""
from Personaje import Personaje
from Paladin import Paladin
from Arquero import Arquero
from Mago import Mago
import random



pala1 = Paladin("Ezze Bertedero","Hacha")
pala2 = Paladin("Brian Sancges","Cuchara")
arque = Arquero("Franky")
arque2 = Arquero("Ricado Ford")
personaje_actual = random.choice([pala1, arque])# en una lista d eobjeto nos da uno alazar




combatefinalizado = False
while not combatefinalizado:
    if personaje_actual == pala1:
        pala1.atacar(arque)
        personaje_actual = arque  
    else:
        arque.atacar(pala1)
        personaje_actual = pala1
            
    if arque.get_vida() <= 0:
        print(f"{arque.get_nombre()} ha perdido el combate. {arque.get_vida()}")
        combatefinalizado = True
    if pala1.get_vida() <= 0:
        print(f"{arque.get_nombre()} ha perdido el combate. {pala1.get_vida()}")## puse este get para saber sia ndaba
        combatefinalizado = True
        
    
    
'''
La excepcion deberia estar implementada en el metodo defende 
y el bucle debe cortat cuando uno d elos personajes muera pero NUNCA usar una excepcion para cerrar un bucle
'''