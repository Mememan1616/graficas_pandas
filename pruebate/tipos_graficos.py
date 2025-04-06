import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np


birth=pd.read_csv('../data/Birth.csv')
#birth.columns=birth.columns.str()

death=pd.read_csv('../data/Death.csv')



birth_mexico=birth.loc[birth['Country Name']=='Mexico']
death_mexico=death.loc[death['Country Name']=='Mexico']

#borramos la columna country code
birth_mexico = birth_mexico.drop('Country Code',axis=1)
death_mexico= death_mexico.drop('Country Code', axis=1)

birth_mexico.set_index('Country Name', inplace=True)
death_mexico.set_index('Country Name', inplace=True)
birth_mexico=birth_mexico.T
death_mexico=death_mexico.T




#Se agrupan los dos archivos a traves de Country code y de esa manera unir ambos datos
#merge = pd.merge(left=birth,right=death,left_on='Years',right_on='Years')
print(birth_mexico)

#plt.plot(birth_mexico.index, birth_mexico)
#plt.plot(death_mexico.index, death_mexico)

#df1=birth_mexico
#df2=death_mexico
#df1.plot()
#df2.plot()
#plt.show()
#print(birth_mexico)