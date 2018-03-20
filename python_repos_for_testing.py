import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

def get_response():
	"""执行API调用,存储响应,并返回响应"""
	url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
	response = requests.get(url)
	return response
	
def get_repo_dicts(response):
	"""响应信息存储在列表中，并返回列表"""
	response_dict = response.json()
	#探索有关仓库的信息
	#response_dict字典存储在列表中，列表里每个字典都包含有关一个Python仓库的信息
	repo_dicts=response_dict['items']
	return repo_dicts

def get_names_plot_dicts(repo_dicts):
	"""处理字典列表，并返回数据以进行绘图"""
	names,plot_dicts = [],[]
	for repo_dict in repo_dicts:
		names.append(repo_dict['name'])
		#一些项目缺少描述，在标签栏中会导致错误。如果没有描述，指定一个标签。
		description = repo_dict['description']
		if not description:
			description = "No description provided ."
		plot_dict ={
			'value':repo_dict['stargazers_count'],
			'label':str(repo_dict['description']),
			'xlink':repo_dict['html_url'],
			}
		plot_dicts.append(plot_dict)
	return names,plot_dicts

def make_visualization(names,plot_dicts):
	"""可视化"""
	my_style = LS("#333366",base_style = LCS)
	my_style.title_font_size = 24
	my_style.lable_font_size = 14
	my_style.major_lable_font_size = 18
	
	my_config = pygal.Config()
	my_config.x_label_rotation = 45#让标签绕x轴旋转45度（x_label_rotation=45 ）
	my_config.show_legend = False#隐藏图例（show_legend=False ）
	my_config.truncate_label = 15#将较长的项目名缩短为15个字符
	my_config.show_y_guides = False #隐藏图表中的水平线
	my_config.width = 1000#自定义宽度
	
	chart = pygal.Bar(my_config,style = my_style)
	chart.title = 'Most-Starred Python Projects on GitHub'
	chart.x_labels = names
	chart.add('',plot_dicts)
	chart.render_to_file('refactor_python_repos.svg')
	

response = get_response()
repo_dicts = get_repo_dicts(response)
names,plot_dicts = get_names_plot_dicts(repo_dicts)
make_visualization(names,plot_dicts)
