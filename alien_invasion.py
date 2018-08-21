import pygame

from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from socreboard import Scoreboard


def run_game():
	#初始化游戏，创建屏幕对象
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	#创建play按钮
	play_button = Button(ai_settings,screen,"play")

	#创造统计实例
	stats = GameStats(ai_settings)
	#计分板实例
	sb = Scoreboard(ai_settings,screen,stats)
	#创建一艘飞船
	ship = Ship(ai_settings,screen)


	#创建一个用于存储子弹的编组
	bullets = Group()

	#创建一个外星人
	#alien = Alien(ai_settings,screen)
	#创建一组外星人
	aliens = Group()

	#创建外星人群
	gf.create_fleet(ai_settings,screen,ship,aliens)


	#开始游戏主循环
	while True:

		#监视键盘和鼠标事件
		gf.check_events(ai_settings,screen,stats,sb,play_button,ship,aliens,bullets)
		if stats.game_active:
			ship.update()
			gf.update_bullets(ai_settings,screen,stats,sb,ship,aliens,bullets)
			gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets)
			
		gf.update_screen(ai_settings,screen,stats,sb,ship,aliens,bullets,play_button) 

		sleep(2)


run_game()