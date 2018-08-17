import pygame

from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien


def run_game():
	#初始化游戏，创建屏幕对象
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	#创建一艘飞船
	ship = Ship(ai_settings,screen)
	alien = Alien(ai_settings,screen)


	#创建一个用于存储子弹的编组
	bullets = Group()

	#开始游戏主循环
	while True:

		#监视键盘和鼠标事件
		gf.check_events(ai_settings,screen,ship,bullets)
		

		screen.fill(ai_settings.bg_color)


		ship.blitme()
		alien.blitme()
		print(str(alien.rect.x)+" "+str(alien.rect.y)+" "+str(alien.rect.width)+" "+str(alien.rect.height))

		#让最近绘制的屏幕可见
		pygame.display.flip()
		

run_game()