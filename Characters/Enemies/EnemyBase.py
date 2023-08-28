import pygame
import os
from Movement.vector2d import Vector
from Utils.Direction import Direction

class Enemy(pygame.sprite.Sprite):
    def __init__(self, Enemy="Crabby", position=None):
        pygame.sprite.Sprite.__init__(self)

        self.enemy = Enemy
        self.position = Vector(coordinates=position)
        self.velocity = Vector(0, 0)
        self.gravity = Vector(0, 4)
        self.health = 3
        self.is_hit = False
        self.can_attack = False
        self.touching_ground = False
        self.walk_speed = 2

        self.enemy_path = [f"Treasure Hunters/The Crusty Crew/Sprites/{Enemy}/01-Idle",
                          f"Treasure Hunters/The Crusty Crew/Sprites/{Enemy}/02-Run",
                          f"Treasure Hunters/The Crusty Crew/Sprites/{Enemy}/03-Jump",
                          f"Treasure Hunters/The Crusty Crew/Sprites/{Enemy}/04-Fall",
                          f"Treasure Hunters/The Crusty Crew/Sprites/{Enemy}/05-Ground",
                          f"Treasure Hunters/The Crusty Crew/Sprites/{Enemy}/06-Anticipation",
                          f"Treasure Hunters/The Crusty Crew/Sprites/{Enemy}/07-Attack",
                          f"Treasure Hunters/The Crusty Crew/Sprites/{Enemy}/08-Hit",
                          f"Treasure Hunters/The Crusty Crew/Sprites/{Enemy}/09-Dead Hit",
                          f"Treasure Hunters/The Crusty Crew/Sprites/{Enemy}/10-Dead Ground",
                          f"Treasure Hunters/The Crusty Crew/Sprites/{Enemy}/11-Attack Effect"]
        self.direction = Direction.RIGHT
        self.current_path_index = 0
        self.attack_timer = 0
        self.start_timer = False
        self.current_animation = os.listdir(self.enemy_path[self.current_path_index])
        self.anim_start = 0
        self.anim_end = len(self.current_animation)
        self.animation = self.current_animation
        self.can_move = False

        self.max_movement_distance = 30

        self.image = pygame.image.load(f"{self.enemy_path[self.current_path_index]}/{self.animation[self.anim_start]}")
        self.rect = self.image.get_rect()
        
    def reset_animation_timer(self):
        if self.anim_start > self.anim_end-1:
            self.anim_start = 0

    def idle(self):
        self.current_path_index = 0
        self.current_animation = os.listdir(self.enemy_path[self.current_path_index])
        self.anim_end = len(self.current_animation)
        self.image = pygame.image.load(f"{self.enemy_path[self.current_path_index]}/{self.animation[self.anim_start]}")
    
    def detect_player(self, player, window):
        translate = 40
        detect_rect = pygame.rect.Rect(self.position.x-translate, self.position.y-translate, self.rect.w+translate*2, self.rect.h+translate)
        
        self.can_attack = False
        
        if player.position.x + player.rect.w > detect_rect.x and player.position.x+player.rect.w < detect_rect.x+detect_rect.w or \
        player.position.x > detect_rect.x and player.position.x < detect_rect.x+detect_rect.w:
            self.can_attack = True
            self.can_move = False

    def attack_animation(self):
        self.current_path_index = 6
        self.current_animation = os.listdir(self.enemy_path[self.current_path_index])
        self.anim_end = len(self.current_animation)
        self.reset_animation_timer()
        self.image = pygame.image.load(f"{self.enemy_path[self.current_path_index]}/{self.current_animation[self.anim_start]}")
        
        if self.anim_start >= self.anim_end-1:
            self.can_attack = False
            self.start_timer = True
            self.can_move = True

    def walking_animation(self):
        self.current_path_index = 1
        self.current_animation = os.listdir(self.enemy_path[self.current_path_index])
        self.anim_end = len(self.current_animation)
        self.reset_animation_timer()
        self.image = pygame.image.load(f"{self.enemy_path[self.current_path_index]}/{self.current_animation[self.anim_start]}")
        


    def apply_gravity(self):
        if self.velocity.y > 9:
            self.velocity.y = 9
        self.velocity += self.gravity  
        self.position += self.velocity

    def is_touching_ground(self):
        return self.touching_ground

    def basic_movement(self):
        self.walking_animation()
        if self.position.x > 970:
                self.direction = Direction.LEFT
        if self.position.x < 750:
                self.direction = Direction.RIGHT
        if self.can_move:
            
            
            if self.direction == Direction.RIGHT:
                self.velocity.x = self.walk_speed

            if self.direction == Direction.LEFT:
                self.velocity.x = -self.walk_speed
            
            
            
    
                

    def collision_update(self, platform_rect:pygame.rect.Rect):
        # if self.position.y+self.velocity.y+self.rect.h -2 > platform_rect.top:
        if self.position.y+self.velocity.y+self.rect.h> platform_rect.y and self.position.x + self.rect.w > platform_rect.x and self.position.x < platform_rect.x+platform_rect.w and self.position.y<platform_rect.y+platform_rect.h:
            
            
            self.gravity = Vector(0, 0)
            self.position.y = platform_rect.y - self.rect.h + 3
            self.touching_ground = True
            self.can_move=True
        else:
            self.gravity = Vector(0, 3)
            self.touching_ground = False

    def hit_animation(self):
        
        self.current_path_index = 7
        self.current_animation = os.listdir(self.enemy_path[self.current_path_index])
        self.anim_end = len(self.current_animation)
        self.image = pygame.image.load(f"{self.enemy_path[self.current_path_index]}/{self.current_animation[self.anim_start]}")
        if self.anim_start >= self.anim_end - 1:
            self.is_hit = False

    def check_if_hit(self, player):
        if player.sword_hitbox_rect.x + player.sword_hitbox_rect.w >= self.position.x and player.sword_hitbox_rect.x + player.sword_hitbox_rect.w <= self.position.x+self.rect.w and player.damage_enemy:
            self.anim_start = 0
            self.is_hit = True
            self.health -= 1

    def change_direction(self, player):
        if self.can_attack:
            if player.position.x+player.rect.w//2 > self.position.x+self.rect.w//2:
                self.direction = Direction.RIGHT
            else:
                self.direction = Direction.LEFT
    
    def attack_timer_toggle(self):
        if self.start_timer:
            self.attack_timer += 1

        if self.attack_timer == 45:
            self.attack_timer = 0
            self.start_timer = False
            self.anim_start = 0

    def update(self):
        
        self.apply_gravity()

        

        self.reset_animation_timer()

        self.idle()

        self.basic_movement()
        
        self.attack_timer_toggle()
        

        if self.can_attack and self.start_timer == False\
            and self.anim_start == 0:
                self.attack_animation()
               
        # print(f"{self.attack_timer, self.start_timer, self.can_attack}")
        # print(self.anim_start)
        if self.is_hit:
            self.hit_animation()

        

    def draw(self, window: pygame.surface.Surface):
        
        

        self.anim_start+=1
        
        if self.direction == Direction.RIGHT:
            self.image = pygame.transform.flip(self.image, True, False)
       
        
        window.blit(self.image, (self.position.x, self.position.y))
        # pygame.draw.rect(window, (255, 255, 255), (self.position.x, self.position.y, self.rect.w, self.rect.h), 1)
