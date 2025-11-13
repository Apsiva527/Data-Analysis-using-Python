import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler,PolynomialFeatures
#from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import cross_val_score, train_test_split


from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
print("done")

df = pd.read_csv(r"C:\Users\amuda\Downloads\kc_house_data_NaN.csv")
print(df)
print(df.dtypes)
print(df.describe())

"""
Question 2
Drop the columns "id" and "Unnamed: 0" from axis 1 using the method drop(), then use the method describe() to obtain a statistical summary of the data. Make sure the inplace parameter is set to True. Take a screenshot of your code and output. You will need to submit the screenshot for the final project.
"""
df.drop(["id","Unnamed: 0"], axis=1, inplace= True)
print(df.describe())
#We can see we have missing values for the columns  bedrooms and  bathrooms 
print("number of NaN values for the column bedrooms :", df['bedrooms'].isnull().sum())
print("number of NaN values for the column bathrooms :", df['bathrooms'].isnull().sum())
#We can replace the missing values of the column 'bedrooms' with the mean of the column 'bedrooms'  using the method replace(). Don't forget to set the inplace parameter to True
mean=df['bedrooms'].mean()
df['bedrooms'].replace(np.nan,mean, inplace=True)
#We also replace the missing values of the column 'bathrooms' with the mean of the column 'bathrooms'  using the method replace(). Don't forget to set the  inplace  parameter top  True 
mean=df['bathrooms'].mean()
df['bathrooms'].replace(np.nan,mean, inplace=True)

print("number of NaN values for the column bedrooms :", df['bedrooms'].isnull().sum())
print("number of NaN values for the column bathrooms :", df['bathrooms'].isnull().sum())
print(df.head())

"""
Module 3: Exploratory Data Analysis
Question 3
Use the method value_counts to count the number of houses with unique floor values, use the method .to_frame() to convert it to a data frame. Take a screenshot of your code and output. You will need to submit the screenshot for the final project.

"""
floorcount=df['floors'].value_counts().to_frame()
print(floorcount)
"""
Question 4
Use the function boxplot in the seaborn library to determine whether houses with a waterfront view or without a waterfront view have more price outliers. Take a screenshot of your code and boxplot. You will need to submit the screenshot for the final project.

"""
sns.boxplot(x="waterfront", y="price", data=df)
plt.title("House Price Based On Waterfront View")
plt.xlabel('Waterfront (0=No,1=Yes)')
plt.ylabel('Price')
plt.show()

"""
Question 5
Use the function regplot in the seaborn library to determine if the feature sqft_above is negatively or positively correlated with price. Take a screenshot of your code and scatterplot. You will need to submit the screenshot for the final project.

"""
sns.regplot(x="sqft_above", y="price", data=df, line_kws={"color": "red"})
plt.ylim(0,)
plt.show()

"""
We can use the Pandas method corr() to find the feature other than price that is most correlated with price.
"""

df_numeric = df.select_dtypes(include=[np.number])
corr_price=df_numeric.corr()['price'].sort_values()
print(corr_price)
"""
Module 4: Model Development
We can Fit a linear regression model using the longitude feature 'long' and caculate the R^2.

"""
X = df[['long']]
Y = df['price']
lm = LinearRegression()
lm.fit(X,Y)
print("linear regression model using the longitude feature 'long'.")
print(lm.score(X, Y))

"""
Question 6.Fit a linear regression model to predict the 'price' using the feature 'sqft_living' then calculate the R^2
"""
X = df[['sqft_living']]
Y = df['price']
lm = LinearRegression()
lm.fit(X,Y)
print("linear regression model using the feature 'sqft_living'.")
print(lm.score(X, Y))
"""
Question 7
Fit a linear regression model to predict the 'price' using the list of features:
"""
features =["floors", "waterfront","lat" ,"bedrooms" ,"sqft_basement" ,"view" ,"bathrooms","sqft_living15","sqft_above","grade","sqft_living"] 
Z=df[features]
lm.fit(Z,Y)
print("linear regression model using the all feature .")
print(lm.score(Z,Y))

"""
This will help with Question 8
Create a list of tuples, the first element in the tuple contains the name of the estimator:

'scale'

'polynomial'

'model'

The second element in the tuple contains the model constructor

StandardScaler()

PolynomialFeatures(include_bias=False)

LinearRegression()
"""
Input=[('scale',StandardScaler()),('polynomial', PolynomialFeatures(include_bias=False)),('model',LinearRegression())]
"""
Question 8
Use the list to create a pipeline object to predict the 'price', fit the object using the features in the list features, and calculate the R^2. Take a screenshot of your code and the value of the R^2. You will need to submit it for the final project.
"""
pipe=Pipeline(Input)
Z =Z.astype(float)
pipe.fit(Z,Y)
ypipe=pipe.predict(Z)
print("create a pipeline object to predict the 'price'.")
print(r2_score(Y,ypipe))

#We will split the data into training and testing sets:
features =["floors", "waterfront","lat" ,"bedrooms" ,"sqft_basement" ,"view" ,"bathrooms","sqft_living15","sqft_above","grade","sqft_living"]    
X = df[features]
Y = df['price']

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.15, random_state=1)


print("number of test samples:", x_test.shape[0])
print("number of training samples:",x_train.shape[0])

"""
Question 9
Create and fit a Ridge regression object using the training data, set the regularization parameter to 0.1, and calculate the R^2 using the test data. Take a screenshot of your code and the value of the R^2. You will need to submit it for the final project.

"""
RidgeModel=Ridge(alpha=0.1)
RidgeModel.fit(x_train, y_train)
yhat = RidgeModel.predict(x_test)
print("set the regularization parameter to 0.1, and calculate the R^2 using the test data.")
print(r2_score(y_test,yhat))

"""
Question 10
Perform a second order polynomial transform on both the training data and testing data. 
Create and fit a Ridge regression object using the training data, set the regularisation parameter to 0.1, and calculate the R^2 utilising the test data provided. 
Take a screenshot of your code and the R^2. You will need to submit it for the final project.
"""
poly = PolynomialFeatures(degree=2)
X_train_poly = poly.fit_transform(x_train)
X_test_poly = poly.transform(x_test)

#create Ridge model
RidgeModel = Ridge(alpha=0.1)

#Fit the model on training data
RidgeModel.fit(X_train_poly, y_train)
#Predict using test data
Y_pred = RidgeModel.predict(X_test_poly)
#Calculate R^2 score
r2 = r2_score(y_test, Y_pred)

print("R^2 Score on Test Data:", r2)
