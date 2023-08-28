from abc import ABC, abstractmethod
import pygame
import os
from Movement.vector2d import Vector


class GameObjs(pygame.sprite.Sprite, ABC):
    def __init__(self, position, name):
        pygame.sprite.Sprite.__init__(self)
        self.position = Vector(coordinates=position)
        self.name = name
    
    @abstractmethod
    def update(self):
        pass 
    
    @abstractmethod
    def draw(self):
        pass