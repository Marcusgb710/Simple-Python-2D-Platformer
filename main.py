import pygame
from random import choice
from Characters.Player import Player
from Movement.vector2d import Vector
from GameObjs.Chest import Chest
from GameObjs.Door import Door
from GameObjs.Spikes import Spikes
from Utils.game_helper_functions import create_enemies, get_world_data
from Characters.Enemies.CrabEnemy import CrabEnemy
from Characters.Enemies.SharkEnemy import SharkEnemy
from Characters.Enemies.StarFishEnemy import StarFishEnemy

pygame.init()

DIM = 1408, 704
WIN = pygame.display.set_mode((DIM))
CLOCK = pygame.time.Clock()

lvl = 1

data = get_world_data()[f"{lvl}"]



def border():
    world_border = data["borders"]#75
    
    borders = []
    y = 0
    x = 0

    for idx, i in enumerate(world_border):
        y = (idx//44)*32
        x = (idx - (44*(idx//44)))*32
        if i == 75:
            borders.append(pygame.rect.Rect(x, y, 32, 32))
    return borders

def game_objs():
    chests = data["chests"]#76
    spikes = data["spikes"]#77
    doors = data["doors"]#78
    objs = []

    y = 0
    x = 0

    for idx, i in enumerate(zip(chests, spikes, doors)):
        y = (idx//44)*32
        x = (idx - (44*(idx//44)))*32
        
        if i[0] == 76:
            
            objs.append(Chest((x, y)))
        if i[1] == 77:
            objs.append(Spikes((x, y)))
        if i[2] == 78:
            objs.append(Door((x, y-32)))
    return objs

def enemies():
    enemies_data = data["enemies"]#79
    enemies = []

    for idx, i in enumerate(enemies_data):
        y = (idx//44)*32
        x = (idx - (44*(idx//44)))*32
        if i == 79:
            enemies.append(choice([CrabEnemy((x, y-5)), SharkEnemy((x, y-5)), StarFishEnemy((x, y-5))]))

    return enemies

borders = border()            
game_obj = game_objs()            

player = Player()
platform_rect = pygame.rect.Rect(0, DIM[1]-25, DIM[0], 25)
bg = pygame.image.load("Treasure Hunters/Palm Tree Island/newpmap.png")


# enemies = [CrabEnemy(),Enemy("Fierce Tooth", Vector(870, 550)), Enemy("Pink Star", Vector(940, 550))]
# enemies=create_enemies()
_enemies=enemies()

def redraw():
    
    WIN.blit(bg, (0,0))
    
    
    if _enemies:
        for enemy in _enemies:
            for b in borders:
                enemy.collision_update(b)
            
            enemy.draw_hitbox(WIN)
            enemy.check_if_player_is_hit(player)
            enemy.draw(WIN)
            enemy.update()
            enemy.change_direction(player)
            enemy.detect_player(player, WIN)
            enemy.check_if_hit(player)
        
            if enemy.health <= 0:
                _enemies.remove(enemy)
                    
                
        
    for gobjs in game_obj:
        gobjs.draw(WIN)
        gobjs.update(player)
    
    player.draw(WIN)
        
   

    # pygame.draw.rect(WIN, (255, 255, 255), platform_rect, 1)

    pygame.display.update()

    
def quit_game(event):
    if event.type == pygame.QUIT:
        pygame.quit()

def run_main():
    
    # EVENT1 = pygame.event.Event(pygame.event.custom_type(), attr1 ="Event1")
    # pygame.event.post(EVENT1)
    while True:
        CLOCK.tick(10)

        # if not enemies:
        #     pygame.quit()
       
        redraw()
        
        for b in borders:
            player.collision_update(b)

        for event in pygame.event.get():
            quit_game(event)

            # if event == EVENT1:
            #     print("Event 1")
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.jump()
                
                if event.key == pygame.K_n:
                    player.has_sword = not player.has_sword
                
                if event.key == pygame.K_e:
                    
                    for obj in game_obj:
                        if (obj.name == "chest" or obj.name == "door")and obj.colliding:
                            obj.open = True
                        

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and player.has_sword and player.do_attack == False:
                    player.attack()

if "__main__" == __name__:
    run_main()