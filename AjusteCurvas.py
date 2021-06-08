# Ugalde Carreño Paulina 19141209

# Importamos las siguientes 
import numpy as np
import matplotlib.pyplot as plt

# Definimos un arreglo para almacenar los puntos
puntos = []
# Abrimos nuestro archivo txt donde guardamos nuestros puntos
with open("Puntos.txt", "r") as File:
	for lineas in File:
        # Usamos lineas.split() para separar cada linea usando el caracter de espacio en blanco, 
        # por lo que obtenemos una lista donde cada elemento es una de los numeros de esa línea. 
        # Usamos el método extend para copiar todo el contenido de esa lista de numeros a otra lista llamada puntos
		puntos.extend(lineas.split())
# Cerramos el archivo
File.close()

# Listas que almacenaran las coordenadas en x e y respectivamente
CoordenadasX = []
CoordenadasY = []

# Extraemos las coordenadas de la lista de puntos
for i in range(len(puntos)):
    if i%2 ==0:
        CoordenadasX.append(float(puntos[i]))
    else:
        CoordenadasY.append(float(puntos[i]))

# Imprimimos las coordenadas de los puntos en el formato (a,b)
print("Los puntos son: ")
for i in range(len(CoordenadasX)):
    print("("+str(CoordenadasX[i])+" , "+str(CoordenadasY[i])+")")

# Armamos la matriz nxn de la expresion 4 del PDF
def formarMatriz():
    # Obtenemos la cantidad de puntos
    N = len(CoordenadasX)
    # Armamos la matriz
    for i in range(filas):          
        for j in range(filas):      
            # La primera fila la formamos por separado
            if i == 0 and j == 0:
                    matriz[i][j] = N
            elif i==0:
                for k in range(len(CoordenadasX)):
                    matriz[i][j] += pow(CoordenadasX[k],j)
            # Las demas filas las formamos juntas
            else:
                for k in range(len(CoordenadasX)):
                    matriz[i][j] += pow(CoordenadasX[k],(i+j))
                
# Armamos las soluciones de la matriz 4 del PDF
def formarSoluciones():
    for i in range(len(soluciones)):      
        for k in range(len(CoordenadasY)):
            soluciones[i] += pow(CoordenadasX[k],i)*CoordenadasY[k]

# Imprimir la matriz
def imprimirMatriz(matriz, filas):
    for i in range(filas):
        print("[", end=" ")
        for j in range(filas):
            #imprime el numero redondeado por 2 cifras
                print(round(matriz[i][j],2), end="\t")
        print("| "+str(round(soluciones[i],2))+" ]")

# Metodo para imprimir el polinomio
def imprimirPolinomio(x):
    polinomio = f"{round(x[-1],3)}x^{len(x)-1} "

    for i in reversed(range(2, len(x)-1)):
        if x[i] < 0:
            polinomio += f"{round(x[i], 3)}x^{i} "
        else:
            polinomio += f"+ {round(x[i], 3)}x^{i} "

    if x[1] < 0:
        polinomio += f"{round(x[1], 3)}x "
    else:
        polinomio += f"+ {round(x[1], 3)}x "

    if x[0] < 0:
        polinomio += f"{round(x[0], 3)} "
    else:
        polinomio += f"+ {round(x[0], 3)} "

    print("El polinomio es: ")
    print(polinomio)

# Metodo para sacar la recta de regresion
def minimosCuadrados(CoordenadasX, CoordenadasY):
    sumx = sumy = sumxy = sumx2 = 0  
    n = len(CoordenadasX)  # Cantidad de puntos

    for i in range(n):     # Se ejecutan cada una de las sumas
        sumx += CoordenadasX[i] # Suma de las coordenadas en x
        sumy += CoordenadasY[i] # Suma de las coordenadas en y
        sumxy += CoordenadasX[i]*CoordenadasY[i]    # Suma de los productos x*y
        sumx2 += pow(CoordenadasX[i], 2)            # Suma de los cuadrados de x

    promx = sumx/n  # Promedio de x
    promy = sumy/n  # Promedio de y

    # Calcula la pendiente (a1) - Tomado de Chapra
    a1 = (n * sumxy - sumx*sumy)/(n * sumx2 - sumx**2)
    a0 = promy - a1*promx  # Calcula el intercepto (a0) - Tomado de Chapra

    return a1, a0

# -----------------------------------------MAIN----------------------------------------------------------
grado = int(input("Grado del polinomio que deseas ajustar (>0): "))

# Polinomio de grado n, el sistema es (n+1)*(n+1)
filas = grado + 1

# Declaramos nuestra matriz vacia
matriz = []
# Declaramos nuestro vector de soluciones
soluciones = []
# Construimos nuestra matriz, introduciendo 0 en ella e introducimos 0 en el array
for i in range(filas):            
    matriz.append([0]*filas)      
    soluciones.append(0)

# Mandamos a llamar nuestros metodos
formarMatriz()
formarSoluciones()
imprimirMatriz(matriz, filas)

# Resolvemos el sistema de ecuaciones
x = np.linalg.solve(matriz,soluciones)

# Imprimimos nuestros resultados
print("===========================================", end="\n")
# Imprimimos el polinomio
imprimirPolinomio(x)
# Mandamos llamar nuestro metodo para obtener los valores de la recta
a1, a0 = minimosCuadrados(CoordenadasX, CoordenadasY)
# Imprimimos la recta de regresion
print("La recta de regresion es: ")
print("y = " + str(a1) + "x + " + str(a0))  # y = a1x + a0
print("===========================================")

t = np.poly1d([a1, a0])
#Propiedades de la grafica
plt.scatter(CoordenadasX, CoordenadasY, alpha=1, color="orange")
# Grafica de la recta de regresion
plt.plot(CoordenadasX, a1*np.array(CoordenadasX) + a0, label=t)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.grid()
plt.show()