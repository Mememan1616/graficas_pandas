import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

#Cargar el archivo CSV
population = pd.read_csv('../data/Population.csv')
metadata=pd.read_csv('../data/Metadata.csv')
# Verificar columnas disponibles
#print("Columnas disponibles:", population.columns)

# Eliminar espacios en nombres de columnas
population.columns = population.columns.str.strip()

#Se agrupan los dos archivos a traves de Country code y de esa manera unir ambos datos
merged_df = pd.merge(left=metadata,right=population,left_on='Country Code',right_on='Country Code')


'''
El objetivo será sacar el total de población por región para el año 2019, entonces se utiliza groupby() 
de Pandas con la función sum() para combinar todos los registros por grupo:

region_population = merged_df.groupby(['Region']).sum()

Con lo anterior se totaliza por región todos los campos numéricos, pero como únicamente es de 
interés el año 2019, podemos quedarnos únicamente con esa columna:

region_population = merged_df.groupby(['Region']).sum()[['2019']]
'''
#region_population = merged_df.groupby(['Region']).sum()

region_population = merged_df.groupby(['Region']).sum()[['2019']]
print(region_population)

region_population.plot(rot=90,figsize=(10,8),legend=False)

plt.title('Population by region 2019',fontsize=20,
horizontalalignment='left')
plt.xlabel('Region',fontsize=20)
plt.show()

