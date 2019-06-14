import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """
    对飞机发射子弹控制的类
    """
    def __init__(self,ai_settings,screen,ship):
        """
        在飞机的位置创建一个对象类
        :param ai_settings:
        :param screen:
        :param ship:
        """
        # super(Bullet,self).__init__()#2.7使用法
        super().__init__()
        self.screen = screen

        """
        在（0，0）处创建一个表示子弹的矩形，再设置正确的位置
        """
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        """
        存储用小数表示的子弹位置
        """
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """
        向上移动子弹
        :return:
        """
        #更新子弹位置的小数
        self.y -= self.speed_factor
        #更新位置
        self.rect.y = self.y
    def draw_bullet(self):
        """
        屏幕出现子弹
        :return:
        """
        pygame.draw.rect(self.screen,self.color,self.rect)