import pygame.font

class Scoreboard():

    def __init__(self,ai_settings,screen,stats):

        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        self.text_color = (0,0,0)
        self.font = pygame.font.SysFont(None,48)

        self.prep_score()
        self.prep_high_score()
        self.prep_ship_left()
        self.prep_level()
        self.prep_over_heated()

        self.lable_width,self.lable_height = 175,50
        self.lable_color      = (100,255,100)

        self.lable_rect = pygame.Rect(0,0,self.lable_width,self.lable_height)
        self.lable_rect.centerx = self.screen_rect.centerx
        self.lable_rect.top  = self.screen_rect.top

    def prep_score(self):

        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str,True,self.text_color,self.ai_settings.bg_color)


        self.score_rect = self.score_image.get_rect()
        self.score_rect.centerx = self.screen_rect.centerx
        self.score_rect.top  = self.screen_rect.top

    def show_score(self):

        self.screen.fill(self.lable_color, self.lable_rect)
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.screen.blit(self.ship_left_image,self.ship_left_rect)
        self.screen.blit(self.level_image,self.level_rect)
        self.screen.blit(self.over_heated_image,self.over_heated_rect)

    def prep_high_score(self):

        high_score = int(round(int(self.stats.high_score),-1))
        high_score_str = "High Score:%s"%('{:,}'.format(high_score))
        self.high_score_image = self.font.render(high_score_str,True,self.text_color,self.ai_settings.bg_color)

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.right = self.screen_rect.right
        self.high_score_rect.top   = self.screen_rect.top

    def prep_ship_left(self):
        ship_left = self.stats.ship_left
        ship_left_str = 'Ship Left:%d'%(ship_left)
        self.ship_left_image = self.font.render(ship_left_str,True,self.text_color,self.ai_settings.bg_color)

        self.ship_left_rect = self.ship_left_image.get_rect()
        self.ship_left_rect.left = self.screen_rect.left
        self.ship_left_rect.top  = self.screen_rect.top

    def prep_level(self):
        level_number = self.stats.level
        level_number_str = 'Round:%d'%(level_number)
        self.level_image = self.font.render(level_number_str,True,self.text_color,self.ai_settings.bg_color)

        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.screen_rect.right
        self.level_rect.top   = self.high_score_rect.bottom + 15

    def prep_over_heated(self):
        over_heated = self.stats.over_heated
        over_heated_str = 'Over_heat!'
        if over_heated >= self.stats.heat_sum:
            over_heated_color = (255, 0, 0)
        elif over_heated < self.stats.heat_sum:
            over_heated_color = self.ai_settings.bg_color
        self.over_heated_image = self.font.render(over_heated_str,True,over_heated_color,self.ai_settings.bg_color)

        self.over_heated_rect = self.over_heated_image.get_rect()
        self.over_heated_rect.left = self.screen_rect.left
        self.over_heated_rect.top = self.screen_rect.centery
