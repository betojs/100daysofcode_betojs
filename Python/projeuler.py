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




    
def default():
    return "Opcion no valida"

def switch(case, a):
    sw = {
        1: example1(a),
        2: example2(a)
    }
    return sw.get(case, default())

def menu():
    print("1.ejemplo 1 ")
    print("2.ejemplo 2")
    print("3.default")


a=int(input("valor de a = "))
menu()
case=int(input("seleccione una opcion = "))
print(switch(case, a))