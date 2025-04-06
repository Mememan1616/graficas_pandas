import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Crear DataFrame
data = {"Año": ["2013", "2014", "2015"], "Valores": [10000, 20000, 30000]}
df = pd.DataFrame(data)

# Crear la gráfica con Seaborn
plt.figure(figsize=(6,4))

sns.lineplot(x="Año", y="Valores", data=df, marker='o')

plt.xlabel("Año")
plt.ylabel("Valor")
plt.title("Crecimiento en México con Seaborn")
plt.grid(True)
plt.show()
