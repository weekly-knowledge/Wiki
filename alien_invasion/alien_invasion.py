# import sys
import pygame
from settings import Settings
from ship import Ship
from background import Background
import game_function as gf
from pygame.sprite import Group
def run_game():
    pygame.init()
    ai_settings = Settings()
    scree = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height)
    )#幕布
    pygame.display.set_caption(ai_settings.name)#游戏名称
    # bg_color = (230,230,230)#背景色
    #背景图
    background = Background(scree)
    #创建一艘飞船
    ship = Ship(ai_settings,scree)
    # pygame.image.load("saturn_family1.jpg").convert()
    """
    创建一个用于存储子弹的编组
    """
    bullets = Group()
    #开始游戏的主循环
    while True:
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         sys.exit()
        gf.check_events(ai_settings,scree,ship,bullets)
        ship.update()
        # scree.fill(ai_settings.bg_color)
        # ship.blitem()
        # pygame.display.flip()
        # gf.update_screen(ai_settings,scree,ship,background)
        bullets.update()
        gf.update_screen(ai_settings,scree,ship,background,bullets)

run_game()