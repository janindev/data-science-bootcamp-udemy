import numpy as np
import pandas as pd
import statsmodels.api as sm
from matplotlib import pyplot as plt
import seaborn as sns
sns.set()



# Load data
filepath = r'C:\Users\970jwillems\OneDrive - Sonova\Admin - Self-Dev\Data Science Bootcamp\Course Material\1.02.+Multiple+linear+regression.csv'
data = pd.read_csv(filepath)

print(data)


# Analyse data

y = data['GPA']
x1 = data[['SAT', 'Rand 1,2,3']]

x = sm.add_constant(x1)
results = sm.OLS(y,x).fit()

print(results.summary())

