from Empresa import Empresa
from Persona import Persona


trabajador1 = Persona("Franco","Garcia",'1999-12-21',"M",True,True)
trabajador2 = Persona("Mirtas","Legrand",'1960-06-11',"M",False,True)
trabajador3 = Persona("Pedro","Guittierrez",'2000-01-01',"M",True,True)
trabajador4 = Persona("Max","Mad",'1990-09-02',"M",True,True)
trabajador5 = Persona("Eibar","Gold",'1932-12-21',"M",True,True)

empresa1 = Empresa("Globant","O`Higgins 780")


empresa1.agregar_empleado(trabajador1)
empresa1.agregar_empleado(trabajador2)
empresa1.agregar_empleado(trabajador3)
empresa1.agregar_empleado(trabajador4)
empresa1.agregar_empleado(trabajador5)

empresa1.cantidad_empleados()

empresa1.mostrar_info_empleados()