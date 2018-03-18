from die import Die
import pygal
#创建两个D6骰子
die_1 = Die()
die_2 = Die()
#掷多次骰子，并将结果存储在一个列表中
results=[die_1.roll()+die_2.roll() for roll_number in range(1000)]
	
#分析结果统计次数
max_result = die_1.num_sides + die_2.num_sides
frequencies =[results.count(value) for value in range(2,max_result+1)]

#对结果进行可视化 直方图
hist = pygal.Bar()
hist.title = "Result of rolling two D6 1000 times."
hist.x_labels=[x for x in range(2,max_result+1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6+D6',frequencies)
hist.render_to_file('dice_visual.svg')
