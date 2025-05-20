import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


languages=pd.read_csv('../data/Languages.csv')


'''
Habrá casos en los que además de ubicar un texto en una posición determinada del gráfico,
 necesites puntualizar en alguna característica. Para ello, puedes usar la función annotate(), que
 además de considerar la ubicación del texto, recibe la ubicación de la anotación. Ambas
 ubicaciones deben ser enviadas como tuplas (x,y). Para probar su funcionamiento, veamos cómo
 están distribuidas todas las lenguas en México:
'''
mexico = languages.loc[languages['CountryCode']=='MEX',['Language','Percentage']] 
mexico.set_index('Language',inplace=True)

#print(mexico)

'''
Usaremos un gráfico circular para representarlas, pero antes incluyamos una nueva categoría 
(Others) para completar el 100% de los hablantes:
 
'''
mexico.loc['Others']=[100 - mexico['Percentage'].sum()] 

#mexico.plot.pie(y='Percentage',labels=mexico.index,rotatelabels=True,figsize=(8,8))

#tomamos solo las lenguas sin contar español
mexico_unofficial = mexico.drop(mexico.loc[mexico.index=='Spanish'].index) 
mexico_unofficial.plot.pie(y='Percentage',labels=mexico_unofficial.index,autopct='%1.1f%%') 

#hacemos una anotacion de flecha señando la coordenada 0,0 que es el centro del grafico pastel
#xy punto que señala flecha xytext coordenada donde ira el texto
plt.annotate('(0,0)',xy=(0,0),xytext=(1,1),arrowprops=dict(arrowstyle='->')) 

'''
 Hay muchos estilos de flecha:
 '-' sin saeta, 
 '-[' corchete en la anotación, 
 '|-|' líneas en ambos extremos, 
 '<-' saeta en el texto, 
 '-|>' saeta completa en la anotación 
'''
plt.annotate('(0,0)',xy=(0,0),xytext=(-1,-1), 
arrowprops=dict(arrowstyle='<->', connectionstyle='angle3',color='maroon'))



'''
Si no estableces el estilo, puedes detallar otras propiedades para la flecha. Como en casos
 anteriores, el diccionario puede ser definido antes:

'''

props_arrow = {'facecolor':'white', 
'width':0.5, 
'headwidth':8, 
'headlength':8} 
plt.annotate('1.8% including Spanish', xy=(0.45,0.58),xytext=(1,0.6),arrowprops=props_arrow )


plt.show()