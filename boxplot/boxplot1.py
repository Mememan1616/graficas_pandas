import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


lifexp_male=pd.read_csv('../data/LifeExpectancyMale.csv')

'''se empleará nuevamente el dataframe lifexp_male, el cual concentra la información del archivo 
LifeExpectancyMale.csv, y se graficará un boxplot con la
 expectativa de vida del año 2019, utilizando varias de las formas equivalentes estudiadas:'''

#Toma la columna del año 2019, los acomoda de menor a mayor y se utiliza boxplot

#Matplotlib
plt.boxplot(lifexp_male['2019'].dropna(),label=['2019'])

#pandas
lifexp_male['2019'].plot.box()

#seaborn
sns.boxplot(x=lifexp_male['2019'])
sns.boxplot(x='2019',data=lifexp_male)
sns.catplot(kind='box',x='2019',data=lifexp_male)

plt.show()