import numpy as np
import pandas as pd
import statsmodels.api as sm
from matplotlib import pyplot as plt
import seaborn as sns
sns.set()



# Load and prepare data
filepath = r'C:\Users\970jwillems\OneDrive - Sonova\Admin - Self-Dev\Data Science Bootcamp\Excercises\real_estate_price_size_year_view.csv'
data = pd.read_csv(filepath)

data['view'] = data['view'].map({'No sea view':0, 'Sea view':1})

print(data)


# Multiple Linear Regression
y = data['price']
x = data[['size', 'year', 'view']]
x = sm.add_constant(x)

results = sm.OLS(y,x).fit()

print(results.summary())

