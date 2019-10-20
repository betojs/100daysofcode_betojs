

def promedio_de_simon():
    # a= [[0,0,0,0],
    #     [0,1,1,10],
    #     [0,3,3,3],
    #     [0,34,24,24]]
    # for item in range(len(a)):
    #     print(item)
    matriz = []
    matriz2 = []
    a=5
    b=3
    for i in range(b):
        matriz.append([])
        matriz2.append([])
        print("i=%d" % i)
        for j in range(a):
            matriz[i].append(int(input("Ingrese un numero")))
            matriz2[i].append(j+1)
    print (len(matriz))
    print (len(matriz[0]))

    for i in range(b):
        for j in range(a):
            # print("ï= %d   y   j=%d" % (i,j ))
            if( (i== ( len(matriz[0])-len(matriz[0]) ) and j == ( len(matriz)-len(matriz) )) ):#esquina superior izquierda
                matriz2[i][j] =(matriz[i][j+1] + matriz[i+1][j]) /2

            if(i == len(matriz)-1  and j == len(matriz[0])-1 ): # esquina inferior derecha
                print("len(matriz[0]) -1")

                matriz2[i][j] =(matriz[i][j-1] + matriz[i-1][j]) /2

            if(i == len(matriz)-1  and j == len(matriz)-len(matriz) ): #esquina inferior  izquierda
                matriz2[i][j] =(matriz[i-1][j] + matriz[i][j+1]) /2

            if(i == len(matriz)-len(matriz)  and j == len(matriz[0])-1 ): #esquina superior derecha
                matriz2[i][j] =(matriz[i][j-1] + matriz[i+1][j]) /2
                

            if(i==len(matriz)-len(matriz)): #fila de arriba
                if(j>len(matriz)-len(matriz) and j <len(matriz[0])-1 ):
                    matriz2[i][j] =(matriz[i][j-1] + matriz[i+1][j] + matriz[i][j+1]) /3
            
            if(i == len(matriz)-1 ): #fila de abajo
                if(j>len(matriz)-len(matriz) and j <len(matriz[0])-1 ):
                    matriz2[i][j] =(matriz[i][j-1] + matriz[i-1][j] + matriz[i][j+1]) /3



            if(j==len(matriz)-len(matriz) ): #fila izquierda
                if(i>len(matriz)-len(matriz) and i <len(matriz)-1 ):
                    matriz2[i][j] =(matriz[i-1][j] + matriz[i][j+1] + matriz[i+1][j]) /3

            if(j==len(matriz[0])-1 ): #fila derecha
                if(i>len(matriz)-len(matriz) and i <len(matriz)-1 ):
                    matriz2[i][j] =(matriz[i-1][j] + matriz[i][j-1] + matriz[i+1][j]) /3


            if( (i > 0 and j > 0) and (i<len(matriz)-1 and j< len(matriz[0])-1 )): #centro
                    matriz2[i][j] =(matriz[i][j-1] + matriz[i-1][j] + matriz[i][j+1] + matriz[i+1][j]) /4

    



    for i in range(b):
        print (matriz[i])
    print(" ")
    for i in range(b):
        print (matriz2[i])

        
    
promedio_de_simon()