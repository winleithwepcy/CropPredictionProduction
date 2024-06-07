import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 
import pickle

data = pd.read_csv('encoded_crop_data.csv') 
print(data)

#Select all rows and column 1 from dataset to x and all rows and column 2 as y

x = data.iloc[:, 0:8].values  
print(x)

y = data.iloc[:, 8].values   
print(y)

# Fitting Random Forest Regression to the dataset 
# import the regressor 
from sklearn.ensemble import RandomForestRegressor 
  
 # create regressor object 
regressor = RandomForestRegressor(n_estimators = 100, random_state = 0) 
  
# fit the regressor with x and y data 
regressor.fit(x, y)  
pickle.dump(regressor,open('crop_model.pkl','wb'))