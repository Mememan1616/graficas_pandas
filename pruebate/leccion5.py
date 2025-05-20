import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

gdp=pd.read_csv('../data/GDP.csv')
desempleado=pd.read_csv('../data/Unemployment.csv')

gdp_2019=gdp[['Country Code', '2019']]
desempleado_2019=desempleado[['Country Code', '2019']]


#estilos de graficos
sns.set_palette("Spectral")
sns.set_style('ticks')



merge=gdp_2019.merge(desempleado_2019, on='Country Code', suffixes=('_gdp','_desempleado'))

#merge.set_index('Country Code',inplace=True)

fig,ax1=plt.subplots()


ax1.hist(x='2019_gdp',data= merge, label="Desempleados")
ax1.set_xlabel('GDP')
ax1.set_ylabel('Frecuency')
ax2=ax1.twiny()
ax2.hist(x='2019_desempleado', data=merge,label='GDP', color='darkseagreen' )
ax1.set_xlabel('Desempleado')
ax1.set_ylabel('Frecuency')
plt.title('World 2019')
fig.legend(bbox_to_anchor=(0.86,0.87))


#parte 2 de pruebate

continent=pd.read_csv('../data/Continents.csv')

continent_2019=continent.merge(merge, on='Country Code')
continents_group = continent_2019.groupby(['Continent']).sum(['2019_gdp','2019_desempleado'])

fig = plt.figure(figsize=(20,10))
fig.suptitle('Leccion 5', fontsize=16)

ax3=fig.add_subplot(131)
ax3.scatter(x=continent_2019['2019_gdp'],y=continent_2019['2019_desempleado'])
ax3.set_title("World 2019")
plt.xscale('log')



ax4=fig.add_subplot(132)
sns.boxplot(x='Continent',y='2019_desempleado',data=continent_2019,ax=ax4)
ax4.set_title('Unemployment by continent 2019')




ax5=fig.add_subplot(133)
continents_group.plot.pie(y='2019_gdp', ax=ax5)
ax5.set_title('GDP por continente')
#print(continents_group)


#parte 3: Datos duales

gdp_mexico=gdp.loc[gdp['Country Name']=='Mexico']
gdp_mexico=gdp_mexico.drop(columns=['Country Name', 'Country Code'])
gdp_mexico=gdp_mexico.T
gdp_mexico.index.name='Years'
gdp_mexico.columns.name='GDP'

desempleo_mexico=desempleado.loc[desempleado['Country Name']=='Mexico']
desempleo_mexico.drop(columns=['Country Name', 'Country Code'])
desempleo_mexico=desempleo_mexico.T
desempleo_mexico.index.name='Years'
desempleo_mexico.columns.name='desempleo'

mexico=gdp_mexico.merge(desempleo_mexico, on='Years')
mexico.columns=['GDP','Desempleo']
print(mexico)

fig,ax6=plt.subplots()
ax6=mexico['GDP'].plot(color='blue')
ax6.set_ylabel='GDP'
ax6.legend(loc='upper left')


ax7=ax6.twinx()
mexico['Desempleo'].plot(ax=ax7 ,color='red')
ax7.set_ylabel='Desempleo'
ax7.legend(loc='upper right')
plt.show()