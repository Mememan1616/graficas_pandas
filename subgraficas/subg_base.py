import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


#con ello podemos generar varias graficas en una matriz
#el primer numero indica el numero de columna y el segundo de renglones



#La funcion figsize indica el tamaño de la grafica
#sharex y sharey se aplica si se quieren compartir los mismos ejes para las graficas

'''
True o 'all': las subgráficas comparten todos los ejes.
 False o 'none': cada subgráfica posee sus propios ejes.
 'row': cada fila de gráficas compartirá el eje indicado.
 'col': cada columna de gráficas compartirá el eje indicado.
'''
fig,ax2= plt.subplots(2,3, figsize=(8,8),sharex='col',sharey='all', )


#Ajusta la separacion entre las graficas
plt.subplots_adjust(wspace=0.4,hspace=0.6)


'''

También se pueden crear matrices con subgráficas de tamaño irregular usando la función subplot2grid(), 
que recibe los siguientes parámetros:

shape: la forma de la matriz. Por ejemplo, de 3 x 3 – (3,3)
loc: la ubicación del gráfico dentro de la misma. Por ejemplo, en la primera fila, segunda columa – (0,1)
rowspan: el número de filas para que el eje se extienda hacia la derecha.
colspan: el número de columnas para que el eje se extienda hacia abajo.

'''

fig,axs = plt.subplots(3,3,figsize=(10,10)) 
ax1 = plt.subplot2grid((3,3),(0,0),colspan=3) 
ax2 = plt.subplot2grid((3,3),(1,0),colspan=2) 
ax3 = plt.subplot2grid((3,3),(1,2),rowspan=2)
ax4 = plt.subplot2grid((3,3),(2,0)) 
ax5 = plt.subplot2grid((3,3),(2,1))

plt.show()