import matplotlib.pyplot as plt

x_values = list(range(1,101))
y_values = [x**2 for x in x_values]
plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,edgecolor='none',s=40)

#设置图表标题并给坐标轴加上标签
plt.title("Square Number",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)
#设置刻度标记的大小
plt.tick_params(axis='both',which='major',labelsize=14)
plt.axis([0,110,0,12100])
plt.show()
