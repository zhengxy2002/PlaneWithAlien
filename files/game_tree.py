'''
该文档主要用途在于存储游戏的设置
包括分辨率、背景色等
也包括以后可能的任何设定
还有部分函数的重构也将放在此处
'''
import pygame
import sys
from alien  import Alien
from random import randint
from time import sleep

class Settings():                          #设置基础数据
    def __init__(self):

        self.screen_width = 1920
        self.screen_height= 1080
        self.caption = 'Plane With Alien'
        self.plane_speed = 1.5
        self.bullet_magazine = 100
        self.screen_pixel = (self.screen_width,self.screen_height)
        self.alien_moving_speed_s = 1.0
        self.fleet_drop_speed = 10.0
        self.alien_direction = 1.0
        self.ship_limit = 3
        self.speedup_scale = (randint(70,130))/100
        self.bullet_speed_factor = 3.0
        self.bg_color = (255,255,255)
        self.alien_points = 50
        self.cold_speed = 10
        self.heat_sum = 70


    def initialize_dynamic_settings(self):
        self.plane_speed = 1.5
        self.bullet_speed_factor = 3.0
        self.alien_moving_speed_s = 1.0
        self.fleet_drop_speed   = 10
        self.alien_points = 50



        self.fleet_direction = 1

    def increase_speed(self):

        self.plane_speed            *= self.speedup_scale
        self.bullet_speed_factor    *= self.speedup_scale
        self.alien_moving_speed_s   *= self.speedup_scale
        self.fleet_drop_speed       *= self.speedup_scale
        self.alien_points           = int(self.speedup_scale*self.alien_points)



setting = Settings()


def game_control(ship,screen,bullets,stats,play_button,aliens,scoreboard,ai_settings):                        #检测键盘和鼠标

    for event in pygame.event.get():
        if event.type == pygame.QUIT:           #这里是用来退出的
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings,stats,play_button,mouse_x,mouse_y,ship,aliens,bullets,screen,scoreboard)

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                sys.exit()

            elif event.key == pygame.K_p:
                stats.game_active = True

            elif event.key == pygame.K_RIGHT:
                ship.moving_right = True
                stats.over_heated += 20

            elif event.key == pygame.K_LEFT:
                ship.moving_left  = True
                stats.over_heated += 20

            elif event.key == pygame.K_DOWN:
                ship.moving_down  = True
                stats.over_heated += 20

            elif event.key == pygame.K_UP:
                ship.moving_up  = True
                stats.over_heated += 20

            elif event.key == pygame.K_d:
                ship.moving_right = True
                stats.over_heated += 20

            elif event.key == pygame.K_a:
                ship.moving_left  = True
                stats.over_heated += 20

            elif event.key == pygame.K_s:
                ship.moving_down  = True
                stats.over_heated += 20

            elif event.key == pygame.K_w:
                ship.moving_up  = True
                stats.over_heated += 20

            elif event.key == pygame.K_c:
                change_angle(stats,ship,screen)

            elif event.key == pygame.K_SPACE:
                if stats.angle == 0:
                    ship.fire_allowed     = True
                    stats.over_heated += 30
                elif stats.angle == 180:
                    ship.fire_back_allowed = True
                    stats.over_heated += 30

            elif event.key == pygame.K_x:
                ship.ship_cold = True

            elif event.key == pygame.K_z:
                ship_hit(stats, screen, ship, aliens, bullets, scoreboard)



        elif event.type == pygame.KEYUP:

            if event.key == pygame.K_RIGHT:
                ship.moving_right = False

            elif event.key == pygame.K_LEFT:
                ship.moving_left = False

            elif event.key == pygame.K_DOWN:
                ship.moving_down = False

            elif event.key == pygame.K_UP:
                ship.moving_up = False

            elif event.key == pygame.K_d:
                ship.moving_right = False

            elif event.key == pygame.K_a:
                ship.moving_left  = False

            elif event.key == pygame.K_s:
                ship.moving_down  = False

            elif event.key == pygame.K_w:
                ship.moving_up  = False

            elif event.key == pygame.K_SPACE:
                ship.fire_back_allowed = False
                ship.fire_allowed      = False

            elif event.key == pygame.K_x:
                ship.ship_cold = False


def screen_make_it_newer(ship,screen,bullets,aliens,play_button,stats,scoreboard):             #刷新屏幕
    screen.fill((255,255,255))

    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()

    aliens.draw(screen)

    if not stats.game_active:
        play_button.draw_button()

    check_ship_allowed(stats)

    scoreboard.prep_over_heated()

    scoreboard.show_score()

    pygame.display.flip()

def bullets_moving(bullets,aliens,screen,ship,ai_settings,stats,scoreboard):
    bullets.update()

    for bulllet in bullets.copy():
        if bulllet.rect.bottom <= 0 or bulllet.rect.bottom >= ai_settings.screen_height:
            bullets.remove(bulllet)

    check_bullet_alien_collisions(screen,ship,aliens,bullets,ai_settings,stats,scoreboard)

def create_enemies(screen,aliens,ship):

    alien = Alien(screen,setting)

    alien_width = alien.rect.width
    alien_height= alien.rect.height

    alien_number = get_number_aliens_x(screen,alien_width)
    row_numbers = get_number_rows(screen,alien.rect.height,ship.rect.height)

    for row_number in range(row_numbers):
        for alien_numbers in range(alien_number):
            random_judge_number = randint(0,1)
            if random_judge_number == 1:
                alien = Alien(screen,setting)

                alien.x = alien_width + 2 * alien_width * alien_numbers
                alien.rect.x = alien.x
                alien.y = alien_height + 2 * alien_height * row_number
                alien.rect.y = alien.y

                aliens.add(alien)

            else:
                continue

def get_number_aliens_x(screen,alien_width):

    screen_rect = screen.get_rect()

    available_space_x =  screen_rect.width - 2* alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))

    return number_aliens_x

def get_number_rows(screen,alien_height,ship_height):
    screen_rect = screen.get_rect()

    available_space_y = screen_rect.height - 3*alien_height - ship_height

    number_rows = int(available_space_y/(2*alien_height))

    return  number_rows

'''
def create_enemies1(screen,aliens,ship):             #这是测试用的代码，正式游戏中不会使用。

    alien = Alien(screen)

    alien_width = alien.rect.width

    alien_number = get_number_aliens_x(screen,alien_width)

    for alien_numbers in range(alien_number):

        alien = Alien(screen)

        alien.x = alien_width + 2 * alien_width * alien_numbers

        alien.rect.x = alien.x

        aliens.add(alien)
        
'''

def update_aliens(aliens,screen,settings,ship,stats,bullets,scoreboard):
    check_fleet_edges(aliens,screen,settings)
    aliens.update(settings)

    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(stats,screen,ship,aliens,bullets,scoreboard)

    check_alien_bottom(stats,screen,ship,aliens,bullets,scoreboard)

def check_fleet_edges(aliens,screen,settings):
    for alien in aliens.sprites():
        if alien.check_edges(screen):
            change_fleet_direction(aliens,settings)
            break

def change_fleet_direction(aliens,settings):
    for alien in aliens.sprites():
        alien.rect.y += settings.fleet_drop_speed
    settings.alien_direction *= -1

def check_edges(self,screen):
    screen_rect = screen.get_rect()

    if self.rect.right >= screen_rect.right:
        return True

    elif self.rect.left <= 0:
        return True

def check_bullet_alien_collisions(screen,ship,aliens,bullets,ai_settings,stats,scoreboard):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points
            scoreboard.prep_score()

        check_high_score(stats,scoreboard)

    if len(aliens) == 0:

        ai_settings.increase_speed()
        stats.level += 1
        scoreboard.prep_level()

        create_enemies(screen, aliens, ship)

def ship_hit(stats,screen,ship,aliens,bullets,scoreboard):

    if stats.ship_left >0:
        stats.ship_left -= 1

        aliens.empty()
        bullets.empty()

        scoreboard.prep_ship_left()
        scoreboard.show_score()

        ship.center_ship()

        create_enemies(screen,aliens,ship)

        sleep(0.5)

    else:

        pygame.mouse.set_visible(True)

        save_high_score(stats)

        stats.game_active = False

def check_alien_bottom(stats,screen,ship,aliens,bullets,scoreboard):
    screen_rect = screen.get_rect()

    for alien in aliens.sprites():

        if alien.rect.bottom >= screen_rect.bottom:

            ship_hit(stats,screen,ship,aliens,bullets,scoreboard)

            break

def check_play_button(ai_settings,stats,play_button,mouse_x,mouse_y,ship,aliens,bullets,screen,scoreboard):

    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)

    load_high_score(stats,scoreboard)

    if button_clicked and not stats.game_active:



        ai_settings.initialize_dynamic_settings()

        pygame.mouse.set_visible(False)

        stats.reset_stats()
        stats.game_active = True

        aliens.empty()
        bullets.empty()

        screen_make_it_newer(ship,screen,bullets,aliens,play_button,stats,scoreboard)

        create_enemies(screen,aliens,ship)

        ship.center_ship()

def check_high_score(stats,scoreboard):
    if int(stats.score) > int(stats.high_score):
        stats.high_score = int(stats.score)
        scoreboard.prep_high_score()

def load_high_score(stats,scoreboard):
    filename = 'files/save/save.json'

    with open(filename,'r') as file_objects:
        stats.high_score = file_objects.read()

    scoreboard.prep_high_score()

def save_high_score(stats):
    filename = 'files/save/save.json'
    with open(filename,'w') as file_objects:
        file_objects.write(str(stats.high_score))

def change_angle(stats,ship,screen):
    if stats.angle == 0:
        stats.angle = 180
        ship.image = pygame.transform.flip(ship.image, False,True)
        screen.blit(ship.image,ship.rect)

    elif stats.angle == 180:
        stats.angle = 0
        ship.image = pygame.transform.flip(ship.image, False, True)
        screen.blit(ship.image,ship.rect)

def check_ship_allowed(stats):
    if stats.over_heated <= stats.heat_sum:
        stats.allowed = True
    elif stats.over_heated > stats.heat_sum:
        stats.allowed = False

