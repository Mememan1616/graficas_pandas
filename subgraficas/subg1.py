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

#print(mexico)


#en matplotlib
fig,axs = plt.subplots(2,2,figsize=(10,10))
axs[0,1].plot(mexico)
axs[0,1].set_xticks(np.arange(0,len(mexico)+1,5))

#pandas
fig,axs = plt.subplots(2,2,figsize=(10,10))
mexico.plot(ax=axs[0,1])


#seaborn
#fig,axs = plt.subplots(2,2,figsize=(10,10))
#sns.lineplot(data=mexico,ax=axs[0,1])
#axs[0,1].set_xticks(np.arange(0,len(mexico)+1,5))

#se agregan el titulo a cierta parte de la matriz
axs[0,1].set_title('Mexico')
axs[0,1].set_xlabel('Year')


'''
Revisemos ahora un modo alternativo para hacer referencia a las subgráficas 
sin usar la posición que ocupan en la matriz. Esto es posible únicamente cuando son pocas subgráficas. 
Cada una de ellas se nombra durante la creación del contenedor. Para el ejemplo anterior de 2 x 2 quedaría de la 
siguiente manera:

'''
fig,((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2,figsize=(10,10))
ax2.plot(mexico)


plt.show()

