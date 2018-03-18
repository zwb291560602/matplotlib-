from die import Die
import pygal
#创建一个D6
die = Die()
#掷几次骰子，并将结果存储在一个列表中
results=[die.roll() for roll_number in range(1000)]
	
#分析结果统计次数
frequencies =[results.count(value) for value in range(1,die.num_sides+1)]

#对结果进行可视化 直方图
hist = pygal.Bar()
hist.title = "Result of rolling one D6 1000 times."#标题
hist.x_labels=[x for x in range(1,die.num_sides+1)]#横坐标
hist.x_title = "Result"#横轴标题
hist.y_title = "Frequency of Result"#纵轴标题

hist.add('D6',frequencies)#将值添加到图表中
hist.render_to_file('die_visual.svg')#将图表渲染为svg文件
