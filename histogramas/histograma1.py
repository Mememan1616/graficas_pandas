import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


Exp_vid=pd.read_csv('../data/LifeExpectancyMale.csv')
#birth.columns=birth.columns.str()

#Toma solo la columna del año 2019
life_expect_2019=Exp_vid["2019"]

#print(life_expect_2019)

#crea la grafica de histograma con matplotlib
plt.hist(life_expect_2019)

#Con pandas
life_expect_2019.plot.hist()
life_expect_2019.plot(kind='hist')

#Con seaborn
sns.histplot(x=life_expect_2019)


'''De forma base siempre crean histogramas de 10 barras para visualizar los rangos de datos
pero tambien se pueden definir el numero de barras o rangos de datos
para los histogramas se debe definir la columna de X'''

plt.hist('2019',data=Exp_vid,bins=5)

'''Si se especifica una secuencia que define los bordes de las
 clases, por ejemplo, haciendo 10 clases cada una con una anchura de 10 años, se obtendría:'''

life_expect_2019.plot(kind='hist',bins=[0,10,20,30,40,50,60,70,80,90,100])


'''range (para Matplotlib y Pandas) / binrange (para Seaborn)
Establece el límite inferior y superior a considerar. Los valores fuera de este rango se ignoran.
* Se ocupó la paleta Set1.
plt.hist('2019',data=lifexp_male,range=(60,80))
range (para Matplotlib y Pandas) / binrange (para Seaborn)
'''
plt.hist('2019',data=Exp_vid,range=(60,80))

'''
Establece un muestreo acumulativo
Si es True, cada bin incluye su conteo y 
el de todos los bins para valores más pequeños. '''
Exp_vid['2019'].plot(kind='hist',cumulative=True)

plt.show()