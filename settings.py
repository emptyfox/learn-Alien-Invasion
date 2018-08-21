class Settings():
	"""存储所有设置的类"""

	def __init__(self):
		#初始化游戏设置

		#屏幕设置
		self.screen_width = 800
		self.screen_height = 600
		self.bg_color = (230,230,230)

		#飞船设置
		
		self.ship_limit = 3
		self.ship_image = 'images/ship.bmp'

		#子弹设置
		
		self.bullet_width = 3
		self.bullet_height = 5
		self.bullet_color = (60,60,60)
		self.bullet_allowed = 30

		#外星人设置
		self.alien_image = 'images/alien.bmp'
		
		self.fleet_drop_speed = 15

		self.speedup_scale = 1.1
		self.score_scale = 1.5

		self.initialize_dynamic_settings()
		
		

	def initialize_dynamic_settings(self):
		#动态设置
		self.ship_speed_factor = 5
		self.bullet_speed_factor = 1
		self.alien_speed_factor = 5
		self.fleet_direction = 1
		self.alien_points = 50

	def increase_speed(self):
		#提高速度
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale

		self.alien_points = int(self.score_scale*self.alien_points)
		

