import pygame
"""
飞船
"""
class Ship():
    def __init__(self,ai_settings,screen):
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()#得到曲面的矩形区域
        self.screen_rect = screen.get_rect()
        # print(screen.get_rect)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)
        self.moving_right = False#移动标志
        self.moving_left = False
        self.moving_top = False
        self.moving_bottom = False
    def update(self):
        """
        根据移动标志调整飞船的位置
        :return:
        """
        if self.moving_right and self.rect.right < self.screen_rect.right:
            # self.rect.centerx += 1
            self.center += self.ai_settings.ship_speed_factor
        elif self.moving_left and self.rect.left > 0:
            # self.rect.centerx -= 1
            self.center -= self.ai_settings.ship_speed_factor
        elif self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:
            self.rect.bottom += 1
        elif self.moving_top and self.rect.top > 0:
            self.rect.top -= 1
        self.rect.centerx = self.center
    def blitem(self):
        """
             飞船初始化位置
        """
        self.screen.blit(self.image,self.rect)