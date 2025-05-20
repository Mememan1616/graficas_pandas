import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

gdp=pd.read_csv('../data/GDP.csv')
desempleado=pd.read_csv('../data/Unemployment.csv')

gdp_2019=gdp[['Country Code', '2019']]
desempleado_2019=desempleado[['Country Code', '2019']]
merge=gdp_2019.merge(desempleado_2019, on='Country Code', suffixes=('_gdp','_desempleado'))

#print(merge)

sns.set_palette('Spectral')
sns.set_style('ticks')

#Crearemos un histograma que muestre la correlacion del gdp y el desempleo

#se crea una variable llamado fig y ax1 para crear varias graficas en una sola
fig,ax1 = plt.subplots() 
#ax1 solo toma los datos de la columna del gdp
ax1.hist(x='2019_gdp',data=merge,alpha=0.5,label='GDP') 
ax1.set_xlabel('GDP')
ax1.set_ylabel('Frecuency')

#con ax2 creamos una copia de 
ax2 = ax1.twiny() 
ax2.hist(x='2019_desempleado',data=merge,color='darkseagreen',alpha=0.5,label='Unemployment')
ax2.set_xlabel('Unemployment')

plt.title('World 2019')
fig.legend(bbox_to_anchor=(0.86,0.87))
plt.show()
'''
plt.hist(x='2019_gnp',data=merge, alpha=0.5,label='GNP')
plt.hist(x='2019_desempleado',data=merge, color='darkseagreen',alpha=0.5,label='Desempleados')
plt.legend()
plt.show()'''

#parte 2 del pruebate

continentes= pd.read_csv('../data/Continents.csv')

continentes_2019=continentes.merge(merge, on='Country Code')

print(continentes_2019)
#Creamos una matriz donde poder almacenar diferentes graficas con subplot
fig = plt.figure(figsize=(17,5)) 
plt.subplots_adjust(wspace=0.4)

ax1 = fig.add_subplot(131)
continentes_2019.plot(kind='scatter',x='2019_gdp',y='2019_desempleado',color='indianred',logx=True,ax=ax1)
ax1.set_title('World 2019')


#plt.scatter(x=continentes_2019['2019_gdp'], y=continentes_2019['2019_desempleado'], label=['GDP'])
#plt.xscale('log')



plt.show()