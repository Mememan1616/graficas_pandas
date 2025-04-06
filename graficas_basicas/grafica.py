import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


#Arreglo de datos 
data={"Año":["2013","2014","2015"],"Valores":[1000,2000,3000]}
#definir los indices para el arreglo
df = pd.DataFrame(data).set_index("Año")

index=["2013","2014","2015"]
valores=[1000,2000,3000]

#----------------------------------------------------------------------------------
#Con matplotlib

#tamaño de la figura figsize(ancho,alto)
plt.figure(figsize=(8,4))
#Asignar los datos
plt.plot(index, valores, marker='o', linestyle='-', color='c', label="Crecimiento")
#label del eje x
plt.xlabel("Año")
#label del eje y
plt.ylabel("Valor")
#titulo del grafico
plt.title("Crecimiento en México con Matplotlib")
plt.legend()
plt.grid(True)
#mostrarlo
plt.show()

