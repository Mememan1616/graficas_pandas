import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

population_2019=pd.read_csv('../data/Population.csv')

# Eliminar espacios en nombres de columnas
population_2019.columns = population_2019.columns.str.strip()

#En este caso le decimos que filas de la columna country name tomara en cuenta y despues le diremos que columnas mostrara
population_2019=population_2019.loc[
                    population_2019["Country Name"].isin(['Mexico','Canada','Australia','Japan','United States']),['Country Code','Country Name','2019']
                    ]
population_2019.set_index('Country Code',inplace=True)



#print(population_2019)


#Matplotlib
#con plt. le decimos que tipo de grafico sera
plt.bar(population_2019.index,'2019',data=population_2019)


#Pandas
#population_2019.plot(kind='bar')

#seaborn
#barra lateral
sns.barplot(x='2019',y='Country Name',data=population_2019,orient='h',palette='pastel')
sns.set_theme()

#barra comun
sns.catplot(kind='bar',x=population_2019.index,y='2019',data=population_2019,palette='bright',hue='Country Name')
sns.set_theme()
plt.show()