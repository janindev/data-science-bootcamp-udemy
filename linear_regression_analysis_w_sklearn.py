import numpy as np
import pandas as pd 
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
import seaborn as sns
sns.set()



# Load data
filepath = r'C:\Users\970jwillems\OneDrive - Sonova\Admin - Self-Dev\Data Science Bootcamp\Course Material\1.01.+Simple+linear+regression.csv'
data = pd.read_csv(filepath)


# Declare variables


x = data['SAT']
y = data['GPA']
x = x.values.reshape(-1 ,1)

print(x)
print(y)


# Create the Regression Analysis
reg = LinearRegression()
reg.fit(x, y)

print(reg.score(x, y))
print(reg.coef_)
print(reg.intercept_)


#Explore regression line
plt.scatter(x,y)
yht = reg.coef_ * x + reg.intercept_
print(yht)
plt.plot(x, yht, lw=4, c='orange', label='regression line')
plt.xlabel('SAT', fontsize = 20)
plt.ylabel('GPA', fontsize = 20)
plt.show(block=False)


# Simple test
new_data = pd.DataFrame(data=[1740, 1790], columns = ['SAT'])
reg.predict(new_data)
new_data['Predicted GPA'] = reg.predict(new_data)
print(new_data)






