import random
import os
from colorama import init, Fore, Back, Style
init()
a=0
numero = 0
while(a == numero):
    a = int(random.randrange(50))
    


c = 0
d = 0
print("Hola {%d}" % a)
while(a != numero):
    numero = int(input("Ingresa un numero "))
    if(numero > a):
        print("El numero ingresado es mayor que el Ramdon")
        c = c + 1
        if(c == 2):
            print ("Intenta con un numero por debajo de %d " % ((a * 2) + 3))
        if(c == 4):
            print("El numero es muy bajo ")
            print ("Intenta con un numero por arriba de %d " % (a - numero))
    if(numero < a):
        print("El numero Ingresado es Menor al Ramdon")
        d += 1
        if(d == 2):
            print ("Intenta con un numero por arriba de %d " % ((a / 2) - 3))
        if (d == 4):
            print("El numero es muy alto")
            print ("Intenta con un numero por deabjo de %d " % ((a + numero)))
            d = 0

    print (numero)

os.system ("cls") 
print(Back.WHITE+"********************************************")
print("*                                          *")
print(Fore.RED+"*Felicidades Encontraste el numero Correcto*"+Fore.RESET)
print("*                                          *")
print("********************************************")