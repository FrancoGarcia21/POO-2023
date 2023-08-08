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
while(valor!=1 and valor!=2):
    valor = int(input("Ingrese una opcion posible"))
if (valor==1 and num1>num2):
        print("Ganaste")
elif (valor==1 and num1<num2):
        print("Perdiste")
if(valor==2 and num2>num1):
            print("Ganaste")
elif(valor==2 and num2<num1):
            print("Perdiste")
            
print("El valor N1 fue:",num1,"el valor N2 fue:",num2,"y el valor que apostaste fue:",valor)
        

    
#Con esto se comenta si no me equivoco#