from GameObjs.GameObjs import GameObjs
import os
import pygame

class Door(GameObjs):
    def __init__(self, position):
        super().__init__(position=position, name="door")
        self.door_opening_dir = "Treasure Hunters/Pirate Ship/Sprites/Decorations/Door/Opening"
        self.door_closing_dir = "Treasure Hunters/Pirate Ship/Sprites/Decorations/Door/Closing"
        self.door_opening = os.listdir(self.door_opening_dir)
        self.door_closing = os.listdir(self.door_closing_dir)
        
        self.current_dir = self.door_opening_dir
        self.current_anim = self.door_opening

        self.is_opened = False
        self.colliding = False
        self.open = False
        self.anim_start = 0
        self.image = pygame.image.load(self.current_dir+"/"+self.current_anim[0])
        self.rect = self.image.get_rect()

    def action(self):
        
        if self.open:
            self.anim_start += 1
            if self.anim_start >= len(self.door_opening)-1:
                self.open = False
                self.is_opened = True
                self.current_dir = self.door_closing_dir
                self.current_anim = self.door_closing
                self.anim_start = 0
            
            
            
        
        if self.is_opened:
            self.anim_start += 1
            if self.anim_start >= len(self.door_closing)-1:
                self.current_dir = self.door_opening_dir
                self.current_anim = self.door_opening
                self.is_opened = False
                self.anim_start = 0

            
            
        


    def player_collision(self, player):
        self.colliding = False
        if player.position.x + player.rect.w > self.position.x and player.position.x < self.position.x + self.rect.w\
        and player.position.y+player.rect.h > self.position.y and player.position.y:
            self.colliding = True
    
    def update(self, player):

        self.player_collision(player)
        self.action()

    def draw(self, window: pygame.surface.Surface):
        
        self.image = pygame.image.load(self.current_dir+"/"+self.current_anim[self.anim_start])
        window.blit(self.image, self.position.as_tup())

        
        
        
        