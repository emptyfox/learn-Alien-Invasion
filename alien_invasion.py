import sys

import pygame

def run_game():
	#初始化游戏，创建屏幕对象
	pygame.init()
	screen = pygame.display.set_mode((1200,800))
	pygame.display.set_caption("Alien Invasion")


	#开始游戏主循环
	while True:

		#监视键盘和鼠标事件
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		#最近绘制屏幕可见
		pygame.display.flip()

run_game()