from Movement.vector2d import Vector
import pygame
import os
import random
from Utils.Direction import Direction


class Player(pygame.sprite.Sprite):
    def __init__(self): 
        pygame.sprite.Sprite.__init__(self)
        self.position = Vector(50, 250)
        self.velocity = Vector(0, 0)
        self.gravity = Vector(0, 4)
        self.has_sword = False
        self.health = 5
        
        self.without_sword_path = ["Treasure Hunters/Captain Clown Nose/Sprites/Captain Clown Nose/Captain Clown Nose without Sword/01-Idle",
                          "Treasure Hunters/Captain Clown Nose/Sprites/Captain Clown Nose/Captain Clown Nose without Sword/02-Run",
                          "Treasure Hunters/Captain Clown Nose/Sprites/Captain Clown Nose/Captain Clown Nose without Sword/03-Jump",
                          "Treasure Hunters/Captain Clown Nose/Sprites/Captain Clown Nose/Captain Clown Nose without Sword/04-Fall",
                          "Treasure Hunters/Captain Clown Nose/Sprites/Captain Clown Nose/Captain Clown Nose without Sword/05-Ground",
                          "Treasure Hunters/Captain Clown Nose/Sprites/Captain Clown Nose/Captain Clown Nose without Sword/06-Hit",
                          "Treasure Hunters/Captain Clown Nose/Sprites/Captain Clown Nose/Captain Clown Nose without Sword/07-Dead Hit",
                          "Treasure Hunters/Captain Clown Nose/Sprites/Captain Clown Nose/Captain Clown Nose without Sword/08-Dead Ground"]
        
        self.sword_path = ["Treasure Hunters/Captain Clown Nose/Sprites/Captain Clown Nose/Captain Clown Nose with Sword/09-Idle Sword",
                          "Treasure Hunters/Captain Clown Nose/Sprites/Captain Clown Nose/Captain Clown Nose with Sword/10-Run Sword",
                          "Treasure Hunters/Captain Clown Nose/Sprites/Captain Clown Nose/Captain Clown Nose with Sword/11-Jump Sword",
                          "Treasure Hunters/Captain Clown Nose/Sprites/Captain Clown Nose/Captain Clown Nose with Sword/12-Fall Sword",
                          "Treasure Hunters/Captain Clown Nose/Sprites/Captain Clown Nose/Captain Clown Nose with Sword/13-Ground Sword",
                          "Treasure Hunters/Captain Clown Nose/Sprites/Captain Clown Nose/Captain Clown Nose with Sword/14-Hit Sword",
                          "Treasure Hunters/Captain Clown Nose/Sprites/Captain Clown Nose/Captain Clown Nose with Sword/15-Attack 1",
                          "Treasure Hunters/Captain Clown Nose/Sprites/Captain Clown Nose/Captain Clown Nose with Sword/16-Attack 2",
                          "Treasure Hunters/Captain Clown Nose/Sprites/Captain Clown Nose/Captain Clown Nose with Sword/17-Attack 3"]
        self.do_attack = False
        self.damage_enemy = False
        self.is_hit = False
        
        self.direction = Direction.RIGHT

        self.current_anim = 0
        self.anim_start = 0
        self.current_path = self.without_sword_path

        self.animation = os.listdir(self.current_path[self.current_anim])
        self.anim_end = len(self.animation)
        self.img = self.animation[0]
        self.image = pygame.image.load(self.current_path[self.current_anim]+"/"+self.img)
        self.rect = self.image.get_rect()
        self.player_hitbox = pygame.rect.Rect(self.position.x+24, self.position.y+16, 16, 32)
        self.sword_hitbox_rect = pygame.rect.Rect((self.position.x+self.rect.w) - 15, (self.position.y+self.rect.h//2)+5, 10, 5)

        self.max_peak = 10

        self.move_l = False
        self.move_r = False
        
    def apply_gravity(self):
        if self.velocity.y > 9:
            self.velocity.y = 9

        self.velocity += self.gravity
        self.player_hitbox.y += self.velocity.y
        self.player_hitbox.x += self.velocity.x  
        self.position += self.velocity
    
    def attack(self):
        self.anim_start = 0
        self.do_attack = True

    def idle(self):
        self.current_anim = 0
        self.animation = os.listdir(self.current_path[self.current_anim])
        self.image = pygame.image.load(self.current_path[self.current_anim]+"/"+self.animation[self.anim_start])
        self.anim_end = len(self.animation)   

    def jump(self):
        self.velocity.y = -20

        
    
    def attack_animation(self):
        self.current_anim = random.randint(6, 8)
        self.animation = os.listdir(self.current_path[self.current_anim])
        self.anim_end = len(self.animation)
        self.image = pygame.image.load(self.current_path[self.current_anim]+"/"+self.animation[self.anim_start])
        self.damage_enemy = False
        if self.anim_start == 1:
            self.damage_enemy = True
        
        if self.anim_start >= self.anim_end-1:
            self.do_attack = False
            self.idle()

    def hurt_animation(self):
        self.current_anim = 5
        self.animation = os.listdir(self.current_path[self.current_anim])
        self.anim_end = len(self.animation)
        self.image = pygame.image.load(self.current_path[self.current_anim]+"/"+self.animation[self.anim_start])

        if self.anim_start >= self.anim_end-1:
            self.is_hit = False
            self.idle()

    def movement(self):
        keys = pygame.key.get_pressed()

        self.move_r = False
        self.move_l = False

        if keys[pygame.K_a]: 
            # self.velocity.x = -10
            self.move_l = True
            self.move_r = False
            
        if keys[pygame.K_d]: 
            # self.velocity.x = 10
            self.move_r = True
            self.move_l = False

    def collision_update(self, platform_rect):
        if self.player_hitbox.y+self.player_hitbox.h > platform_rect.y and self.player_hitbox.x + self.player_hitbox.w > platform_rect.x and self.player_hitbox.x < platform_rect.x+platform_rect.w and self.player_hitbox.y<platform_rect.y+platform_rect.h:
            
            self.gravity = Vector(0, 0)
            self.position.y = platform_rect.y - self.rect.h - 2
        else:
            self.gravity = Vector(0, 3)

        # if self.position.x < platform_rect.x + platform_rect.w or self.position.x + self.rect.w > platform_rect.x:
        #     self.velocity = Vector(0,0)


    def update(self):
        self.apply_gravity()
        self.movement()
        self.sword_hitbox_rect = pygame.rect.Rect((self.position.x+self.rect.w) - 15, (self.position.y+self.rect.h//2)+2, 10, 5)

        
        self.velocity.x = 0
        # keys = pygame.key.get_pressed()

        if self.anim_start > self.anim_end-1:
            self.anim_start = 0

        self.idle()

        if self.do_attack:
            self.attack_animation()
        
        elif self.is_hit:
            self.hurt_animation()

        elif self.move_l: 
            self.direction = Direction.LEFT
            self.velocity.x = -10
            
            self.current_anim = 1
            self.animation = os.listdir(self.current_path[self.current_anim])
            
            self.image = pygame.image.load(self.current_path[self.current_anim]+"/"+self.animation[self.anim_start])
            # self.image = pygame.transform.flip(self.image, True, False)
            
        elif self.move_r:
            self.direction = Direction.RIGHT 
            self.velocity.x = 10
            self.current_anim = 1
            self.animation = os.listdir(self.current_path[self.current_anim])
            
            self.image = pygame.image.load(self.current_path[self.current_anim]+"/"+self.animation[self.anim_start])  

        # if keys[pygame.K_n]:
        #     self.has_sword = not self.has_sword

    def take_damage(self):
        self.is_hit = True
        self.anim_start = 0
        self.health -= 1

    def draw(self, window:pygame.surface.Surface):
        self.player_hitbox = pygame.rect.Rect(self.position.x+24, self.position.y, 16, 32)


        if self.has_sword:
            self.current_path = self.sword_path            
        else:
            self.current_path = self.without_sword_path

        self.update()
        # self.image = pygame.image.load(self.idle_path[self.current_anim]+"/"+self.animation[self.anim_start])
        # self.image = pygame.image.load(self.current_path[self.current_anim]+"/"+self.animation[self.anim_start])
        if self.direction == Direction.LEFT:
            self.sword_hitbox_rect.x = self.position.x
            self.image = pygame.transform.flip(self.image, True, False)
        self.anim_start+=1
        
        window.blit(self.image, (self.position.x, self.position.y))
        pygame.draw.rect(window, (255, 255, 255), (self.position.x, self.position.y, self.rect.w, self.rect.h), 2)
        # pygame.draw.rect(window, (255, 255, 0), self.player_hitbox)