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

def update_bullets(ai_settings,screen,ship,aliens,bullets):
	#更新子弹位置，并删除超出的子弹
	bullets.update()

	#销毁超出屏幕的子弹
	for bullet in bullets.copy():
		#print(len(bullets.copy()))
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)

	check_bullet_alien_collisions(ai_settings,screen,ship,aliens,bullets)
	


def check_bullet_alien_collisions(ai_settings,screen,ship,aliens,bullets):
	#检查是否击中外星人，并删除击中的子弹和外星人
	collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)

	if len(aliens) <= 0:
		#删除现有子弹，创建一群新的外星人
		bullets.empty()
		create_fleet(ai_settings,screen,ship,aliens)



def fire_bullet(ai_settings,screen,ship,bullets):
	#发射子弹
	#创建一颗子弹，并加入编组
	if len(bullets) < ai_settings.bullet_allowed:
		new_bullet = Bullet(ai_settings,screen,ship)
		bullets.add(new_bullet)


def create_fleet(ai_settings,screen,ship,aliens):
	"""创建外星人群"""
	#创建一个外星人，并计算一行可以容纳多少个
	#外星人间距为外星人宽度
	alien = Alien(ai_settings,screen)
	number_aliens_x = get_number_alien_x(ai_settings,alien.rect.width)
	number_rows = get_number_rows(ai_settings,ship.rect.height,alien.rect.height)
	#print(number_rows)

	#创建外星人群
	for row_number in range(number_rows):
		#print(row_number)
		for alien_number in range(number_aliens_x):
			#创建一个外星人并加入当前行
			creat_alien(ai_settings,screen,aliens,alien_number,row_number)


def get_number_alien_x(ai_settings,alien_width):
	"""计算每行可容纳多少外星人"""
	available_space_x = ai_settings.screen_width - 2 * alien_width
	number_aliens_x = int(available_space_x / (2 * alien_width))
	return number_aliens_x


def get_number_rows(ai_settings,ship_height,ailen_height):
	"""计算可容纳外星人行数"""
	available_space_y = (ai_settings.screen_height - (3 * ailen_height) - ship_height)
	number_rows = int (available_space_y / (2 * ailen_height))
	return number_rows


def creat_alien(ai_settings,screen,aliens,alien_number,row_number):
	"""创建一个外星人并将其放在当前行"""
	alien = Alien(ai_settings,screen)
	alien_width = alien.rect.width
	alien.x = alien_width + 2 * alien_width * alien_number
	alien.rect.x = alien.x
	#下一行
	alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
	#print(alien.rect.x,alien.rect.y)
	aliens.add(alien)


def update_aliens(ai_settings,aliens):
	check_fleet_edges(ai_settings,aliens)
	aliens.update()

		
def check_fleet_edges(ai_settings,aliens):
	#对达到边缘的外星人处理
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(ai_settings,aliens)
			break



def change_fleet_direction(ai_settings,aliens):
	#下沉改变方向
	for alien in aliens.sprites():
		alien.rect.y += ai_settings.fleet_drop_speed
	ai_settings.fleet_direction = ai_settings.fleet_direction* (-1)
