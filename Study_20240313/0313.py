
import pandas as pd
import numpy as np

dataset = np.array([['kor',70], ['math',80]])
df = pd.DataFrame(dataset, columns = ['class','score'])
df.to_csv('Class.csv', header=True, index=True, encoding='utf8')
print(df)

