# Player (shooter) class
# - Handle player input for aimimg (arrow keys)
# - Track aim direction and angle
# - Handle shooting input (spacebar)
# - Calculate shot power and direction
# - Draw the plater character
# - Draw aiming indicator/line
# - Pass shot parameters to ball when shooting

import pygame
import math
from constants import *

class Player:
    def __init__(self):
        self.x = PENALTY_X - 150
        self.y = PENALTY_Y
        
        self.width = 20
        self.height = 30
        
        self.aim_angle = 0 # Angle in degrees, (0 = straight, + = up, - = down)
        self.max_angle = 45 # Max up or down
        
        
    def update(self):
        # Handle aiming input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.aim_angle < self.max_angle:
            self.aim_angle += 2
        elif keys[pygame.K_DOWN] and self.aim_angle > -self.max_angle:
            self.aim_angle -= 2
        
        
    def get_shot_params(self):
        return self.aim_angle, 18
            
    def draw(self, screen):
        pygame.draw.rect(screen, BLUE, (self.x - self.width//2, self.y - self.height//2, self.width, self.height))
        
    
        
        