import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

#Cargar el archivo CSV
population = pd.read_csv('data/Fertility.csv')

# Verificar columnas disponibles
#print("Columnas disponibles:", population.columns)

# Eliminar espacios en nombres de columnas
population.columns = population.columns.str.strip()

mexico=population.loc[population["Country Name"]=='Mexico','1960':'2018']
mexico=mexico.T
mexico.columns=["Fertilidad"]
mexico.index=mexico.index.astype(int)

canada=population.loc[population["Country Name"]=='Canada','1960':'2018']
canada=canada.T
canada.columns=["Fertilidad"]
canada.index=canada.index.astype(int)

plt.figure(figsize=(8,5))
plt.plot(mexico.index, mexico["Fertilidad"], marker='o', linestyle='-', color='r',label="Mexico")

plt.plot(canada.index, canada["Fertilidad"], marker='o', linestyle='-', color='m', label="Canada")
plt.legend()
# Etiquetas y título
plt.xlabel("Año")
plt.ylabel("Población")
plt.title("Crecimiento poblacional en México (2014-2019)")
plt.legend()
plt.grid(True)

plt.show()