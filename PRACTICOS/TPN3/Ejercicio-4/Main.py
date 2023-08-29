"""
4. Defina la clase abstracta Personaje con los atributos vida, nivelAtaque, nivelDefensa y los
métodos atacar():Integer y defender(Integer puntos). Implemente el método atacar pero
no el método defender(). Luego, cree dos clases hijas donde ambas implementan el
método defenderse y al menos una de ellas extiende el método atacar. Cada clase debe
establecer una cantidad de puntos de vida por defecto
En un ataque se deben realizar cierta cantidad de puntos de daño y en la defensa se
debe reducir esa cantidad de puntos de daños. El resultado final de los puntos de ataque
debe descontar la misma cantidad de puntos de vida del personaje que defiende.


"""
from Personaje import Personaje
from Paladin import Paladin
from Arquero import Arquero
from Mago import Mago

pala1 = Paladin("Ezze Bertedero","Hacha")
pala2 = Paladin("Brian Sancges","Cuchara")
arque = Arquero("Franco Garcia")
arque2 = Arquero("Ricado Ford")
mago = Mago("Rey")

pala1.atacar(pala2)
arque.atacar(pala2)
arque.atacar(pala2)
pala1.atacar(pala2)
mago.atacar(pala1)

