import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns




'''Finalmente, veamos cómo graficar una única columna con grupos separados. 
Para ello, se ocupa otra columna que actúa como variable semántica para establecer las separaciones.'''

life_expect=pd.read_csv('../data/LifeExpectancyMale.csv')
metadata=pd.read_csv('../data/Metadata.csv')

#union de histogramas

merged_df = pd.merge(left=metadata,right=life_expect,left_on='Country Code',right_on='Country Code')

print(merged_df)

'''Del dataframe resultante, sería interesante conocer la distribución del indicador por 
grupo de ingresos. Un modo de hacerlo es a través de la función hist() de Pandas, que crea histogramas
 de las columnas numéricas del dataframe, incluso separadas por una variable de agrupación o semántica. 
Esta función es diferente a la que se ha utilizado hasta ahora: plot(kind='hist') o plot.hist(), veamos cómo:'''

#El parámetro by genera la separación entre las filas de una columna seleccionada
merged_df['2019'].hist(by=merged_df['IncomeGroup'],figsize=(10,10))

'''Seaborn también permite dividir en grupos el conteo de valores de una misma columna, haciendo uso del parámetro hue. 
A diferencia de hist(), coloca la información de los cuatro grupos en el mismo histograma.
merged_df['2019'].hist(by=merged_df['IncomeGroup'],figsize=(10,10))
'''

sns.histplot(x='2019',data=merged_df,hue='IncomeGroup')

#diferentes estios de graficos de histograma con seaborn
sns.histplot(x='2019',data=merged_df, hue='IncomeGroup',multiple='stack')
sns.histplot(x='2019',data=merged_df, hue='IncomeGroup',multiple='dodge')
sns.histplot(x='2019',data=merged_df, hue='IncomeGroup',multiple='fill')
'''
También es posible con Seaborn separar las agrupaciones semánticas en gráficos independientes,
 ocupando la interfaz displot e indicándolo en el parámetro col.
merged_df['2019'].hist(by=merged_df['IncomeGroup'],figsize=(10,10))
'''
sns.displot(kind='hist',x='2019',col='IncomeGroup',data=merged_df)

plt.show()