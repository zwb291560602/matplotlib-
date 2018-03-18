import csv
from matplotlib import pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates
#从文件中获取最高气温
filename = 'death_valley_2014.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	dates, highs, lows = [], [], []
	for row in reader:
		try:
			current_date = datetime.strptime(row[0], "%Y-%m-%d")
			high = int(row[1])
			low = int(row[3])
		except ValueError:
			print(current_date,'missing data')
		else:
			dates.append(current_date)
			highs.append(high)
			lows.append(low)
#根据数据绘制图形
fig=plt.figure(dpi=128,figsize=(10,6))
plt.plot(dates,highs,c='red',alpha=0.5)
plt.plot(dates,lows,c='blue',alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)

#设置图形格式
plt.title("Daily high and low temperatures - 2014\nDeath Valley,CA",fontsize=24)
plt.xlabel("",fontsize=16)
#配置横坐标
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%Y'))
plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
fig.autofmt_xdate()#让日期标签倾斜
plt.ylabel("Temperature(F)",fontsize=16)
plt.tick_params(axis='both',which = 'major',labelsize=10)
plt.ylim(10,120)
plt.xlim(dates[0],dates[-1])
plt.show()
