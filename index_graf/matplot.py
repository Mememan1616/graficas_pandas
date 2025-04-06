import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

#Cargar el archivo CSV
population = pd.read_csv('../data/Population.csv')

# Verificar columnas disponibles
#print("Columnas disponibles:", population.columns)

# Eliminar espacios en nombres de columnas
population.columns = population.columns.str.strip()

#Crear el grafico de varias  filas de datos

north_america = population[(population['Country Name']=='Mexico')|
 (population['Country Name']=='United States')|
 (population['Country Name']=='Canada')]   

#Se inicia por eliminar el código del país, pues con el nombre será suficiente para identificarlo:
north_america = north_america.drop('Country Code',axis=1)

 #2.   El índice no es tan representativo, pues ni siquiera indica la posición de cada registro en el 
#dataframe, por lo que se procede a hacer que el nombre sea el nuevo índice:

north_america.set_index('Country Name',inplace=True)

#A continuación, se intercambian entonces las posiciones de las filas y las columnas, usando la 
#propiedad T que obtiene la traspuesta:

north_america = north_america.T

north_america.index.name = 'Year'
north_america.columns.name = ''

print(north_america)


#Ahora crearemos un indice para cada pais en los diferentes tipos de graficos
'''
#Con Matplotlib
plt.plot(north_america.index,north_america.values, marker='o', linestyle='-')

plt.xticks(np.arange(0, len(north_america)+1, 10))
plt.legend(north_america.columns)


#Con pandas
north_america.plot(xlabel='Year',ylabel='Poblacion', rot=45,fontsize=8, kind='line')

#con seaborn
#Recuerda que Seaborn solo agrega diseños, puede construir su grafico siempre y cuando no haya otro
sns.lineplot(data=north_america)
plt.xticks(np.arange(0, len(north_america)+1, 10))

'''

#Ahora vamos a descartar las demas columnas o solo se tomara una 
#aqui lo que se hace es basicamete modificar la cantidad de columnas y le decimos que solo tome la que tiene ese nombre

#Matplotlib
plt.plot(north_america.index, north_america['Mexico'])
plt.xticks(np.arange(0, len(north_america)+1, 10))
plt.legend(north_america.columns)

#Pandas
north_america.plot( y='Mexico', title="Poblacion de Mexico")

#seaborn
'''
sns.lineplot(x=north_america.index,
y=north_america['Mexico'])
plt.xticks(np.arange(0, len(north_america)+1, 10))
plt.legend(north_america.columns)
'''
#plt.title("Poblacion")
plt.legend()
plt.show()