import pygame
"""
背景
"""
class Background():
    def __init__(self,screen):
        self.background = pygame.image.load('images/background.jpg').convert()# 背景图
        self.screen = screen
    def blitem(self):
        self.screen.blit(self.background,(0, 0))#blit( )方法，这次是把上一步粘貼好文本的background再拷贝在screen上，（0，0）表示从坐标原点开始就是从左上角开始；