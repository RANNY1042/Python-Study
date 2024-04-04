import pandas as pd
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
iris = load_iris()
iris = pd.DataFrame(iris.data, columns=iris.feature_names)
iris['class']=load_iris().target
iris['class']=iris['class'].map({0:'Setosa',1:'Vesicolour',2:'Virginica'})

def linear_func(x):
    return 2*x+1

x=iris['sepal length (cm)']
plt.plot(x, linear_func(x), c='#789395')
plt.show()