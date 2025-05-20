import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


languages=pd.read_csv('../data/Languages.csv')

#filtran el grafico para obtener los los paises con cierto codigo y que estos hablen español
#y solo obtener las columnas de porcentaje y codigo de pais

mexico_borders = languages.loc[(languages['CountryCode'].isin(['MEX','USA','BLZ','GTM'])) & 
(languages['Language']=='Spanish'),['CountryCode','Percentage']] 


mexico_borders.set_index('CountryCode',inplace=True)


'''
la inclusión de texto, sin referencia a una propiedad en particular del gráfico,
es también posible mediante la especificación de las coordenadas de ubicación de este,
lo cual permite incrementar la expresividad
de la representación al resaltar zonas o dirigir la atención de los receptores a ciertos resultados.

La función text() de Matplotlib recibe como parámetros la posición y la cadena de 
texto a escribir; y puedes usarla en cualquier gráfico, independientemente de la 
plataforma de trazado que hayas empleado. 



'''
'''
#Matplot
plt.bar(mexico_borders.index ,'Percentage',data=mexico_borders)  

#Pandas
mexico_borders.plot(kind='bar')
'''
#seaborn
sns.barplot(x=mexico_borders.index,  
y='Percentage',data=mexico_borders ) 


'''
La transformación predeterminada especifica que el texto está en coordenadas de datos,
 Como alternativa, puede especificar texto en las coordenadas de los ejes ((0, 0) es
abajo a la izquierda y (1, 1) es arriba a la derecha). El siguiente ejemplo coloca texto en el centro de los ejes:

text(0.5, 0.5, 'matplotlib', horizontalalignment='center',
     verticalalignment='center', transform=ax.transAxes)
'''


'''
Observa de la función text() que, por defecto, las coordenadas donde se ubica el 
texto están especificadas en coordenadas de datos: 2 en el eje horizontal porque MEX 
está en la posición 2 (la serie inicia en 0 para los gráficos de barras) y 92.1 en el eje 
vertical, que corresponde al porcentaje que queremos representar. Pero si en lugar de 
indicar los valores fijados, la información se extrae del dataframe, el código a emplear 
sería el siguiente:'''

#plt.text(2,92.1,'92.1%')


'''
Así, para la ubicación en el eje x se busca 'MEX' porque, en este caso, el 
CountryCode es el índice en el dataframe; y para el eje y, el valor extraído con la 
función loc() que es value = 92.
'''
value = mexico_borders.loc['MEX','Percentage'] 



'''Pero ¿qué pasaría si no conoces directamente el índice a buscar y lo tienes que extraer 
de una condición? Por ejemplo, si desearas representar el valor del porcentaje máximo 
en el dataframe (que en este caso coincide con MEX):'''

value = mexico_borders.loc[mexico_borders['Percentage']==mexico_borders['Percentage'].max(), 'Percentage']

#en el value anterior nos envio 
value = value.to_list()[0] 

plt.text('MEX',value,str(value)+'%')
plt.show()
