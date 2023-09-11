
'''
Desarrollé parte del sistema de control de horarios para la universidad.
Para todo el personal que trabaja en la universidad se desea tener el nombre completo,
antigüedad en años y sector. Además, es necesario que para cada uno sea posible
almacenar y obtener la cantidad de horas trabajadas en el mes.

El personal docente tiene asociada una categoría que define la cantidad de horas
semanales a trabajar:
● Simple: 10 hs semanales
● Semiexclusiva: 20 hs semanales
● Exclusiva: 40 hs semanales

El personal no docente puede tener dos tipos de jornadas asignadas:
● Completa: 30 hs semanales
● Reducida: 20 hs semanales
Defina la clase Reloj que sepa generar un informe. Este debe indicar para cada persona
la cantidad de horas trabajadas en el mes indicando además si cumplió o no con el
mínimo esperado.


Para poner a prueba el sistema debe realizarse un simulación con los siguientes criterios:
● Al menos diez personas entre docentes y no docentes
● Para los docentes debe definirse aleatoriamente la categoría
● Para los no docentes debe definirse aleatoriamente la jornada
● La cantidad de horas trabajadas en el mes debe ser generada aleatoriamente
bajo las siguientes pautas:
○ Para docentes con categoría simple hay un 95% de posibilidad de que
exceda la cantidad de horas requeridas.
○ Para docentes con categoría semiexclusiva hay un 75% de posibilidad de
que exceda la cantidad de horas requeridas.
○ Para docentes con categoría exclusiva hay un 60% de posibilidad de que
exceda la cantidad de horas requeridas.
○ Para no docentes hay un 80% de posibilidad de que exceda la cantidad de
horas requeridas.
● Debe solicitarse a una instancia de la clase Reloj que imprima el informe.
'''
import random
from Personal import Personal
from NoDocente import NoDocente
from Docente import Docente
from Reloj import Reloj


personas = []

# Crear docentes aleatorios
for _ in range(5):
    nombre = "Docente" + str(_)
    antiguedad = random.randint(1, 10)
    sector = "Docencia"
    categoria = random.choice(["Simple", "Semiexclusiva", "Exclusiva"])
    docente = Docente(nombre, antiguedad, sector, categoria)
    personas.append(docente)

# Crear no docentes aleatorios
for _ in range(5):
    nombre = "NoDocente" + str(_)
    antiguedad = random.randint(1, 10)
    sector = "Administración"
    jornada = random.choice(["Completa", "Reducida"])
    nodocente = NoDocente(nombre, antiguedad, sector, jornada)
    personas.append(nodocente)

reloj = Reloj(personas)
informe = reloj.generar_informe()

# Imprimir informe
for nombre, detalles in informe.items():
    print(f"Nombre: {nombre}")
    print(f"Antigüedad: {detalles['Antigüedad']} años")
    print(f"Sector: {detalles['Sector']}")
    print(f"Horas Trabajadas: {detalles['Horas Trabajadas']} horas")
    print(f"Cumplió Mínimo: {'Sí' if detalles['Cumplió Mínimo'] else 'No'}")
    print("=" * 30)