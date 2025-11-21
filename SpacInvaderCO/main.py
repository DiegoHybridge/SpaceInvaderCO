import os
import sys
import pygame

# Inicializar pygame antes de importar módulos que cargan imágenes al import
pygame.init()

current_dir = os.path.dirname(os.path.abspath(__file__))

# Cargar imagen de bala usando current_dir
BULLET_IMAGE = pygame.image.load(os.path.join(current_dir, 'assets', 'bullet.png'))

from game import Game
from enemy import Enemy
from drawing import Drawing

def main():
    screen_w, screen_h = 1920, 1080
    game = Game(screen_width=screen_w, screen_height=screen_h, image=BULLET_IMAGE)
    game.bullets = 3  # mostrar balas en HUD
    
    # Crear instancia de Drawing
    drawer = Drawing(game.window)
    
    # Crear enemigos (usa el método create de una instancia)
    spawner = Enemy()
    enemies = spawner.create(40)

    running = True
    while running:
        game.clock.tick(game.fps)
        # eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # actualizar estado
        for e in enemies:
            e.move()
        game.contador += 1

        # dibujar usando la clase Drawing
        drawer.drawing(game, None, enemies, game.fps)

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()