import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
#lee el documento de CSV
alcohol=pd.read_csv('../data/AlcoholConsumption.csv')


#Crea un df con solo los datos de mexico
mexico=alcohol[alcohol['country']=='Mexico']
mexico.set_index('country',inplace=True)

'''----Secccion de analizar los datos de cada columna, para ello se utilizan histogramas,
ya que son la mejor opcion para visualizar todos los datos de una columna con muchas filas---------'''
#print(mexico)
#crea un histograma con todas las columnas, cada columna es un histograma diferente en la misma figura
'''
'alcconsumption', 'incomeperperson', 'suicideper100th',
'employrate', 'urbanrate'
'''
axs=alcohol.hist(layout=(1,5),figsize=(25,3))
#con shape[1] podemos obtener la extension del arreglo, el cual nos dira cuantas columnas tiene el DF
print(axs.shape[1])
#con este for se recorre todas las columnas del DF empezando por el 1 para esquivar el index
for i in range(axs.shape[1]):
    #lo que hacemos aqui es localizar la fila 0 del DataFrame Mexico, y recorrer todos los datos de sus columnas
    #df.iloc[y,x]
    print(mexico.iloc[0,i])

    #crea un texto encontrando el punto del eje x que corresponde a mexico, y en y se coloca 0 para que quede en la parte inferior
    #del DF
    axs[0,i].text(mexico.iloc[0,i],0,'MEX',  weight='bold',color='white')
    



plt.show()