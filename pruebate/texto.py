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

#print(data_2020)


sns.barplot(x=data_2020.index, data=data_2020, y='2020', palette='pastel')
plt.title('Women Parliaments')

for i in range(data_2020.shape[0]): 
    plt.text(i,data_2020.iloc[i,0],str(round(data_2020.iloc[i,0],2))+'%')

#rotar el texto de horizontal a vertical
plt.xticks(rotation=90)

plt.show()