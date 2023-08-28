import pygame
from enum import Enum
class EntityEvents(Enum):
    ATTACK_EVENT = pygame.event.custom_type()
    