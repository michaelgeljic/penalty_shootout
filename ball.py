# Ball physics and movement
# - Store ball position and velocity
# - Handle ball movement with physics (gravity, trajectory)
# - Apply friction and bouncing
# - Handle being "shot" with initial velocity
# - Reset ball position for new shots
# - Draw the ball
# - Detect when ball is out of bounds or stopped

import pygame
import math
from constants import *

class Ball:
    def __init__(self):
        self.reset()
        
    def reset(self):
        self.x = PENALTY_X
        self.y = PENALTY_Y
        self.radius = 10
        self.speed = 0
        self.angle = 0
        self.active = False # is ball moving
        
    def shoot(self, angle, power):
        self.angle = angle
        self.speed = power
        self.active = True
        
    def update(self):
        if self.active: 
            # Move ball in direction of angle
            self.x += self.speed * math.cos(math.radians(self.angle))
            self.y -= self.speed * math.sin(math.radians(self.angle))
            # Slow down ball (friction)
            self.speed *= 0.98
            if self.speed < 1:
                self.active = False
                
    def draw(self, screen):
        pygame.draw.circle(screen, YELLOW, (int(self.x), int(self.y)),self.radius)