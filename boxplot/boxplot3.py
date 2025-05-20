import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


lifexp_male=pd.read_csv('../data/LifeExpectancyMale.csv')
metadata=pd.read_csv('../data/Metadata.csv')

'''
Así como en los histogramas, en los boxplots se puede graficar una única columna y ocupar otra para separarla 
en grupos. Retomando el dataframe metada, que combina el indicador de expectativa de vida, por país, 
con la región y el grupo de ingresos, se podría obtener un boxplot por región:
'''
merged_df = lifexp_male.merge(metadata,on='Country Code')

'''
Un modo de hacerlo es a través de la función boxplot() de Pandas, que permite la separación por una variable 
de agrupación. Esta función es diferente a la que se ha usado hasta ahora: plot(kind='box') o plot.box(). Observa de qué manera:

'''
merged_df.boxplot(column=['2019'],by='Region',rot=90)


#estilo 1
sns.boxplot(x='Region',y='2019',data=merged_df) 
#estilo 2
sns.boxplot(x='Region',y='2019',hue='IncomeGroup',data=merged_df)
#rotacion al 90
plt.xticks(rotation=90)
'''
Con Seaborn tambien es posible realizar estos graficos
Si el gráfico que incluye dos separaciones semánticas (con los parámetros y y hue) se muestra muy cargado, se tiene la opción de usar la interfaz catplot para dividirlo, basta con indicarlo en el parámetro col:
splot = sns.catplot(kind='box',x='Region',y='2019',col='IncomeGroup',data=merged_df);
splot.set_xticklabels(rotation=90)
'''
splot = sns.catplot(kind='box',x='Region',y='2019',col='IncomeGroup',data=merged_df);
splot.set_xticklabels(rotation=90)
plt.show()