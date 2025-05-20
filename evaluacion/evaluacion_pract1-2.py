import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
#lee el documento de CSV
alcohol=pd.read_csv('../data/AlcoholConsumption.csv')


#Crea un df con solo los datos de mexico
mexico=alcohol[alcohol['country']=='Mexico']
mexico.set_index('country',inplace=True)


'''---seccion 3:  Evaluar la dispersión del consumo de alcohol en el mundo
para ello se hara uso de los boxplot, en el que se pueden analizar las medidas de tendencia central y 
dispersion------'''

#si usamos dropna se borrarian los datos nulos y modificariamos el DF original
#alcohol.dropna(axis=0,subset=['alcconsumption'],inplace=True)

#por ello se borran solo en la grafica y no en el DF
plt.boxplot(alcohol['alcconsumption'].dropna(),labels=['Litres pure alcohol']) 
plt.title('Alcohol consumption per adult (age 15+)')
plt.show()