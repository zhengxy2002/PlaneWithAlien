'''
创建时间
2021年2月17日 12:37:34
'''

class Gamestats():

    def __init__(self,ai_settings):
        self.game_active = False
        self.ai_settings = ai_settings
        self.high_score = 0
        self.level      = 1
        self.cold_speed = self.ai_settings.cold_speed
        self.heat_sum   = self.ai_settings.heat_sum

        self.reset_stats()





    def reset_stats(self):
        self.ship_left = self.ai_settings.ship_limit
        self.score = 0
        self.angle = 0
        self.over_heated = 0
        self.allowed = True
        self.bullet_left =