import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

#Cargar el archivo CSV
fertility = pd.read_csv('data/Fertility.csv')

# Verificar columnas disponibles
#print("Columnas disponibles:", population.columns)

# Eliminar espacios en nombres de columnas
fertility.columns = fertility.columns.str.strip()
five = fertility.loc[fertility['Country Name'].isin(['Mexico','United States','Somalia','China','India']) ,['Country Name','2018']]
five.set_index('Country Name',inplace=True)
five.plot(legend=False,title='Fertility rate 2018',rot=90,linestyle=':')

plt.xlabel("")
plt.ylabel("")
plt.title("Fertilidad en el 2018")
plt.legend()
plt.grid(True)

plt.show()