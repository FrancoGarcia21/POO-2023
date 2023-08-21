from Persona import Persona
from Familia import Familia
from Censo import Censo

familia1 = Familia()
persona1 = Persona("Franco","Garcia",'1999-12-21',"M",True,True)
persona2 = Persona("Tania","Garcia",'1992-05-02',"F",False,True)
persona3 = Persona("Ariel","Garcia",'1972-01-6',"M",False,True)

familia1.agregrar_integrante(persona1)
familia1.agregrar_integrante(persona2)
familia1.agregrar_integrante(persona3)

familia2 = Familia()
persona4 = Persona("Fran","cia",'2018-12-21',"M",True,True)
persona5 = Persona("Tani","cia",'1994-05-02',"F",False,True)
persona6 = Persona("PEPE","cia",'1973-01-6',"M",False,True)
persona7 = Persona("ranco","cia",'1929-12-21',"M",True,True)
persona8 = Persona("nia","cia",'2002-05-02',"F",False,True)
persona9 = Persona("iel","cia",'1975-01-6',"M",False,True)

familia2.agregrar_integrante(persona4)
familia2.agregrar_integrante(persona5)
familia2.agregrar_integrante(persona6)
familia2.agregrar_integrante(persona7)
familia2.agregrar_integrante(persona8)
familia2.agregrar_integrante(persona9)


familia3 = Familia()
persona44 = Persona("tito","fracia",'1997-12-21',"F",True,True)
persona52 = Persona("MELi","fraccia",'1994-05-02',"F",False,True)
familia3.agregrar_integrante(persona44)
familia3.agregrar_integrante(persona52)

#print(persona1.devolver_edad())#testeando
#print(persona1.info_persona())##testeando

familia1.mostrar_integrantes()
print(familia3.cantidad_inte())
#familia2.mostrar_integrantes()#testeo
#familia3.mostrar_integrantes()#testeo
print(familia1.promedio_edad_familia())


censo1 = Censo("Censo Comuna")
censo1.agregar_fami(familia1)
censo1.agregar_fami(familia2)
censo1.agregar_fami(familia3)

censo1.cantidad_fami()## parte del ejercicio 9
censo1.cantidad_personas()## parte del ejercicio 9
censo1.promedio_total_familias()## parte del ejercicio 9


#print(familia1.cantidad_trabajadores())
censo1.cantidad_total_trabajadores()## parte del ejercicio 9 

print(persona1.puede_trabajar())## ejercicio 10
print(persona1.puede_manejar())