import matplotlib.pyplot as plt
import pandas as pd

# Cargar el archivo CSV
population = pd.read_csv('../data/Population.csv')

# Verificar columnas disponibles
#print("Columnas disponibles:", population.columns)

# Eliminar espacios en nombres de columnas
population.columns = population.columns.str.strip()

# Filtrar los datos de México entre 2014 y 2019
mexico = population.loc[population['Country Name'] == 'Mexico', '2014':'2019']

# Transponer los datos para que los años sean el índice
mexico = mexico.T  # Transpone el DataFrame
mexico.columns = ["Población"]  # Renombrar la única columna
mexico.index = mexico.index.astype(int)  # Convertir los años a enteros

# Verificar los datos antes de graficar
#print(mexico)

mexico.plot(title='Population of Mexico',
            legend=False,
            xlabel='Year',
            ylabel='Population',
            rot=45,
            fontsize=10)
plt.show()