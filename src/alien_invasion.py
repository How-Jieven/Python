import sys
import pygame
def run_game():
    #初始化游戏并创建一个游戏屏幕对象
    pygame.init()
    #设置当前界面的大小
    screen=pygame.display.set_mode((1200,650))
    #设置界面的标题
    pygame.display.set_caption("alien Invasion")
    while True:
        #监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
        #每次循环时都重绘屏幕（让最近绘制的屏幕可见）
        pygame.display.flip()
run_game()