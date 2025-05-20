import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


languages=pd.read_csv('../data/Languages.csv')

#filtran el grafico para obtener los los paises con cierto codigo y que estos hablen español
#y solo obtener las columnas de porcentaje y codigo de pais

mexico_borders = languages.loc[(languages['CountryCode'].isin(['MEX','USA','BLZ','GTM'])) & 
(languages['Language']=='Spanish'),['CountryCode','Percentage']] 


mexico_borders.set_index('CountryCode',inplace=True)

print(mexico_borders)



#sns.barplot(x=mexico_borders.index,  
#y='Percentage',data=mexico_borders ,palette='pastel') 

'''
Puedes indicar la ubicación seleccionando un sistema de coordenadas diferente a través del
 parámetro transform. Este te permite posicionar el texto en:
'''
#Un pixel en específico:  
mexico_borders['Percentage'].plot.bar() 
#Eje x en pixeles, eje y en pixeles , 'texto', transform=None
#se indica en todo el cuadro
plt.text(220,150,'92.1%',transform=None)
plt.title('Texto con pixel')
 
 
#Relación a los ejes: 
ax = mexico_borders['Percentage'].plot.bar()
#Eje x donde el extremo es 1, eje y  donde el extremo es 1 , 'texto', transform=ax.transAxes
# su rango se limita a solo el grafico y la zona de las graficas no a toda la figura
plt.text(0.58,0.58,'92.1%',transform=ax.transAxes)
plt.title('Texto con ejes')

 
#Relación a la figura: 
fig,ax = plt.subplots() 
mexico_borders['Percentage'].plot.bar(ax=ax)
#Eje x donde el extremo es 1, eje y  donde el extremo es 1 , 'texto', transform=ax.transAxes
#Se encarga de toda la figura 
plt.text(0.58,0.5,'92.1%',transform=fig.transFigure,
         #En esta parte se añade su estilo
        family='serif',
        fontsize=18,
        fontweight='bold',
        style='italic', 
        color='red',
        horizontalalignment='center'
         )

#se puede crear el estilo usando un diccionario

props_font = {'family': 'serif', 
         'size': 18, 
         'weight': 'bold', 
         'style': 'italic', 
         'color': 'blue', 
         'horizontalalignment': 'center'} 
plt.text(2,92.1,'92.1%',fontdict=props_font)

plt.title('Texto con Relacion a la figura')


'''El texto también puedes resaltarlo a través de un objeto bbox, que posee entre sus propiedades el
 nivel de transparencia (alpha) y el espacio entre el contenido y el borde del elemento (pad):
 '''
plt.text(2,80.1,'92.1%',bbox=dict(facecolor='red',alpha=0.3,pad=5))



 
'''
Puedes especificar, además, el tipo de contenedor e indicar las propiedades creando previamente 
el diccionario:'''

props_bbox = {'boxstyle': 'circle',
 'facecolor': 'blue',
 'alpha': 0.3}

plt.text(2,70.1,'92.1%',bbox=props_bbox)


'''
Algunos otros valores del estilo son: 
'larrow' flecha izquierda, 
'rarrow' flecha derecha,  
'round' rectángulo con bordes redondeados
'''

plt.show()