import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


Exp_vid=pd.read_csv('../data/LifeExpectancyMale.csv')
#birth.columns=birth.columns.str()

#Toma solo la columna del año 2019
life_expect_2019=Exp_vid["2019"]

#print(life_expect_2019)
plt.hist(life_expect_2019)

plt.show()