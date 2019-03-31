'''
Created on 2019-3-13

@author: Administrator
'''
import sys

import pygame

from bullet import Bullet

from ship import Ship

from alien import Alien


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


def update_screen(ai_settings, screen, ship, aliens, bullets):
    """更新屏幕上的图像，并切换到新的屏幕"""
    # 每次循环的时候都切换屏幕
    screen.fill(ai_settings.bg_color)
    # 在飞船和外星人后面重绘 所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
   # 对编组调用draws的时候，Python会自动绘制编组的每一个元素，绘制的位置有每一个元素的rect决定
    aliens.draw(screen)
    # alien.blitme()
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
        """ if len(bullets) < ai_settings.bullet_allowed:
            new_Bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_Bullet)"""
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_bullets(bullets):
    """更新子弹的位置，并删除已经消失的子弹"""
    # 更新子弹的位置
    bullets.update()

    # 删除已经消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def fire_bullet(ai_settings, screen, ship, bullets):
    """如果还没有到达限制，就发射一颗子弹"""
    # 创建新的子弹，并将其加入到编组bullets中去
    if len(bullets) < ai_settings.bullet_allowed:
        new_Bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_Bullet)


def creat_fleet(ai_settings, screen, ship, aliens):
    """创建外星人群"""
    # 创建一个外星人，并计算一行可以容纳多少个外星人
    # 外星人间距是外星人的宽度
    alien = Alien(ai_settings, screen)
    #alien_width = alien.rect.width
    #alien_height = alien.rect.height
    #available_space_x = ai_settings.screen_width - 2 * alien_width
    #number_aliens_x = int(available_space_x / (2 * alien_width))
    number_aliens_x = get_number_alines_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(
        ai_settings, ship.rect.height, alien.rect.height)

    # 创建第一个外星人-->创建外星人群
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            # 创建一个外星人并将其加入当前行
            """alien = Alien(ai_settings, screen)
            alien.x = alien_width + 2 * alien_width * alien_number
            alien.rect.x = alien.x
            aliens.add(alien)"""
            creat_alien(ai_settings, screen, aliens, alien_number, row_number)


def get_number_alines_x(ai_settings, alien_width):
    """计算每行可以容纳多少个外星人（屏幕宽度-2倍的外星人宽度）除以外星人宽度"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def creat_alien(ai_settings, screen, aliens, alien_number, row_number):
    """创建一个外星人并将其放在当前行"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    alien.rect.x = alien.x
    aliens.add(alien)


def get_number_rows(ai_settings, ship_height, aline_height):
    """计算屏幕可以容纳多少行外星人"""
    avaliable_space_y = (
        ai_settings.screen_height - 3 * (aline_height) - ship_height)
    number_row = int(avaliable_space_y / (2 * (aline_height)))
    return number_row


def update_aliens(aliens):
    """更新外星人群中所有外星人的位置"""
    aliens.update()