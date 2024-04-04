import pandas as pd
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt


iris = load_iris()
iris = pd.DataFrame(iris.data, columns
                    =iris.feature_names) 
iris['class'] = load_iris().target
iris['class'] =iris['class'].map({0:'Setosa',1:'Versicolour',2:'Virginica'})

# plt.boxplot(iris.drop(columns='class'))
# plt.show()

# plt.boxplot(iris['sepal width (cm)'], whis=1.5)
# plt.title('sepal width (cm)')
# plt.show()

# iris[['sepal width (cm)', 'class']].boxplot(by='class')
# plt.show()

import seaborn as sns
sns.boxplot(x="class", y="sepal width (cm)", data=iris)
plt.show()