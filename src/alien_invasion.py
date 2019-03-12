import sys
import pygame
from settings import Settings
from ship import Ship 
def run_game():
    print('execute run_game')
    #初始化游戏并创建一个游戏屏幕对象
    ai_settings=Settings()
    pygame.init()
    #设置当前界面的大小
    #screen=pygame.display.set_mode((1200,650))
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    #设置界面的标题
    pygame.display.set_caption("alien Invasion")
    #设置背景颜色
    #bg_color=(230,230,230)
    #创建一艘飞船
    ship=Ship(screen)
    while True:
        #监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
                
        #每次循环的时候都重绘屏幕
        #screen.fill(bg_color)
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        #每次循环时都重绘屏幕（让最近绘制的屏幕可见）
        pygame.display.flip()
run_game()