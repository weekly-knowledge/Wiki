class Settings():
    """
    初始化
    """
    def __init__(self):
        '''
        飞机设置和屏幕设置
        '''
        self.screen_width = 800
        self.screen_height = 600
        self.name = '打飞机'
        #self.bg_color = (230,230,230)背景色
        self.ship_speed_factor = 1.5
        '''
        子弹设置
        '''
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60