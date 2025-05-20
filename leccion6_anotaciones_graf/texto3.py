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



sns.barplot(x=mexico_borders.index,  
y='Percentage',data=mexico_borders ,palette='pastel') 
plt.title('Hablantes del Español')

#para mostrar el texto de su valor en cada barra

'''
Para incluir los valores de todos los países, es necesario que hagas un recorrido por las filas 
del dataframe con un ciclo y extraer el porcentaje de hablantes con 
mexico_borders.iloc[i,0]:
'''

for i in range(mexico_borders.shape[0]): 
    plt.text(i,mexico_borders.iloc[i,0],str(mexico_borders.iloc[i,0])+'%')


'''
Además de texto, puedes insertar líneas horizontales y/o verticales para indicar ciertos valores 
relevantes o de referencia, utilizando las funciones axhline() y axvlines(). Si en los gráficos 
anteriores quisieras añadir, por ejemplo, el promedio de hablantes del español en todos los países 
que incluyen este idioma, podrías hacer:
'''
spanish_mean = (languages.loc[languages['Language']=='Spanish','Percentage']).mean() 
plt.axhline(y=spanish_mean,color='red',linestyle=':') 
#plt.text(-0.5,spanish_mean,str(f'{spanish_mean:.2f}')+'%') 

'''
Para incluir expresiones matemáticas, puedes usar un subconjunto del sistema de tipografía         . 
Para ello, deberás utilizar cadenas sin formato precedidas con una r antes de las comillas y rodear
 el texto matemático con el signo de peso ($). El texto normal y el texto matemático se pueden
 intercalar dentro de la misma cadena.
 Si en el gráfico anterior, desearas incluir la fórmula que calcula el valor (66.05%) como
'''

plt.text(-0.4,spanish_mean,r'$\frac{\sum_{i=1}^\# percentage_i}{\#}=$'+str(f'{spanish_mean:.2f}')+'%') 


plt.show()


