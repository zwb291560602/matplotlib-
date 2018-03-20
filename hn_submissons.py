import requests
from operator import itemgetter
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


#执行API调用并存储响应
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
#打印请求状态（200表示成功）
print("Status code:",r.status_code)

#处理有关每篇文章的信息
#将包含ID信息的响应文本转换为列表
submission_ids = r.json()
#创建空列表存储文章信息（字典）
submission_dicts = []

#通过ID遍历前30篇文章，并执行API调用
for submission_id in submission_ids[:3]:
	#对于每篇文章都执行一个API调用
	url = ('https://hacker-news.firebaseio.com/v0/item/' +
		str(submission_id) + '.json')
	submission_r = requests.get(url)
	print(submission_r.status_code)
	response_dict = submission_r.json()

	submission_dict = {
		'title': response_dict['title'],#标题
		'link': 'http://news.ycombinator.com/item?id=' + 
			str(submission_id),#讨论页面链接
		#不确定某个键是否包含在字典中时，使用方法dict.get()
		#它在指定的键存在时返回与之相关联的值
		#并在指定的键不存在时返回你指定的值（这里是0）
		'comments': response_dict.get('descendants', 0)#评论数
		}
	submission_dicts.append(submission_dict)
#根据comments降序排列
submission_dicts = sorted(submission_dicts, key = itemgetter('comments'), 
	reverse = True)
for submission_dict in submission_dicts:
	print("\nTitle:",submission_dict['title'])
	print("Discussion link:",submission_dict['link'])
	print("Comments:",submission_dict['comments'])

titles,plot_dicts = [],[]
for submission_dict in submission_dicts:
	titles.append(submission_dict['title'])
	plot_dict = {
		'value':submission_dict['comments'],
		'label':submission_dict['title'],
		'xlink':submission_dict['link'],
		}
	plot_dicts.append(plot_dict)

my_style = LS('#333366',base_style = LCS)
my_style.title_font_size = 24
my_style.label_font_size = 14
my_style.major_lable_font_size = 18

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_lenged = False
my_config.truncate_label = 15 #将较长的项目名缩短为15个字符
my_config.show_y_guides = False #隐藏图表中的水平线
my_config.width = 1000
my_config.y_title = 'Number of Comments'

chart = pygal.Bar(my_config, style = my_style)
chart.title = 'Most Active Discussions on Hacker News'
chart.x_labels = titles
chart.add('',plot_dicts)
chart.render_to_file('hn_discussions.svg')
