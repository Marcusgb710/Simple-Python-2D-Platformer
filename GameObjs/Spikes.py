from GameObjs.GameObjs import GameObjs
import os
import pygame


class Spikes(GameObjs):
    def __init__(self, position):
        super().__init__(position=position, name="spikes")
        self.colliding = False
        self.spike_dir = "Treasure Hunters/Palm Tree Island/Sprites/Objects/Spikes/Spikes.png"
        self.image = pygame.image.load(self.spike_dir)
        self.rect = self.image.get_rect()
        self.hurt_timer = 0
        self.timer_len = 5

    def player_collision(self, player):
        self.colliding = False
        if player.player_hitbox.x + player.player_hitbox.w > self.position.x and player.player_hitbox.x < self.position.x + self.rect.w\
        and player.player_hitbox.y+player.player_hitbox.h > self.position.y and player.player_hitbox.y:
            self.colliding = True

    def reset_timer(self):
        if self.hurt_timer >= self.timer_len:
            self.hurt_timer = 0

    def damage_player(self, player):
        if self.colliding and self.hurt_timer == 1:
            player.take_damage()

    def update(self, player):
        self.reset_timer()
        self.player_collision(player)
        self.damage_player(player)


    def draw(self, window):
        self.hurt_timer += 1
        window.blit(self.image, self.position.as_tup())