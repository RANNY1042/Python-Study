
import numpy as np
import pandas as pd

# dataset = np.array([['kor',70],['math',80]])
# df= pd.DataFrame(dataset, columns =['class','score'])
# print(df)

from sklearn.datasets import load_iris
iris = load_iris()
iris = pd.DataFrame(iris.data, columns=iris.feature_names)
# print(iris)

print(iris.head())
print(iris.tail())

print(iris.info())

print(iris.describe())

# df.set_index('class',drop=True, append=False, inplace=True)
# print(df)

# df.reset_index(drop='false', inplace=True)
# print(df)

print(iris.columns)
iris.columns=['sepal length','sepal width','petal length','petal width']
print(iris)

iris.columns = iris.columns.str.replace(' ','_')
print(iris.head(3))

print(iris.dtypes)

iris['sepal_length'] = iris['sepal_width'].astype('int')
iris[['sepal_width','petal_length']] = \
iris[['sepal_width', 'petal_length']].astype('int')
iris.head(3)


