from Banco import Banco
from BilleteraVirtual import BilleteraVirtual
from Impuesto import Impuesto
import random

cuenta1 = Banco("Franco Garcia",1234,5000,39437204)
cuenta2 = BilleteraVirtual("Emilia Gallardo", 4032,500,123456)


## creando impuesto randoms

impuestos = []
for i in range(20):
    nombre = "Impuesto" + str(i+1)
    monto = random.randint(100, 500)
    periodo = random.randint(1,12)
    estado = random.choice([True,False])
    impuesto = Impuesto(nombre,monto,periodo,estado)
    impuestos.append(impuesto)
    
# for impuest  in impuestos:
#     print(impuest.mostrar_impuesto())

'''
'''

for impuest  in impuestos:
    num = random.randint(1,2)### esto me dic esi lo pago con credito o debito
    perido = impuesto.get_periodo()
    cantidad_cuotas = random.randint(1,12)
    print(impuest.mostrar_impuesto())
    if num == 1:
        #periodo = impuesto.get_periodo()
        cuenta1.realizar_pago_debito(monto)
        impuesto.verificar_pago(monto,perido)
    else:
        cuenta1.realizar_pago_credito(monto,cantidad_cuotas)
        impuesto.verificar_pago(monto,perido)
        
        
        
    
    
        
        
        
    
# impuesto = Impuesto("IV:A",100,1,True)
# print(impuesto.mostrar_impuesto())


    
# cuenta1.realizar_pago_efectivo(100)


