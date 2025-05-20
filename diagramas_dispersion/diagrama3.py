
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

'''
Como en los histogramas y boxplots, en los scatter plots también puedes separar en grupos
 la relación entre dos variables. Para ello, se ocupará nuevamente el dataframe metada, 
 para combinarlo con merged_df y
así poder obtener un scatter plot en el que se indique la región:

'''
#leer los csv
metadata=pd.read_csv('../data/Metadata.csv')
gni=pd.read_csv('../data/GNI.csv')
lifexp_male=pd.read_csv('../data/LifeExpectancyMale.csv')

#Unir los dataframes de gni y lifexp
merged_df = lifexp_male.merge(gni,on='Country Code',suffixes=('_lifexp','_gni'))

#unirlos con el dataframe de meta daata
merged_df2 = merged_df.merge(metadata,on='Country Code')

'''
Sin embargo, la única plataforma que permite la separación de manera directa con una variable de agrupación es Seaborn, 
a través de su parámetro hue. No hay función para el scatter en Pandas que sea equivalente a hist() y boxplot(), 
en las que se usaba el parámetro by con este fin. Tanto en Matplotlib 
como en Pandas se deben crear los grupos explícitamente (con groupby) y después iterarlos.
'''

splot = sns.scatterplot(x='2019_gni',y='2019_lifexp',hue='IncomeGroup',data=merged_df2)
splot.set(xscale='log')
corr = gni['2019'].corr(lifexp_male['2019']) 
print(corr)
plt.show()