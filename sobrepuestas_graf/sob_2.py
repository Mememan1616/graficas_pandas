import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

gni=pd.read_csv('../data/GNI.csv')
internet=pd.read_csv('../data/InternetUsers.csv')

internet=internet.drop(columns=['Country Code'])
gni=gni.drop(columns=['Country Code'])

 

mexico_internet_users=internet.loc[internet['Country Name']=='Mexico']
mexico_internet_users=mexico_internet_users.drop(columns=['Country Name'])

mexico_internet_users=mexico_internet_users.T

mexico_internet_users.index=mexico_internet_users.index.astype(int)
mexico_internet_users.index.name='Years'
mexico_internet_users=mexico_internet_users[mexico_internet_users.index >= 1990]
mexico_internet_users.columns=['Internet Users']



mexico_gni=gni.loc[gni['Country Name']=='Mexico']
mexico_gni=mexico_gni.drop(columns=['Country Name'])
mexico_gni=mexico_gni.T
mexico_gni.index=mexico_gni.index.astype(int)
mexico_gni.columns=['GNI']

mexico_gni=mexico_gni[mexico_gni.index >= 1990]
mexico_gni.columns.name='GNI'
#print(mexico_gni)

#en este caso graficamos los usuarios de internet y el gni de mexico por separado
#Sin embargo estan de forma individual, asi que trataremos de unirlos
'''mexico_internet_users.plot() 
mexico_gni.plot()
'''


#La union de los dos dataframes en una grafica es asi
mexico = pd.concat([mexico_internet_users,mexico_gni],axis=1)
mexico.index.name='Years'

mexico.columns=['Internet Users', 'GNI']
print(mexico)
#mexico.plot(legend=True)

'''
Al unir ambas graficas en una sola tenemos un problema y es que los indicadores son demasiado grandes para los usuarios de internet
por lo que solo vemos una linea recta en numero bajos y no se puede aprecia los cambios de sus datos
'''

'''
Es aqui donde se pueden implementar los ejes duales
Es decir dos medidores de datos diferentes para poder apreciar ambas graficas
'''

#Ejes duales
'''
twinx
Esta función crea un eje x invisible y un eje y independiente opuestamente posicionado al original, es decir, a la derecha. 
En este caso, los ejes y's son considerados gemelos al compartir el eje x.
fig,ax1 = plt.subplots()
ax2 = ax1.twinx()
'''

'''
twiny
Esta función crea un segundo eje x en la figura, que comparte el eje y con el eje x original.
fig,ax1 = plt.subplots()
ax2 = ax1.twinx()
'''

#con matplotlib
'''
fig,ax1 = plt.subplots()
 
ax1.plot(mexico_internet_users.index , mexico_internet_users.values,label='Internet users' , color='red')
ax1.set_ylabel('Internet users')
 
ax2 = ax1.twinx()
ax2.plot(mexico_gni.index, mexico_gni.values,label='GNI',color='steelblue')
ax2.set_ylabel('GNI')
 
fig.legend(bbox_to_anchor=(0.37,0.83))
'''
'''
#con pandas
ax1 = mexico_internet_users.plot()
ax1.set_ylabel="Internet Users"
ax1.legend(loc='upper left')
 
ax2 = ax1.twinx()
mexico_gni.plot(ax=ax2,color='red')
ax2.set_ylabel='GNI'
ax2.legend(loc='upper right')
'''
#con seaborn
ax1 = sns.lineplot(data=mexico_internet_users, color='r')
ax1.set_ylabel('Internet users',color='red')
ax1.legend('')
 
ax2 = ax1.twinx()
sns.lineplot(data=mexico_gni,ax=ax2,palette=['steelblue'])

ax2.legend('')
ax2.set_ylabel('GNI',color='steelblue')
 
#plt.xticks(np.arange(0,len(mexico)+1,5))

'''
Es posible también cambiar las propiedades de las cuadrículas para diferenciar cuál pertenece a cada eje y:
'''

ax1.grid(linestyle=':',linewidth=1) 
ax2.grid(linestyle='--',linewidth=1)

plt.show()

