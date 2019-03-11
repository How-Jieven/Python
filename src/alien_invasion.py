import sys
import pygame
def run_game():
    #初始化游戏并创建一个游戏屏幕对象
    pygame.init()
    screen=pygame.display.set_mode((1200,650))
    pygame.display.set_caption("alien Invasion")
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
        #每次循环时都重绘屏幕
        pygame.display.flip()
run_game()