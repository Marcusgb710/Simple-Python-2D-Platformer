from Characters.Enemies.EnemyBase import Enemy
import pygame

class CrabEnemy(Enemy):
    def __init__(self, position):
        super().__init__(Enemy="Crabby", position=position)
        self.offset = 5
        self.left_rect = pygame.rect.Rect(self.position.x, (self.position.y+self.rect.h//2)+self.offset, 10, 10)
        self.right_rect = pygame.rect.Rect((self.position.x+self.rect.w)-5, (self.position.y+self.rect.h//2)+self.offset, 10, 10)
        self.hit_counter = 0
        self.right_counter = 0
        self.walk_speed = 2
    
    def draw_hitbox(self, window):
        pygame.draw.rect(window, (0, 0, 255), self.left_rect)
        pygame.draw.rect(window, (255, 0, 255), self.right_rect)
    
    def check_if_player_is_hit(self, player):
        self.left_rect = pygame.rect.Rect(self.position.x, (self.position.y+self.rect.h//2)-self.offset, 10, 10)
        self.right_rect = pygame.rect.Rect((self.position.x+self.rect.w)-5, (self.position.y+self.rect.h//2)-self.offset, 10, 10)
        
        if self.can_attack and self.anim_start == 1:
            if player.player_hitbox.x +player.player_hitbox.w > self.left_rect.x and player.player_hitbox.x< self.left_rect.x + self.left_rect.w and player.player_hitbox.y + player.player_hitbox.h > self.left_rect.y and player.player_hitbox.y < self.left_rect.y+self.left_rect.h:
                player.take_damage()
            if player.player_hitbox.x < self.right_rect.x + self.right_rect.w and player.player_hitbox.x + player.player_hitbox.w> self.right_rect.x and player.player_hitbox.y + player.player_hitbox.h > self.right_rect.y and player.player_hitbox.y < self.right_rect.y+self.right_rect.h:
                player.take_damage()