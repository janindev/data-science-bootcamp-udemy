import numpy as np
import pandas as pd
#import scipy
import statsmodels.api as sm
from matplotlib import pyplot as plt
import seaborn as sns
sns.set()
#import sklearn


# Load data
filepath = r'C:\Users\970jwillems\OneDrive - Sonova\Admin - Self-Dev\Data Science Bootcamp\Course Material\1.01.+Simple+linear+regression.csv'
data = pd.read_csv(filepath)


# Explore data points
print(data.describe(), '\n'*2)

y = data['GPA']
x1 = data['SAT']

plt.scatter(x1, y, c="blue")
plt.xlabel('SAT', fontsize = 20)
plt.ylabel('GPA', fontsize = 20)
plt.show(block=False)


# Regression analysis
x0 = sm.add_constant(x1)                #Add intercept
results = sm.OLS(y,x0).fit()            #Fit using Ordinary Least Squares
print(results.summary(), '\n'*2)        #Output summary of OLS fit results
slope, intercept = np.polyfit(x1, y, 1) #Get slope and intercept
print(f"The slope = {slope}")
print(f"The intercept = {intercept}")


#Explore regression line
yht = slope * x1  + intercept
plt.plot(x1, yht, lw=4, c='orange', label='regression line')
plt.xlabel('SAT', fontsize = 20)
plt.ylabel('GPA', fontsize = 20)
plt.show(block=False)
