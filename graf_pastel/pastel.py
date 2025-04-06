import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

metadata=pd.read_csv('../data/Metadata.csv')


metadata.set_index=('Country Code')

#con matplotlib
#la variable counts agrupa  los datos por columnas
counts = metadata['IncomeGroup'].value_counts()

plt.pie(counts.values,labels=counts.index,autopct='%1.1f%%')
#print(metadata)

#con pandas
#ya no es necesario el counts
metadata['IncomeGroup'].value_counts().plot(kind='pie',ylabel='',
autopct='%1.1f%%')


plt.show()