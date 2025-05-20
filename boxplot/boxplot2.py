import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns




lifexp_male=pd.read_csv('../data/LifeExpectancyMale.csv')
metadata=pd.read_csv('../data/Metadata.csv')
#Crearemos boxplot combinados al menos dos en una sola grafica

#Matplotlib
plt.boxplot(x=[lifexp_male['1960'].dropna(),lifexp_male['2019'].dropna()],tick_labels=['1960','2019'])

#pandas
lifexp_male[['1960','2019']].plot.box()

#seaborn
sns.boxplot(x='variable',y='value',data=pd.melt(lifexp_male.loc[:,['1960','2019']]))

plt.show()