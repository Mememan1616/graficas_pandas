import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np


users_net=pd.read_csv('../data/InternetUsers.csv')

mexico=users_net.loc[users_net['Country Name']=='Mexico']

#mexico=mexico.drop('Country Code',axis=1)
mexico=mexico.drop('Country Name',axis=1)
mexico=mexico.drop('Country Code',axis=1)

mexico=mexico.T

mexico = mexico.rename(columns={mexico.columns[0]: 'Internet Users'})
mexico.index.name='Years'


'''
A la función add_subplot() se le pasan tres números: los dos primeros indican la dimensión de la matriz, 
en este caso 2 x 3; y el último indica la posición de la subgráfica en dicha matriz, en este caso la 1. 
Las posiciones se numeran consecutivamente de izquierda a derecha, como se muestra a continuación:
'''

fig = plt.figure(figsize=(20,10))
fig.suptitle('Internet users', fontsize=16)

ax1 = fig.add_subplot(231)
ax1.plot(mexico)
ax1.set_xticks(np.arange(0,len(mexico)+1,5))
ax1.set_title('Mexico')

ax2 = fig.add_subplot(233)
users_net['2019'].plot.hist(ax=ax2)
ax2.set_title('World 2019')

ax3 = fig.add_subplot(234)
sns.boxplot(y='2019',data=users_net,orient='h',ax=ax3)
ax3.set_title('World 2019')

ax4 = fig.add_subplot(235)
ref = users_net[(users_net['Country Code']=='MEX') | (users_net['2019']==users_net['2019'].min()) | (users_net['2019']==users_net['2019'].max())]
ref.set_index('Country Name',inplace=True)
ref = ref.drop('Country Code',axis=1)
ref['2019'].plot(kind='bar',ax=ax4)
ax4.set_title('Min/Max references')



users_net.loc[:,'2012':'2017'].plot.hist(subplots=True,layout=(2,3),figsize=(20,10),sharey=True)

plt.show()