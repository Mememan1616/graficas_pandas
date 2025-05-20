import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

languages=pd.read_csv('../data/Languages.csv')

some_languages = languages.loc[languages['Language'].isin( 
['Spanish','English','Chinese','French','Russian','Italian', 
'German'])]


print(some_languages)

'''semos una gráfica de barras para determinar el conteo o frecuencia de cada idioma. Si 
recuerdas, anteriormente revisamos que la única plataforma que ofrece una función directa de 
trazado con este fin es Seaborn: countplot(). En Matplotlib y Pandas usamos 
value_counts() como auxiliar en las funciones bar() y plot.bar(), respectivamente, 
para obtener los mismos resultados. '''

sns.countplot(x='Language',data=some_languages ,palette='bright') 
plt.xticks(rotation=90) 

'''
En la figura resultante se observa que el idioma predominante es el inglés (casi 60 países lo 
incluyen como parte de sus lenguas), seguido por el español y el francés. Ahora, si quisieras 
incluir los valores numéricos en el gráfico, podrías utilizar la función text() o una tabla de 
datos en el eje horizontal, como veremos a continuación. Pero antes, es necesario generar el 
dataframe con los conteos por idioma. Para ello, hemos utilizado ya dos formas: con la función 
value_counts() y con groupby(). Recordemos cómo:
'''
#con value counts
counts =pd.DataFrame(some_languages['Language'].value_counts())

#con groupby
counts2 =some_languages.groupby(['Language']).count()[['CountryCode']]

'''
Sin embargo, para incluir la tabla con esta información en el gráfico, el formato del 
dataframe debe coincidir con la forma que adquirirá la tabla. Viendo el gráfico de 
barras antes generado, lo más conveniente es que los idiomas se presenten de 
manera horizontal con los conteos abajo.
Esto lo puedes lograr usando la propiedad T para obtener la transpuesta:
 
'''
counts_T = counts.T

#Ahora ya es posible incluir la tabla en gráficos de barras con las tres plataformas:

#Con Matplotlib 
#plt.table(cellText=counts_T.values,colLabels=counts_T.columns)
#plt.xticks([])
#plt.xlabel('')


#pandas
#counts.plot(kind='bar',table=True,xticks=[],xlabel='',legend='')

#seaborn
'''plt.table(cellText=counts_T.values,colLabels=counts_T.columns)
plt.xticks([])
plt.xlabel('')'''



'''
Observa de los códigos anteriores que: 
En Matplotlib y Seaborn ocupamos el dataframe counts_T para construir la tabla y 
pasamos una lista vacía a la función xticks() para omitir las marcas del eje x.  
La función plot() de Pandas posee el parámetro table para incluir la tabla de datos 
directamente, sin necesidad de la transpuesta, y los parámetros xticks y xlabel para 
ocultar los valores del eje x. Sin embargo, si deseas personalizar su estructrura o 
formato, deberás usar table() de Matplotlib. 
En Seaborn ya no es necesario ocupar countplot(), como inicialmente lo hicimos, 
porque se tiene el conteo en el dataframe counts y es éste el que se grafica. 
'''

#Enfoquémonos a continuación en las propiedades de la tabla. Si quieres incluir encabezados 
#para los registros o filas, utiliza la propiedad rowLabels:
'''
plt.table(cellText=counts_T.values,
          colLabels=counts_T.columns, 
          rowLabels=counts_T.index,
          cellLoc='center',
          edges='horizontal')
plt.xticks([])
plt.xlabel('')
'''

'''
También puedes especificar la alineación de las celdas con cellLoc y podrías hacer lo mismo 
con los encabezados de filas y columnas, utilizando rowLoc y colLoc,respectivamente. 
El parámetro edges te permite indicar qué líneas de la tabla incluir. En este ejemplo, únicamente
 mostramos las horizontales, pero podrías usar: 

'open' sin líneas, 
'closed' todas las líneas, 
'vertical' líneas verticales 

Cuando la tabla posee todas las líneas (closed como valor por defecto), es posible colorear 
las celdas de los encabezados, a través de los parámetros rowColours y colColours:
'''
plt.table(cellText=counts_T.values,
          colLabels=counts_T.columns, 
          rowLabels=counts_T.index,
          rowColours=['cyan'], 
          colColours=['greenyellow']*7
          ) 
plt.xticks([])
plt.xlabel('')


plt.show()