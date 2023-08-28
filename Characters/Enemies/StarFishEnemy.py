from Characters.Enemies.EnemyBase import Enemy
from Movement.vector2d import Vector
import pygame
import math as m
class StarFishEnemy(Enemy):
    def __init__(self, position):
        super().__init__(Enemy="Pink Star", position = position)
        self.offset = 24
        self.hitbox = pygame.rect.Rect(self.position.x, self.position.y, self.rect.w, self.rect.h)
        self.done_attacking = False
        self.walk_speed = 6

    def detect_player(self, player, window):
        translate = 40
        width_translated = translate*6
        detect_rect = pygame.rect.Rect(self.position.x-width_translated//2, self.position.y-translate, self.rect.w+width_translated, self.rect.h+translate)
        
        self.can_attack = False
        
        if player.position.x + player.rect.w > detect_rect.x and player.position.x+player.rect.w < detect_rect.x+detect_rect.w or \
        player.position.x > detect_rect.x and player.position.x < detect_rect.x+detect_rect.w:
            self.can_attack = True
        pygame.draw.rect(window, (255, 255, 255), detect_rect, 1)

    def draw_hitbox(self, window):
        pygame.draw.rect(window, (255, 255, 255), self.hitbox, 2)
        
    def spin_attack(self, player):
        # self.gravity = Vector(0, 0)
        
        # self.position.y -= 25
            
        # print(self.position, player.position)
        # print(m.degrees(m.atan2(self.position.x, self.position.y)))
        # if self.position.y < 450:
        if self.is_touching_ground() == False:
            self.position += Vector(-50, -15)

    def basic_attack(self, player):
        if player.position.x + player.rect.w > self.hitbox.x and player.position.x+player.rect.w < self.hitbox.x+self.hitbox.w and player.position.y +player.rect.h > self.hitbox.y and player.position.y < self.hitbox.y + self.hitbox.h:
                player.take_damage()

        
    def check_if_player_is_hit(self, player):
        self.hitbox = pygame.rect.Rect(self.position.x, self.position.y+self.offset, self.rect.w, self.rect.h)
        if self.can_attack and self.anim_start == 2:
            self.basic_attack(player)