from Characters.Enemies.EnemyBase import Enemy
import pygame
from Utils.Direction import Direction

class SharkEnemy(Enemy):
    def __init__(self, position):
        super().__init__(Enemy="Fierce Tooth", position = position)
        self.offset = 10
        self.hit_counter = 0
        self.bite_rect = pygame.rect.Rect(self.position.x, (self.position.y+self.offset), 15, 5)
        self.walk_speed = 4

    def draw_hitbox(self, window):
        pygame.draw.rect(window, (255, 0, 0), self.bite_rect)
    
    def check_if_player_is_hit(self, player):
        if self.direction == Direction.RIGHT:
            self.bite_rect = pygame.rect.Rect(self.position.x+30, (self.position.y+self.offset), 15, 5)
        else:    
            self.bite_rect = pygame.rect.Rect(self.position.x - 13, (self.position.y+self.offset), 15, 5)
        if self.can_attack and self.anim_start == 1:
            if player.player_hitbox.x + player.player_hitbox.w > self.bite_rect.x and player.player_hitbox.x < self.bite_rect.x+self.bite_rect.w and player.player_hitbox.y+player.player_hitbox.h > self.bite_rect.y and player.player_hitbox.y < self.bite_rect.y + self.bite_rect.h:
                player.take_damage()