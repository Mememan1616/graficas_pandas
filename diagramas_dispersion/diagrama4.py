import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


#leer los csv
metadata=pd.read_csv('../data/Metadata.csv')
gni=pd.read_csv('../data/GNI.csv')
lifexp_male=pd.read_csv('../data/LifeExpectancyMale.csv')

#Unir los dataframes de gni y lifexp
merged_df = lifexp_male.merge(gni,on='Country Code',suffixes=('_lifexp','_gni'))

#unirlos con el dataframe de meta daata
merged_df2 = merged_df.merge(metadata,on='Country Code')



'''La interfaz relplot permite separar los grupos en gráficos independientes, basta con indicarlo en el parámetro col:'''

#en este caso lo que haremos sera crear grupos independientes por  conjunto de datos usando como columna referente IncomeGroup
splot = sns.relplot(kind='scatter',x='2019_gni',y='2019_lifexp',col='IncomeGroup',data=merged_df2)

splot.set(xscale='log')




plt.show()