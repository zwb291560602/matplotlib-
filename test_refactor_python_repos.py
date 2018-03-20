import unittest
import python_repos_for_testing as pr

class PythonReposTestCase(unittest.TestCase):
	"""测试refactor_python_repos.py"""
	def setUp(self):
		"""调用所有的函数，并分别测试元素。"""
		self.response = pr.get_response()
		self.repo_dicts = pr.get_repo_dicts(self.response)
		self.repo_dict = self.repo_dicts[0]
		self.names,self.plot_dicts = pr.get_names_plot_dicts(self.repo_dicts)

	def test_get_response(self):
		"""测试并得到一个有效响应"""
		self.assertEqual(self.response.status_code,200)
	
	def test_repo_dicts(self):
		"""测试得到的数据"""
		#获取30组响应
		self.assertEqual(len(self.repo_dicts),30)
		required_keys = ['name','owner','stargazers_count','html_url']
		#Repositories应该具有所需的密钥
		for key in required_keys:
			self.assertTrue(key in self.repo_dict.keys())

unittest.main()
