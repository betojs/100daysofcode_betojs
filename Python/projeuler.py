import array as arr


def example1(a):
    number = arr.array('i', [])
    # save[0]=1
    b=0
    c=0
    total=0
    for item in range(1, a):
        c = item % 3
        b = item % 5
        if(c==0 or b==0):
            number.append(item)
            total= total + item
    return number, total        

def example2(dato):
    condicion = dato
    a = 1
    b = 2
    c = 0
    i = 2
    par = 0
    d = 2
    while (c < condicion):
        c = a + b
        # print(c)
        a = b
        b = c
        par = c % 2
        if(par == 0):
            print(d)
            d = d + c
        i = i + 1

    return c , i , d


def example5(a):
    total = 0 
    i = 0
    mostrar= 0
    for item in range(137886840,30000000):
        for ite2 in range(1,20):
            total = item % ite2
            if(total == 0):
                i = i + 1
                if(i == 10):
                    print("Vamos bien por el %d pero aun no " % item)
                if(i == 20):
                    mostrar = item - 1
                    print("El NUMERO %d es divisible por todos" % (item - 1))
            if(total != 0):
                i=0
                break
    return mostrar
            

# print(example5(1))
            
        

def example6(a):
    total = 0
    total1 = 0
    cuadra = 0
    for item in range(1,101):
        total = total + (item**2)
        total1 = total1 + item
        print("%d ** 2 = %d .... %d" % (item, (item ** 2) , total))
    print("%d " % total1)
        
    cuadra = total1 ** 2
    print ("el cuadrado es %d y el total es %d" % (cuadra, total))
    send =  cuadra - total

    return send


# print(example6(1))

    
def default():
    return "Opcion no valida"

def switch(case, a):
    sw = {
        1: example1(a),
        2: example2(a),
        3: example5(a),
        4: example6(a),
    }
    return sw.get(case, default())

def menu():
    print("1.ejemplo 1 ")
    print("2.ejemplo 2")
    print("3.ejemplo 5")
    print("4.ejemplo 6")
    print("4.default")


a=int(input("valor de a = "))
menu()
case=int(input("seleccione una opcion = "))
print(switch(case, a))