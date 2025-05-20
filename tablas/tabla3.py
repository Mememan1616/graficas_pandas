import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

languages=pd.read_csv('../data/Languages.csv')

some_languages = languages.loc[languages['Language'].isin( 
['Spanish','English','Chinese','French','Russian','Italian', 
'German'])]


#print(some_languages)
'''
sns.countplot(x='Language',data=some_languages ,palette='bright') 
plt.xticks(rotation=90) 
'''

counts_isofficial = some_languages.groupby(['IsOfficial','Language']).count()[['CountryCode']] 
counts_isofficial.columns=['Count']


'''Acomoda la información de forma tal que los conteos queden en columnas independientes 
haciendo diferenciación por el valor de la columna IsOfficial:'''
counts_isofficial = counts_isofficial.iloc[:7,:].merge(counts_isofficial.iloc[7:,:], 
on='Language',suffixes=('_F', '_T'))[['Count_F','Count_T']] 
counts_isofficial.columns =['NonOfficial','Official']

print(counts_isofficial)


#counts_isofficial.plot.bar(xticks=[],xlabel='')
#sns.barplot(palette='Set1',data=counts_isofficial, x='Language')


'''
 Para indicar los colores en la tabla, es necesario que uses la función table() de Matplotlib 
porque plot() de Pandas no permite tal nivel de personalización. No olvides que, en este 
caso, tendrás que ocupar la propiedad T para obtener la transpuesta: 
'''
counts_isofficial.plot.bar(xticks=[],xlabel='',legend='') 
counts_isofficial_T = counts_isofficial.T 

t=plt.table(cellText=counts_isofficial_T.values,
          colLabels=counts_isofficial_T.columns,
          #ubicacion de la tabla
          loc='upper right',
          rowLabels=counts_isofficial_T.index,
          rowColours=['tab:blue','tab:Orange'],
          
) 

'''Aunque en todos los ejemplos previos ubicamos la tabla en el eje horizontal, para utilizar los 
encabezados de columna como marcas del eje, la posición de la tabla puedes cambiarla a 
través del parámetro loc:'''

t.scale(0.8,1) 



'''
Incluso puedes crear una figura sin gráfico con la función subplot(), en la que únicamente 
incluyas la información contenida en la tabla:
 
'''
counts =pd.DataFrame(some_languages['Language'].value_counts())
counts_T=counts.T

fig,ax = plt.subplots(1,1)
ax.axis('off')
ax.table(cellText=counts_T.values,colLabels=counts_T.columns,loc='center')
plt.show()