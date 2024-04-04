import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine

wine_load = load_wine()
wine = pd.DataFrame(wine_load, columns= wine_load.feature_names)
# wine['Class']=wine_load.target
# wine['Class']=wine['Class'].map({0:'class_0',1:'class_1',2:'class_2'})

# wine_type = wine['Class'].value_counts()
# print(wine_type)

# plt.bar(wine_type.index, wine_type.values, width=0.8, bottom=None, align='center')
# plt.show()

# plt.barh(wine_type.index, wine_type.values, height=0.8, left=None, align='edge')
# plt.show()

plt.title('Wine alcohol histogram')
plt.hist('alchol', bins=8, range=(11,15), color='purple', data=wine)
plt.show()