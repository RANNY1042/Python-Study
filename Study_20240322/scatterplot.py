import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
from sklearn.datasets import load_iris
from pandas_profiling import ProfileReport

iris=load_iris()
iris=pd.DataFrame(iris.data, columns=iris.feature_names)
iris['Class'] = load_iris().target
iris['Class'] = iris['Class'].map({0:'Setosa', 1:'Versicolour', 2:'Veirginica'})

# scatter_matrix(iris, alpha=0.5, figsize= (8,8), diagonal ='kde')
# plt.show()

import seaborn as sns
# sns.pairplot(iris, diag_kind= 'auto', hue='Class')
# plt.show()

# iris_corr = iris.drop(columns='Class').corr(method='pearson')
# sns.heatmap(iris_corr, xticklabels = iris_corr.columns, yticklabels = iris_corr.columns, cmap='RdBu_r', annot=True)
# plt.show()

import pandas_profiling as ProfileReport
ProfileReport(iris)