import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

gni=pd.read_csv('../data/GNI.csv')
lifexp_male=pd.read_csv('../data/LifeExpectancyMale.csv')
'''Gross National Income) que almacena este indicador, por país, desde 1960. 
Los valores indican el ingreso nacional bruto, 
convertido a dólares estadounidenses, dividido por la población a mitad de año.'''
#print(gni)

#Grafiquemos un scatter plot de ambos indicadores para el año 2019, utilizando Matplotlib:
plt.scatter(x=gni['2019'],y=lifexp_male['2019'])
'''Observa que la diferencia entre las escalas de los ejes es considerable. Por una parte, los años se muestran con decenas, 
mientras que el ingreso llega a centenas de miles. Además, este último cubre un rango muy grande (de 0 a 120000).'''

'''
Cuando esto ocurre, una escala logarítmica ayudará con un rango más manejable y
 mostrará mejor la relación entre las variables graficadas:

'''
plt.scatter(x=gni['2019'],y=lifexp_male['2019'])
plt.xscale('log')


'''
a expectativa de vida crece a medida que crece el ingreso, es decir, las variables tienen correlación positiva.
 Para calcular el coeficiente de correlación, Pandas provee la función corr(),
 que determina la correlación de columnas por pares, excluyendo los valores nulos.
'''
corr = gni['2019'].corr(lifexp_male['2019'])
#print(corr)



plt.show()