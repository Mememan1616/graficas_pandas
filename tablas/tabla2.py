import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

languages=pd.read_csv('../data/Languages.csv')

some_languages = languages.loc[languages['Language'].isin( 
['Spanish','English','Chinese','French','Russian','Italian', 
'German'])]


print(some_languages)

sns.countplot(x='Language',data=some_languages ,palette='bright') 
plt.xticks(rotation=90) 


#con value counts
counts =pd.DataFrame(some_languages['Language'].value_counts())

#con groupby
counts2 =some_languages.groupby(['Language']).count()[['CountryCode']]

counts_T=counts.T

#ahora crearemos una tabla y cambiaremos su tamaño de letra
t = plt.table(
            #El contenido de la tabla
            cellText=counts_T.values,
            #nombre de las columnas de la tabla
              colLabels=counts_T.columns,
              #nombre de los indices de cada renglon
              rowLabels=counts_T.index,
              #color de los indices de los renglones
              rowColours=['cyan'],
              #color de los indices de las columnas 
              colColours=['greenyellow']*7
              #cellLoc='center',
              #edges='horizontal'
              ) 
t.auto_set_font_size(False) 
t.set_fontsize(12)

plt.xticks([])
plt.xlabel('')

'''
También puedes indexar directamente el objeto tabla para acceder a celdas individuales, como 
lo haces con las matrices: cell = table[row,col]. Una vez referenciada la celda, podrías 
darle el formato que desees.  
Por ejemplo, para hacer énfasis en el español, tendrías que indicar row = 1 y col = 1 
(recuerda que los índices siempre inician con 0): 

'''
cell = t[1,1] 
cell.set_text_props(weight='bold',color='white')
cell.set_facecolor('purple')



'''
Para dar formato a varias celdas, tendrías que hacer un recorrido por la tabla, usando un ciclo y 
ocupando la función get_celld(), que devuelve un diccionario de celdas con el mapeo de la 
tabla (fila, columna) a celdas:  
'''

for (row,col), cell in t.get_celld().items(): 
    if (row == 0): 
        cell.set_text_props(weight='light',style='italic') 
        cell.set_facecolor('palegreen') 
    else: 
        cell.set_text_props(weight='bold',color='white') 
        cell.set_facecolor('purple')

plt.show()