import pandas as pd
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import numpy as np 

iris = load_iris()
iris = pd.DataFrame(iris.data, columns=iris.feature_names)
iris['Class']=load_iris().target
iris['Class']=iris['Class'].map({0:'Setosa',1:'Vesicolour',2:'Virginica'})

#회귀선 그래프
# X, Y = iris['sepal length (cm)'], iris['petal length (cm)']
# b1,b0=np.polyfit(X,Y, 1)
# plt.scatter(x= X, y=Y, alpha=0.5)
# plt.plot(X, b1*X+b0, color='red')
# plt.show()

# iris2 = iris.sort_values(by='sepal length (cm)')

# b2, b1, b0 = np.polyfit(X,Y,2)
# plt.scatter(x=X, y=Y, alpha=0.5)
# plt.plot(X, b0 + b1*X + b2*X**2, color='red')
# plt.show()

iris2 = iris.sort_values(by='sepal length (cm)')

# plt.plot('sepal length (cm)', 'petal length (cm)', data=iris2)
# plt.show()

plt.plot('sepal length (cm) ', 'petal length (cm)', data = iris2.loc[iris2['Class']=='Setosa'])
plt.plot('sepal length (cm) ', 'petal length (cm)', data= iris2.loc[iris2['Class']=='Versicolour'])
plt.plot('sepal length (cm) ', 'petal length (cm)', data= iris2.loc[iris2['Class']=='Virginica'])
plt.legend(iris2.Class.unique())
plt.show()