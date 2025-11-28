import pygame
import sys
import os
from ship import ShipClass
from bullet import Bullet
class Player(ShipClass):
    """
    Clase que representa al jugador en el juego.
    Hereda de ShipClass y agrega funcionalidad específica del jugador.
    """
    
    def __init__(self, x, y, health, ship_img, bullet_img):
        """
        Constructor de la clase Player.
        
        Args:
            x (int): Posición horizontal inicial del jugador
            y (int): Posición vertical inicial del jugador
            health (int): Salud/vida del jugador
            ship_img (pygame.Surface): Imagen de la nave del jugador
            bullet_img (pygame.Surface): Imagen de los proyectiles del jugador
        """
        
        # Llamar al constructor de la clase padre (ShipClass)
        # Esto inicializa: x, y, salud_de_vida, ship_img, bullet_img, etc.
        super().__init__(x, y, health)
        
        # Asignar las imágenes pasadas como parámetros
        self.ship_img = ship_img
        self.bullet_img = bullet_img
        
        # Velocidad de desplazamiento del jugador
        self.player_speed = 5  # Píxeles por frame
        
        # Inicializar velocidades de movimiento del jugador usando player_speed
        self.x_speed = self.player_speed  # Velocidad horizontal (positivo = derecha)
        self.y_speed = self.player_speed  # Velocidad vertical (positivo = abajo)
        
        # Crear máscara de colisión basada en la imagen de la nave
        # Esto permite detectar colisiones más precisas (pixel-perfect)
        self.mask = pygame.mask.from_surface(self.ship_img)
        
        # Configuración de proyectiles del jugador
        self.max_bullets = 3  # Máximo de balas activas simultáneamente
        self.bullet_speed = 10  # Velocidad de los proyectiles (píxeles por frame)
        self.fired_bullets = []  # Lista que almacena las balas activas
        
        # Contadores para manejar cooldown y creación de balas
        self.bullet_cooldown_counter = 0  # Contador para el tiempo de espera entre disparos
        self.cool_down = 10  # Frames de espera entre disparos (10 frames = ~167ms a 60 FPS)
        self.creation_cooldown_counter = 0  # Contador auxiliar para creación de proyectiles
    def move(self, HEIGHT, WIDTH):
        keys = pygame.key.get_pressed()
        # Movimiento vertical (W/S o flechas arriba/abajo)
        if (keys[pygame.K_w] or keys[pygame.K_UP]) and self.y > 0:
            self.y -= self.y_speed
        if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and self.y < HEIGHT - self.ship_img.get_height() - 60:
            self.y += self.y_speed
        # Movimiento horizontal (A/D o flechas izquierda/derecha)
        if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and self.x < WIDTH - self.ship_img.get_width():
            self.x += self.x_speed
        if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and self.x > 0:
            self.x -= self.x_speed
    def create_bullets(self):
        if (len(self.bullets) < self.max_amount_bullets) and (self.creation_cooldown_counter == 0):
            bullet = Bullet(self.x, self.y, self.bullet_img)
            self.bullets.append(bullet)
            self.creation_cooldown_counter = 1
        for bullet in self.fired_bullets:
            if bullet.y <= -40:
                self.fired_bullets.pop(0)
    def cooldown(self):
        if self.bullet_cooldown_counter >= 20:
            self.bullet_cooldown_counter = 0
        elif self.bullet_cooldown_counter > 0:
            self.bullet_cooldown_counter += 1

        if self.creation_cooldown_counter >= self.cool_down:
            self.creation_cooldown_counter = 0
        elif self.creation_cooldown_counter > 0:
            self.creation_cooldown_counter += 1


