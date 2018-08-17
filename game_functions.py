import sys

import pygame
from bullet import Bullet
from alien import Alien

def check_events(ai_settings,screen,ship,bullets):
	#响应按键和鼠标事件

	for event in pygame.event.get():
		if event.type == pygame.QUIT :
			sys.exit()

		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event,ai_settings,screen,ship,bullets)

		elif event.type == pygame.KEYUP:
			check_keyup_events(event,ship)


			


def check_keydown_events(event,ai_settings,screen,ship,bullets):
	#响应按下键盘
	if event.key == pygame.K_RIGHT:
		#向右移动
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		#向左移动
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(ai_settings,screen,ship,bullets)
	elif event.key == pygame.K_q:
		sys.exit()
		

def check_keyup_events(event,ship):
	#响应松开键盘
	if event.key == pygame.K_RIGHT:
		#停止向右移动
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		#停止向左移动
		ship.moving_left = False

def update_screen(ai_settings,screen,ship,aliens,bullets):
	#更新屏幕上的图像，并切换到新屏幕
	#每次循环时都重绘制屏幕
	screen.fill(ai_settings.bg_color)

	#在飞船和外星人后面重绘所有子弹
	for bullet in bullets.sprites():
		bullet.draw_bullet()

	ship.blitme()
	#alien.blitme()
	aliens.draw(screen)

	#让最近绘制的屏幕可见
	pygame.display.flip()

def update_bullets(bullets):
	#更新子弹位置，并删除超出的子弹
	bullets.update()

	#销毁超出屏幕的子弹
	for bullet in bullets.copy():
		#print(len(bullets.copy()))
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)


def fire_bullet(ai_settings,screen,ship,bullets):
	#发射子弹
	#创建一颗子弹，并加入编组
	if len(bullets) < ai_settings.bullet_allowed:
		new_bullet = Bullet(ai_settings,screen,ship)
		bullets.add(new_bullet)


def create_fleet(ai_settings,screen,aliens):
	"""创建外星人群"""
	#创建一个外星人，并计算一行可以容纳多少个
	#外星人间距为外星人宽度
	alien = Alien(ai_settings,screen)
	alien_width = alien.rect.width
	available_space_x = ai_settings.screen_width - 2 * alien_width
	number_aliens_x = int(available_space_x / (2 * alien_width))

	#创建第一行外星人
	for alien_number in range(number_aliens_x):
		#创建一个外星人并加入当前行
		alien = Alien(ai_settings,screen)
		alien.x = alien_width + 2 * alien_width * alien_number
		alien.rect.x = alien.x
		aliens.add(alien)
		
	
