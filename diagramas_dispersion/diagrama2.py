import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

gni=pd.read_csv('../data/GNI.csv')
lifexp_male=pd.read_csv('../data/LifeExpectancyMale.csv')

merged_df = lifexp_male.merge(gni,on='Country Code',suffixes=('_lifexp','_gni'))

print(merged_df)


#matplotlib
#plt.scatter(x='2019_gni',y='2019_lifexp',data=merged_df) 
plt.xscale('log')

'''
plt.scatter(x=merged_df['2019_gni'],y=merged_df['2019_lifexp'])
plt.xscale('log')
'''
#pandas
merged_df.plot(kind='scatter',x='2019_gni',y='2019_lifexp',c='red',logx=True,logy=True)
#o
merged_df.plot.scatter(x='2019_gni',y='2019_lifexp',c='red',logx=True,logy=True)


#seaborn
splot = sns.relplot(kind='scatter',x='2019_gni',y='2019_lifexp',data=merged_df)
splot.set(xscale='log')
#o
splot = sns.scatterplot(x='2019_gni',y='2019_lifexp',data=merged_df)
splot.set(xscale='log')
#o
splot = sns.scatterplot(x=merged_df['2019_gni'],y=merged_df['2019_lifexp'])
splot.set(xscale='log')
plt.show()