from GameObjs.GameObjs import GameObjs
import os
import pygame


class Chest(GameObjs):
    def __init__(self, position):
        super().__init__(position=position, name="chest")
        
        self.chest_dir = "Treasure Hunters/Palm Tree Island/Sprites/Objects/Chest"
        self.chest = os.listdir(self.chest_dir)
        self.opened_chest = self.chest[10:]
        self.closed_chest = self.chest[:10]
        
        
        self.is_opened = False
        self.open = False
        self.colliding = False
        self.anim_start = 0

        self.image = pygame.image.load(self.chest_dir + "/" + self.closed_chest[self.anim_start])
        self.rect = self.image.get_rect()
        self.chest_items = ["Gold", "Apple", "Sword"]

    def action(self):
        if self.open:
            if self.anim_start >= len(self.opened_chest)-1:
                self.open = False
                self.anim_start = 0
            
            self.anim_start += 1
    
    def player_collision(self, player):
        self.colliding = False
        if player.position.x + player.rect.w > self.position.x and player.position.x < self.position.x + self.rect.w\
        and player.position.y+player.rect.h > self.position.y and player.position.y:
            self.colliding = True
        
        


    def update(self, player):

        self.player_collision(player)
        self.action()
        
        
        

        
    
    def draw(self, window: pygame.surface.Surface):
        
        self.image = pygame.image.load(self.chest_dir + "/" + self.closed_chest[self.anim_start])
        window.blit(self.image, self.position.as_tup())
