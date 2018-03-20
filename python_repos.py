import requests
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS
#执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

r = requests.get(url)
print("Status code:",r.status_code)
#将API响应存储在一个变量中
response_dict = r.json()
print("Total repositories:",response_dict['total_count'])#指出GitHub包含多少个Python仓库
#探索有关仓库的信息
repo_dicts=response_dict['items']#response_dict字典存储在列表中，列表里每个字典都包含有关一个Python仓库的信息

names,plot_dicts = [],[]
for repo_dict in repo_dicts:
	names.append(repo_dict['name'])
	plot_dict ={
		'value':repo_dict['stargazers_count'],
		'label':str(repo_dict['description']),
		'xlink':repo_dict['html_url'],
		}
	plot_dicts.append(plot_dict)

#可视化
my_style = LS('#333366',base_style=LCS)
my_config = pygal.Config()#创建Pygal类Config实例，通过修改my_config定制图表外观
my_config.x_label_rotation = 45#让标签绕x轴旋转45度（x_label_rotation=45 ）
my_config.show_legend = False#隐藏图例（show_legend=False ）
my_config.title_font_size = 24#图表标题
my_config.lable_font_size =14#副标签（X轴项目名及Y轴大部分数字）
my_config.major_label_font_size = 18#主标签(Y轴5000整数倍的刻度)
my_config.truncate_label =15#将较长的项目名缩短为15个字符
my_config.show_y_guides = False#隐藏图表中的水平线
my_config.width = 1000#自定义宽度

chart = pygal.Bar(my_config,style=my_style)#通过my_config传递所有配置设置
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels=names
chart.add('',plot_dicts)
chart.render_to_file('python_repos.svg')
