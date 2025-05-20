
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
gni=pd.read_csv('../data/GNI.csv')
lifexp_male=pd.read_csv('../data/LifeExpectancyMale.csv')
population=pd.read_csv('../data/Population.csv')


gni.set_index('Country Code')
lifexp_male.set_index('Country Code')
population.set_index('Country Code')

gni_2019=gni[['Country Code','2019']]
lifexp_male_2019=lifexp_male[['Country Code','2019']]
population_2019=population[['Country Code','2019']]

merged_1=gni_2019.merge(lifexp_male_2019,on='Country Code',suffixes=('_gni','_life'))
merged_2=merged_1.merge(population_2019, on='Country Code',suffixes=('','_population'))
all=merged_2

'''Adicionalmente, Pandas y Seaborn poseen funciones de trazado que operan en más de un objeto y que obtienen
 representaciones de dispersión entre todos los pares de columnas numéricas del dataframe. 
Veamos un ejemplo con un dataframe, denominado all, que contienen cuatro indicadores para el 2019 por país.'''

#pandas
#pd.plotting.scatter_matrix(all,figsize=(10,10))

#seaborn
sns.pairplot(all)

#estilo con seaborn
#sns.heatmap(round(all.corr(),2),annot=True)

plt.show()