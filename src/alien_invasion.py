import sys
import pygame
from settings import Settings
from ship import Ship
import game_functoins as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button


def run_game():
    print('execute run_game')
    # 初始化游戏并创建一个游戏屏幕对象
    ai_settings = Settings()
    pygame.init()
    # 设置当前界面的大小
    # screen=pygame.display.set_mode((1200,650))
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    # 设置界面的标题
    pygame.display.set_caption("alien Invasion")
    # 创建Play按钮
    play_button = Button(ai_settings, screen, "Play")
    # 设置背景颜色
    # bg_color=(230,230,230)
    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()
    #alien = Alien(ai_settings, screen)
    aliens = Group()
    gf.creat_fleet(ai_settings, screen, ship, aliens)

    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)
    while True:
        # 监视键盘和鼠标事件
       # for event in pygame.event.get():
          #  if event.type==pygame.QUIT:
           #     sys.exit()
        gf.check_events(
            ai_settings, screen, stats, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update(ai_settings)
            # gf.update_bullets(aliens, bullets)
            # bullets.update()
            # 删除已经消失的子弹
            """for bullet in bullets.copy():
                if bullet.rect.bottom <= 0:
                    bullets.remove(bullet)"""
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            print(len(bullets))
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
            # 每次循环的时候都重绘屏幕
            # screen.fill(bg_color)
            # screen.fill(ai_setti ngs.bg_color)
            # ship.blitme()
            # 每次循环时都重绘屏幕（让最近绘制的屏幕可见）
            # pygame.display.flip()
        gf.update_screen(
            ai_settings, screen, stats, ship, aliens, bullets, play_button)
run_game()
