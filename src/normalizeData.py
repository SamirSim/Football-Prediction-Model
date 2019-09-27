import getNumericalData
from sklearn import preprocessing
import pandas as pd

train_set = pd.read_csv('dataTrain.csv')
test_set = pd.read_csv('dataTest.csv')

#drops the target column
y_train = train_set.final_score
x_train = train_set.drop(labels='final_score', axis=1)

y_test = test_set.final_score
x_test = test_set.drop(labels='final_score', axis=1)

#MinMax scaler, it does not distort data
mm_scaler = preprocessing.MinMaxScaler()
mm_scaled_x_train = mm_scaler.fit_transform(x_train)
mm_scaled_x_test = mm_scaler.fit_transform(x_test)

#Standard Scaler in case of the normal distribution
std_scaler = preprocessing.StandardScaler()
std_scaled_x_train = std_scaler.fit_transform(x_train)
std_scaled_x_test = std_scaler.fit_transform(x_test)

#Normalization of the data processed by Standard Scaler
normalized_std_train = preprocessing.normalize(std_scaled_x_train)
normalized_std_test = preprocessing.normalize(std_scaled_x_test)
