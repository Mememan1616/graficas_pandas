import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

WomanParliaments=pd.read_csv('../data/WomanParliaments.csv')

mexico=WomanParliaments.loc[WomanParliaments['Country Code']=='MEX']
mexico=mexico.drop(columns=['Country Name', 'Country Code'])
#mexico.set_index('Country Name',inplace=True)
mexico.index.name=''
mexico=mexico.T
mexico.columns=['Mexico']

#print(mexico)
#la funcion mean obtiene el promedio de una serie numerica
world = pd.DataFrame(WomanParliaments.loc[:,'1997':'2020'].mean())
world.columns = ['World']

#unir ambos DF con su index, la funcion AXIS elimina el indice de una y deja uno solo
#solo aplica si el index es igual
mex_world = pd.concat([mexico,world],axis=1)


print(mex_world)
sns.set_palette('Accent')
table=mex_world['2000':'2020':5].T


mex_world.plot(title='Woman Parliaments', xticks=[])
plt.table(
        cellText=table.values.round(),
        colLabels=table.columns,
        rowLabels=table.index,
        cellLoc='center',
        colColours=['blue']*5

)

#seccion de textos

metadata=pd.read_csv('../data/Metadata.csv')

merge=metadata.merge(WomanParliaments, on='Country Code')


data_2020=merge[['Country Code', 'Region', '2020']]

data_2020=data_2020.groupby('Region').mean('2020')
print(data_2020)

sns.barplot( x=data_2020.index, data=data_2020)
plt.show()