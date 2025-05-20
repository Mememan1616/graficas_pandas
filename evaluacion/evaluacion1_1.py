import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

data=pd.read_csv('../data/Metadata.csv')
data2=pd.read_csv('../data/LifeExpectancyMale.csv')

data.set_index('Country Code' ,inplace=True)

data2.set_index('Country Code' ,inplace=True)

print(data.columns)

#sns.histplot(data2[['2009','2019']], alpha=0.5, bins=10)

#fig, axs=plt.subplots(3
'''
df=[['Relationship_status','Time_of_service'],
                     ['Married', 10],
                     ['not_Married', 10],
                     ['Married', 10],
                     ['not_Married', 10],
                     ['Married', 10],
                     ['not_Married', 10]]


data3=[
       ['MEX',3.58,4.1, 6, 1.47,-7],
       ['BRA',3.58,4.1, 6, 1.47,-7],
       ['ARG',3.58,4.1, 6, 1.47,-7]]


exports=pd.DataFrame(data3)
exports.columns=['Country Code', '2016','2017','2018','2019','2020']
exports.set_index('Country Code', inplace=True)
print(exports.columns)

exports.plot(kind='bar', title='Exports')'''



'''data4=[['MEX',7.41, 5.88,7.92,5,3,6,4,1,6,9]]

mexico=pd.DataFrame(data4)


mexico.columns=['Country Code','1966','1967','1968','2010','2011','2012','2013','2014','2015','2020']

mexico.set_index('Country Code', inplace=True)
print(mexico)'''

#plt.plot(mexico.loc['2010':'2020':10],title='Annual growth rate for manufaturing',rot=90) 
#plt.plot(mexico.T.loc[10,'2010':'2020']) 
#plt.xticks(rotation=90) 
#plt.title('Annual growth rate for manufaturing')
#plt.plot(mexico.loc[:,'2010':'2020'],rot=90,title='Annual growth rate for manufaturing') 

'''plt.plot(mexico.T.loc['2010':'2020',:]) 

plt.xticks(rotation=90) 

plt.title('Annual growth rate for manufaturing') '''


#fig,axs = plt.subplots(2,2)
#ax = fig.add_subplot(113) 
#ax = fig.add_subplot(224) 


#data2[['2017','2018','2019']].plot.box(subplots=True)
lifexp_male=pd.read_csv('../data/LifeExpectancyMale.csv')
metadata=pd.read_csv('../data/Metadata.csv')

#merged_df = lifexp_male.merge(metadata,on='Country Code')



#splot = sns.catplot(kind='box',x='Region',y='2019',col='IncomeGroup',data=merged_df);
#splot.set_xticklabels(rotation=90)


sns.set_style('darkgrid') 

# Cargar el archivo CSV
population = pd.read_csv('../data/Population.csv')

# Verificar columnas disponibles
#print("Columnas disponibles:", population.columns)

# Eliminar espacios en nombres de columnas
population.columns = population.columns.str.strip()

# Filtrar los datos de México entre 2014 y 2019
mexico = population.loc[population['Country Name'] == 'Mexico', '2014':'2019']

# Transponer los datos para que los años sean el índice
mexico = mexico.T  # Transpone el DataFrame
mexico.columns = ["Población"]  # Renombrar la única columna




sns.lineplot(x=mexico.index,y=mexico["Población"] ,color='green',marker='s',linestyle=':') 
plt.title('Annual growth rate for manufaturing Mexico') 
plt.ylabel('') 

props_bbox = {'boxstyle': 'circle', 

                        'facecolor': 'red', 

                        'alpha': 0.3} 

plt.text(2025 ,0.5,'Meta')
plt.show()
