import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

population_years=pd.read_csv('../data/Population.csv')

# Eliminar espacios en nombres de columnas
population_years.columns = population_years.columns.str.strip()

population_years= population_years.loc[population_years["Country Name"].isin(['Mexico','Canada','Australia','Japan','United States']),['Country Code', 'Country Name','2017','2018','2019']]
population_years.set_index('Country Code', inplace=True)
#print(population_years)
population_years.plot(kind='bar', ylabel="Poblacion")

population_sex=pd.read_csv('../data/Population.csv')
population_sex=population_sex.loc[population_sex['Country Name']=='Mexico', '2017':'2019']
population_sex=population_sex.T
print(population_sex)
#sns.catplot(kind='bar',x=population_years.index,y='2019',data=population_years,palette='bright',hue='Country Name')

plt.show()