#cancer(이진)데이터로 오늘 배운 SVC, linearSVC, KNeighborsClassifier, KNeighborsRegressor
#중 하나를 사용하여 만든다.


from keras.models import load_model

from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor
# from sklearn.datasets import load_wine
from keras.utils import np_utils
from sklearn.preprocessing import StandardScaler
from keras.models import Sequential
from keras.layers import Dense
from sklearn.model_selection import train_test_split
from pandas import read_csv

# model = load_model("./data/csv/winequality-white.csv.hdf5")

# # Load CSV
# import numpy
# filename = 'winequality-white.csv'
# raw_data = open(filename, 'rt')
# data = numpy.loadtxt(raw_data, delimiter=",")
# print(data.shape)
# 1
# import pandas as pd
# #바로 넘파이로 바꾸기
# wine = pd.read_csv('./data/csv/winequality-white.csv', sep=';',header=0, index_col=None)

import numpy as np
wine = np.genfromtxt('./data/csv/winequality-white.csv',delimiter=';')
print(wine)
'''
print(wine) #[4898 rows x 12 columns]
# import numpy as np
# np.genfromtxt('./data/csv/winequality-white.csv',delimiter=';',dtype=None)


print(type(wine))#<class 'numpy.ndarray'>



#파일형식 유지하며 csv파일 읽어들이기
# Load CSV using Pandas
# import pandas
# filename = './data/csv/winequality-white.csv'
# names = ["fixed acidity", "volatile acidity", "citric acid", "residual sugar", "chlorides", "free sulfur dioxide", "total sulfur dioxide", "density","pH", "sulphates","alcohol","quality"]
# data = pandas.read_csv(filename, names=names ,sep= ";")
print(wine.shape)  #(4899, 12)





#이거는 pd에서만 쓰는 슬라이싱 방식
# x_wine = wine.iloc[:,0:12]
# x_wine.head(12)
# print(x_wine.shape)
# y_wine = wine.iloc[:,12]
# y_wine.head(12)
# print(y_wine.shape)



# 넘파이 데이터 자르기
x_wine = wine[:,0:11]
y_wine = wine[:,11]

print(x_wine.shape)#(4899, 11)
print(y_wine.shape)#(4899,)

#1. 데이터
# dataset = data


# print("data: ",  dataset.data)

# print('target: ', dataset.target)

# x = dataset.data
# y = dataset.target
print(x_wine.shape) # (4899, 11)
print(y_wine.shape) # (4899, 1)

x_train, x_test, y_train, y_test = train_test_split(
    x_wine, y_wine, random_state=66, shuffle=True,
    train_size = 0.8)

print(x_train.shape) #(3919, 11)
print(x_test.shape)  #((980, 11)
print(y_train.shape) #(3919,)
print(y_test.shape) #((980,)




# y= np_utils.to_categorical(y)
#acc 를 구하는 거니까 분류모델인 categorical은 사용하지 않는다. 

scale = StandardScaler()
x = scale.fit_transform(x_wine)

print(x)

#2. 모델
# model = LinearSVC()    #acc =  0.903508, R2 : 0.5810223855
# model = SVC()    #acc =  0.894736, R2 : 0.54293
# model = KNeighborsClassifier()   #acc = 0.9210526, R2 : 0.65720
model = KNeighborsRegressor()
# model = RandomForestClassifier()  #acc =  0.9561403 ,R2 :  0.8095556
# model = RandomForestRegressor()



#3. 실행
model.fit(x_train,y_train)
score = model.score(x_test, y_test)

#4, 평가와 예측
y_pred = model.predict(x_test)
print("x_test : \n",x_test,"\npred values : \n",y_pred)


acc = accuracy_score(y_test, y_pred)
# print(x_test, "의 예측 결과 :", y_pred)

# # R2 구하기
# from sklearn.metrics import r2_score
# r2 = r2_score(y_test, y_pred)


# print("R2 : ", r2)
print("acc : ",acc)
print('score: ', score)
'''