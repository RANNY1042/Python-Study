import matplotlib.pyplot as plt 


korean=[50,70,20]
english=[30,50,70]

fig, ax = plt.subplots()
ax.axis([0,2,0,100])
ax.set_xlabel('학생')
ax.set_ylabel('성적')
ax.set_title('중간고사 성적')
ax.plot(korean, label='korean')
ax.plot(english, label='english')
ax.legend()

plt.show()