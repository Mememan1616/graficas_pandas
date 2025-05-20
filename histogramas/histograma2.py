import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


Exp_vid=pd.read_csv('../data/LifeExpectancyMale.csv')
#birth.columns=birth.columns.str()

#Toma solo la columna del año 2019
life_expect_2019=Exp_vid["2019"]


#Crear histogramas multiples en uno solo

#matplotlib
plt.hist('1960',data=Exp_vid,label='1960')
plt.hist('2019',data=Exp_vid,label='2019')
plt.legend()

#pandas
Exp_vid['1960'].plot.hist(label='1960',alpha=0.5)
Exp_vid['2019'].plot.hist(label='2019',alpha=0.5)
plt.legend()

#seaborn
'''La herramienta fill marca si el grafico estara relleno de color o sera solo el contorno'''
sns.histplot(x='1960',data=Exp_vid,color='blue',label='1960',element='step',fill=False)
sns.histplot(x='2019',data=Exp_vid,color='orange',label='2019',element='step',fill=False)
plt.legend()

plt.show()