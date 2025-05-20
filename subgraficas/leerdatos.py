import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


#leer los csv
metadata=pd.read_csv('../data/Metadata.csv')
lifexp_male=pd.read_csv('../data/LifeExpectancyMale.csv')
gni=pd.read_csv('../data/GNI.csv')
#Unir los dataframes de gni y lifexp
merged_df = lifexp_male.merge(metadata,on='Country Code',suffixes=('_lifexp','_meta'))

#crear un histograma de la expectativa de vida en el 2019, y se separa por el tipo de ingreso
#merged_df['2019'].hist(by=merged_df['IncomeGroup'])

#usar histogramas, diagramas de dispersion y boxplot son seaborn para dichos datos

#histograma
sns.displot(kind='hist',x='2019',col='IncomeGroup',data=merged_df)

#boxplot
sns.catplot(kind='box',x='Region',y='2019',col='IncomeGroup',data=merged_df)

#diagramas de dispersion
merged_df2=merged_df.merge(gni, on="Country Code", suffixes=('_lifexp','_gni'))
print(merged_df2.columns)
splot=sns.relplot(kind='scatter',x='2019_gni',y='2019_lifexp',col='IncomeGroup',data=merged_df2)
splot.set(xscale='log')

#ahora hablaremos de los subplots
#los subplots sirven para agregar graficas en una misma matriz





plt.show()

