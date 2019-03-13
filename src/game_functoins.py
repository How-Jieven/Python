'''
Created on 2019-3-13

@author: Administrator
'''
import sys

import pygame


def check_events(ship):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # 向右移动飞船
                #ship.rect.centerx += 1
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                # 向右移动飞船
                #ship.rect.centerx += 1
                ship.moving_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                # 向右移动飞船
                #ship.rect.centerx += 1
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                # 向右移动飞船
                #ship.rect.centerx += 1
                ship.moving_left = False


def update_screen(ai_settings, screen, ship):
    """更新屏幕上的图像，并切换到新的屏幕"""
    # 每次循环的时候都切换屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # 让最近绘制的屏幕可见
    pygame.display.flip()
