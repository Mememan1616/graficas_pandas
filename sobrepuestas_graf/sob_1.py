import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

'''
Cuando dos o más series de datos poseen la misma escala, es posible comparar sus
 magnitudes compartiendo ambos ejes y fijando los valores de uno de ellos para establecer la correlación.
   Eso ya se ha realizado en lecciones previas. Por ejemplo, en las siguientes imágenes se ha comparado la expectativa
     de vida de los hombres con dos series: 1960 y 2019, que son columnas diferentes del dataframe lifexp_male. 
     
En ambos casos se han fijado los años; en los histogramas a través de los bins en el eje x y en los boxplots en el eje y.

'''

lifexp_male=pd.read_csv('../data/LifeExpectancyMale.csv')

plt.hist('1960',data=lifexp_male,label='1960') 
plt.hist('2019',data=lifexp_male,label='2019') 
plt.legend()

lifexp_male[['1960','2019']].plot.box()



plt.show()