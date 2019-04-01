'''
Created on 2019-3-12

@author: Administrator
'''
import bullet


class Settings():
    "存储《外星人入侵》 的所有设置的类"

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 650
        self.bg_color = (230, 230, 230)

        # 飞船的设置
        self.ship_speed_factor = 1.5

        # 子弹的设置
        self.bullet_speed_factor = 3
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 3

        # 外星人的设置
        self.aline_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction为1表示向右，为-1表示向左
        self.fleet_direction = 1
