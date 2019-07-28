import sys
import pygame
from settings import Settings

def run_game():
    """初始化游戏并创建一个屏幕对象"""
    pygame.init() #初始化pygame
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.secrrn_height)) #调用pygame类来创建一个屏幕对象并设置大小 之所以又两个括号是因为这是一个元组 而不简单是两个括号
    pygame.display.set_caption("Alien Invasion")#设置屏幕显示的名字

    #设置背景色
    bg_color = (230,230,230)

    #开始游戏主循环
    while True:
        #键是键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        #每次循环都重新绘制屏幕
        screen.fill(ai_settings.bg_color)

        #让最近绘制的屏幕可见
        pygame.display.flip()

run_game()
