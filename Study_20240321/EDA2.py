
import pandas as pd
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt

iris = load_iris()
iris = pd.DataFrame(iris.data, columns=iris.feature_names)
iris['class'] = load_iris().target
iris['class'] = iris['class'].map({0:'Setosa',1:'Versicolour',2:'Virginica'})

# plt.title('iris scatter')
# plt.xlabel('sepal length (cm)')
# plt.ylabel('sepal width (cm)')

# plt.scatter(x=iris['sepal length (cm)'], y=iris['sepal width (cm)'],
#             alpha=0.5)

# plt.show()

import seaborn as sns

sns.scatterplot(x='sepal length (cm)', y='sepal width (cm)', data=iris, hue='class', style='class')
plt.show()