import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np


birth=pd.read_csv('../data/Birth.csv')
#birth.columns=birth.columns.str()

death=pd.read_csv('../data/Death.csv')



birth_mexico=birth.loc[birth['Country Name']=='Mexico']
death_mexico=death.loc[death['Country Name']=='Mexico']

#borramos la columna country code
birth_mexico = birth_mexico.drop('Country Code',axis=1)
death_mexico= death_mexico.drop('Country Code', axis=1)

birth_mexico.set_index('Country Name', inplace=True)
death_mexico.set_index('Country Name', inplace=True)


birth_mexico=birth_mexico.T
death_mexico=death_mexico.T

birth_mexico.index.name="Year"
death_mexico.index.name="Year"

birth_mexico.columns.name=''
birth_mexico.columns=['Births']
death_mexico.columns.name=''
death_mexico.columns=['Deaths']

#print(death_mexico)

#se unen
mexico=birth_mexico.join(death_mexico)



mexico.plot(title="Natalidad y Mortalidad en Mexico", xlabel="Años", ylabel="Millones de personas")

#Construir grafico de barras
sns.set_palette('Set2')
sns.set_style('darkgrid')
#Recortar los valores superfialmente sin alterar el contenido de la variable
death.sort_values('2018',inplace=True)

#Acomoda la columna 2018 de menor a mayor
death.dropna(axis=0,subset=['2018'],inplace=True)

#Se encarga de concatenar los valores de Mexico y Estados Unidos y los ultimos 3 valores de la tabla
sample = pd.concat([death[death['Country Name']=='Mexico'],death[death['Country Name']=='United States'],death[-3:]])

#Se coloca el tipo del grafico, y los datos del eje x y y
sample.plot(kind='barh',x='Country Name',y='2018',title='Death rate 2018')
#print(death)


#grafica de pastel

#Esta línea configura la paleta de colores que usará Seaborn para las gráficas. "Set1" es una paleta de colores predefinida que proporciona colores contrastantes y llamativos.
sns.set_palette("Set1")

'''#aquí se eliminan las filas del DataFrame birth que no tienen datos (NaN) en la columna '2018'.
#axis=0 indica que se eliminarán filas.
#subset=['2018'] significa que solo se revisa la columna '2018' para valores nulos.
#inplace=True hace que los cambios se apliquen directamente en el DataFrame birth.
birth.dropna(axis=0,subset=['2018'],inplace=True)'''

#Esta línea cuenta cuántos países tienen un número de nacimientos en 2018 por debajo del promedio de todos los países.

'''birth['2018'].mean() calcula la media de nacimientos en 2018.
#birth['2018'] < ... crea una serie booleana.
#birth[...] filtra el DataFrame con esa condición.
#len(...) cuenta cuántas filas cumplen la condición.'''

below_avg = len(birth[birth['2018'] < birth['2018'].mean()])

'''Se crea una lista con dos valores:

El número de países por debajo del promedio.

El número de países por encima o igual al promedio (calculado como el total menos los que están por debajo).'''

count = [below_avg, len(birth['2018']) - below_avg]

'''Crea el grafico de tipo pastel y agrega l'''
plt.pie(count,labels=['births < avg','births > average'],autopct='%1.1f%%')
plt.title('Number of countries')
plt.show()
