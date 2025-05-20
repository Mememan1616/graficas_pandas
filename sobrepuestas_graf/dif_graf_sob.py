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


#ahora veremos como usar dos graficos diferentes al mismo tiempo
ax1 = mexico_internet_users.loc['2009':'2019'].plot(rot=90,marker='o')
ax1.legend(loc='upper left')
ax1.set_yticks(np.arange(0,101,10))
 
ax2 = ax1.twinx()
mexico_gni.loc['2009':'2019'].plot(kind='bar',ax=ax2,color='None',edgecolor='steelblue')
ax2.legend(loc='upper right')
ax2.set_yticks([5000,9000,11000])

plt.show()