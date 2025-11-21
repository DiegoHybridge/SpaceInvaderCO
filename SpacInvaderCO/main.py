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

def main():
    screen_w, screen_h = 1920, 1080
    game = Game(screen_width=screen_w, screen_height=screen_h, image=BULLET_IMAGE)
    game.bullets = 3  # mostrar balas en HUD
    # Crear enemigos (usa el método create de una instancia)
    spawner = Enemy()
    enemies = spawner.create(5)

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

        # dibujar
        game.window.fill((0, 0, 0))
        for e in enemies:
            e.draw(game.window)
        game.drawHud()
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()