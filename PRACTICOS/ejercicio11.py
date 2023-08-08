import random
num1 = random.randint(1,10)
num2 = random.randint(1,10)
print(num1,num2)
if (num1==num2):
    while(num1==num2):    
        num1 = random.randint(1,10)
        num2 = random.randint(1,10)
        print(num1,num2)
        
print("Si desea apostar al valor 1 ingrese. Si desea apostar al valor 2 ingrese 2")
valor = int(input("Ingrese una opcion"))
if (valor==1 and num1>num2):
    print("Felicidades Ganaste")
else:
    print("Perdiste toda tu casa")
    if(valor==2 and num2>num1):
        print("Felicidades Ganaste")
    else:
        print("Perdiste toda tu casa")
print("El valor N1 era:",num1,"el valor N2 era:",num2)   
    
    
#Con esto se comenta si no me equivoco#