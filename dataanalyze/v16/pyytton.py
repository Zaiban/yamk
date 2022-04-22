# Viikko 16 by Esa Kujansuu

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv('salary.csv')

print('df', df)

#sns.heatmap(df.corr(), annot=True)
#plt.show()

# Divide data to two parts, train and test
x_train, x_test, y_train, y_test = train_test_split(df['YearsExperience'], df['Salary'], test_size=0.2)
 
 # Data formats must be reshaped, because model training expects more than one column by default
x_train = x_train.values.reshape(-1, 1)
x_test = x_test.values.reshape(-1, 1)

# Plot data points
#plt.scatter(x_train, y_train)
#plt.show()

# Create empty linear regression model
lr = LinearRegression()

# Prepare (trian linear regression model with data)
lr_model = lr.fit(x_train, y_train)

# Predict values for test values (x_test)
y_predicted_values = lr_model.predict(x_test)

# Compare predicted values (predicted_values) with actual values (y_test)
comparison = pd.DataFrame()
x_test = x_test.flatten()
comparison['YearsExperience'] = x_test
comparison['Predicted Salary'] = y_predicted_values
comparison['Actual Salary'] = y_test.values

# Plot the comparison
comparison.plot.bar(x='YearsExperience')
plt.show()