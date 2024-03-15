
import matplotlib.pyplot as plt

x = list(range(1,101))
squares=[i**2 for i in x]

plt.scatter(x,squares, c=squares, cmap=plt.cm.Blues)
plt.colorbar()
plt.savefig('colorbar.png')
plt.show()

# ax.set_title('Square')
# ax.set_xlabel('X')
# ax.set_ylabel('Y')

# # # ax.plot(squares, linewidth=5)

# # ax.set_title("Square Numbers", fontsize=20)
# # ax.set_xlabel("Value",fontsize=14)
# # ax.set_ylabel("Square of Value",fontsize=14)

# # # ax.tick_params(labelsize=20)
# # plt.style.use('seaborn-v0_8-pastel')
# # ax.ticklabel_format(style='plain')
# ax.plot(squares, color="red")

# plt.show()