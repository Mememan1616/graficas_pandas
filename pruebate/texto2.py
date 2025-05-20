import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np


WomanParliaments=pd.read_csv('../data/WomanParliaments.csv')


#seccion de textos

metadata=pd.read_csv('../data/Metadata.csv')

merge=metadata.merge(WomanParliaments, on='Country Code')


data_2020=merge[['Country Code', 'Region', '2020']]

data_2020=data_2020.groupby('Region').mean('2020')

parliament_2020=WomanParliaments[['Country Code', '2020']]
parliament_2020.set_index('Country Code',inplace=True)

sns.boxplot(data=parliament_2020)
#print(parliament_2020)
value=parliament_2020.loc[parliament_2020.index=='MEX']
print(value)

props_font = {
        'family': 'serif', 
         'size': 18, 
         'weight': 'bold', 
         'color': 'black', 
         'horizontalalignment': 'center'} 

props_bbox = {
'boxstyle': 'square',
 'facecolor': 'green',
 'alpha': 0.3}


props_arrow = {'facecolor':'white', 
'width':0.5, 
'headwidth':8,
'color':'red', 
'headlength':8} 
plt.annotate('MEX', xy=('2020',value.values),xytext=(0.2, value.values+10),arrowprops=props_arrow, bbox=props_bbox )
#plt.text('2020',value.values,'MEX',fontdict=props_font, bbox=props_bbox)
plt.show()