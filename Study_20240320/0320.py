from matplotlib import pyplot as plt

import random
from random import randint

# x= [randint(0,9) for _ in range(1000)]
x1 = list(range(1,5))
y1 = [i*i for i in x1]

x2 = list(range(1,5))
y2 =[i**3 for i in x2]

plt.plot(x1,y1, label='A')
plt.plot(x1,y2, label='B')

plt.title('X square')
plt.xlabel('X')
plt.ylabel('X square')
plt.show()
# print(x,type(x))
 
# plt.hist(x)
# plt.show()