import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

happiness=pd.read_csv('../data/Happines_report.csv')
meta=pd.read_csv('../data/Metadata.csv')


mexico=happiness[happiness['Country or region']=='Mexico']
mexico.set_index('Country or region',inplace=True)


sns.set_palette('pastel')
sns.set_style('ticks')


'''happines_hist=sns.histplot(happiness['Score'], bins=10, kde=False)
plt.title('World Happines Report')
plt.ylabel('Frecuency')

font = {
        'family': 'serif', 
         'size': 15, 
         'weight': 'bold', 
         'style': 'italic', 
         'color': 'white', 
         'horizontalalignment': 'center'
        } 

box =   {
        'boxstyle': 'circle',
        'facecolor': 'purple',
        'alpha': 0.3
        }



plt.text(mexico.loc['Mexico','Score'],0,'MEX', fontdict=font, bbox=box)'''


'''value=mexico.loc['Mexico','Healthy life expectancy']

happiness['Healthy life expectancy'].plot(kind='box')
plt.title('Healthy life expectancy')

props_arrow = {'facecolor':'red', 
    'width':0.5, 
    'headwidth':8, 
    'headlength':8
    } 

props_arrow = { 
    'color':'red',
    'shrink':0.05,
    'width':0.5, 
    'headwidth':8, 
    'headlength':8
    } 

box2 =   {
        'boxstyle': 'circle',
        'facecolor': 'red',
        'alpha': 0.3
        }

plt.annotate('MEX', xy=(1,value), xytext=(1.2,value), arrowprops=props_arrow,
               bbox=box2, color='white')'''


'''mexico_new=mexico.drop(columns=['Overall rank','Score'])
mexico_new=mexico_new.T
mexico_new.columns=['Factors']


plt.pie(x=mexico_new['Factors'],labels=mexico_new.index,
        autopct='%1.1f%%')
plt.legend=True

table=plt.table(mexico_new, bbox=[-0.6, 0.2, 0.5, 0.6])'''

'''countries=happiness.loc[(happiness['Score']==happiness['Score'].max())|
                        (happiness['Country or region']=='Mexico')|
                        (happiness['Score']==happiness['Score'].min())|
                        (happiness['Country or region']=='Germany')|
                        (happiness['Country or region']=='United States')]

countries.set_index('Country or region', inplace=True)

countries=countries.drop(columns=['Score','Overall rank'])
countries=countries.T

print(countries)

countries.plot(kind='bar', title='World Happiness Report')'''


'''fig = plt.figure(figsize=(20,10))


ax1 = fig.add_subplot(231)
happiness.plot(kind='scatter',x='Score' ,y='GDP per capita', ax=ax1)

ax2 = fig.add_subplot(232)
happiness.plot(kind='scatter',x='Score' ,y='Social support', ax=ax2)

ax3 = fig.add_subplot(233)
happiness.plot(kind='scatter',x='Score' ,y='Healthy life expectancy', ax=ax3)

ax4 = fig.add_subplot(234)
happiness.plot(kind='scatter',x='Score' ,y='Freedom to make life choices', ax=ax4)

ax5 = fig.add_subplot(235)
happiness.plot(kind='scatter',x='Score' ,y='Generosity', ax=ax5)

ax6 = fig.add_subplot(236)
happiness.plot(kind='scatter',x='Score' ,y='Perceptions of corruption', ax=ax6)

fig.suptitle('Contribuition of happiness Score', fontsize=16, fontweight='bold')

plt.show()'''

'''corr = happiness.drop(columns='Country or region').corr()

# Crear heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm', linewidths=0.5, fmt='.2f')

# Título
plt.title('World Happiness Report')
plt.show()'''

happines_Region=meta.merge(happiness,left_on='TableName', right_on='Country or region', how='outer' )



group =happines_Region[['Score','Region']].groupby('Region').median()
print(group['Score'])

sns.barplot(x=group.index, y='Score', data=group, palette='pastel')
plt.xticks(rotation=90)
plt.title('World Happinest Report')
plt.show()