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

#print(mexico_internet_users)

mexico_gni=gni.loc[gni['Country Name']=='Mexico']
mexico_gni=mexico_gni.drop(columns=['Country Name'])
mexico_gni=mexico_gni.T
mexico_gni.index=mexico_gni.index.astype(int)
mexico_gni.index.name='Years'
mexico_gni.columns=['GNI']

mexico_gni=mexico_gni[mexico_gni.index >= 1990]
mexico_gni.columns.name='GNI'

#print(mexico_gni)


fig,ax1 = plt.subplots()
 
 #en este caso se intercambio como eje comun el eje y 
ax1.plot(mexico_internet_users.values,mexico_internet_users.index,label='Internet users', color='red')
ax1.set_xlabel('Internet users')
 
ax2 = ax1.twiny()
ax2.plot(mexico_gni.values,mexico_gni.index,label='GNI',color='steelblue')
ax2.set_xlabel('GNI')
 
fig.legend(bbox_to_anchor=(0.37,0.87))
#plt.yticks(np.arange(0,len(mexico)+1,5))
plt.show()