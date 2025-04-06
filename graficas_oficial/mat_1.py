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

# Graficar
plt.figure(figsize=(8,5))
plt.plot(mexico.index, mexico["Población"], marker='o', linestyle=':', color='m', label="Crecimiento")

# Etiquetas y título
plt.xlabel("Año")
plt.ylabel("Población")
plt.title("Crecimiento poblacional en México (2014-2019)")
plt.legend()
plt.grid(True)

# Mostrar el gráfico
plt.show()
