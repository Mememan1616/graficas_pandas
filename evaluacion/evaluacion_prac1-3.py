import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
#lee el documento de CSV
alcohol=pd.read_csv('../data/AlcoholConsumption.csv')


#Crea un df con solo los datos de mexico
mexico=alcohol[alcohol['country']=='Mexico']
mexico.set_index('country',inplace=True)


#realiza los graficos de diagramas de dispersion de cada relacion entre
#el consumo de alcohol con los demas datos
alcohol.plot.scatter(x='alcconsumption',y='incomeperperson') 
plt.yscale('log') 
alcohol.plot.scatter(x='alcconsumption',y='suicideper100th') 
alcohol.plot.scatter(x='alcconsumption',y='employrate') 
alcohol.plot.scatter(x='alcconsumption',y='urbanrate')



plt.show()