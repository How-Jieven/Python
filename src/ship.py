'''
Created on 2019-3-12

@author: Administrator
'''
import pygame


class Ship():

    def __init__(self, ai_settings, screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen

        "加载飞船图像并获取其外接图形"
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 在飞船的属性center中存储小数值
        self.center = float(self.rect.centerx)

        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self, ai_settings):
        """根据飞船的额移动标志调整飞船的位置"""
        if self.moving_right == True:
            # 更新ship的center值而不是rect值
            #self.rect.centerx += 1
            # 限制飞船的移动范围
            if self.moving_right and self.rect.right < self.screen_rect.right:
                self.center += 1 * ai_settings.ship_speed_factor

        """根据飞船的额移动标志调整飞船的位置"""
        if self.moving_left == True:
             # 更新ship的center值而不是rect值
            #self.rect.centerx -= 1
            # 限制飞船的移动范围
            if self.moving_left and self.rect.left > 0:
                self.center -= 1 * ai_settings.ship_speed_factor

        # 根据self.center重新设置飞船的位置
        self.rect.centerx = self.center

    def blitme(self):
        """在指定位置显示飞船"""
        self.screen.blit(self.image, self.rect)
