import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
#datos
data = {"Año": ["2013", "2014", "2015"], "Valores": [10000, 20000, 30000]}
#conversion de datos para pandas
df = pd.DataFrame(data).set_index("Año")
#generar funcion con su tipo de grafico, tamaño y titulo
df.plot(kind="line", marker='o', figsize=(6,4), title="Crecimiento en México con Pandas")
#Mostrar
plt.show()