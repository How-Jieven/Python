'''
Created on 2019-3-13

@author: Administrator
'''
import sys

import pygame

from bullet import Bullet

from ship import Ship


def check_events(ai_settings, screen, ship, bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            '''if event.key == pygame.K_RIGHT:
                # 向右移动飞船
                #ship.rect.centerx += 1
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                # 向右移动飞船
                #ship.rect.centerx += 1
                ship.moving_left = True'''
            #check_keydown_events(event, ship)
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            '''if event.key == pygame.K_RIGHT:
                # 向右移动飞船
                #ship.rect.centerx += 1
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                # 向右移动飞船
                #ship.rect.centerx += 1
                ship.moving_left = False'''
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, bullets):
    """更新屏幕上的图像，并切换到新的屏幕"""
    # 每次循环的时候都切换屏幕
    screen.fill(ai_settings.bg_color)
    # 在飞船和外星人后面重绘 所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()

    # 让最近绘制的屏幕可见
    pygame.display.flip()


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # 创建新的bullet对象并将其加入到编组bullets中
        if len(bullets) < ai_settings.bullet_allowed:
            new_Bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_Bullet)


def check_keyup_events(event, ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
