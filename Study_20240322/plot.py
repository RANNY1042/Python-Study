import pandas as pd
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
iris = load_iris()
print(iris)
iris=pd.DataFrame(iris.data, columns=iris.feature_names)
print(iris.head())
# iris =pd.DataFrame(iris.data, columns = iris.feature_names)
iris['Class']=load_iris().target
print(iris['Class'])
iris['Class'] = iris['Class'].map({0:'Setosa', 1:'Versicolour', 2:'Virginica'})

iris2 = iris.sort_values(by='sepal length (cm)')
print(iris2.head())
plt.plot('sepal length (cm)', 'petal length (cm)', data=iris2.loc[iris2['Class'] =='Setosa'])
plt.plot('sepal length (cm)', 'petal length (cm)', data=iris2.loc[iris2['Class'] =='Versicolour'])
plt.plot('sepal length (cm)', 'petal length (cm)', data=iris2.loc[iris2['Class'] =='Virginica'])

plt.legend(iris2.Class.unique())
plt.show()