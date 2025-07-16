# Field and goal rendering
# - Draw the field background
# - Draw goal posts and crossbar
# - Draw penalty spot
# - Draw any field markings or boundaries
# - Maybe handle goal area collision detection
# - Store goal dimensions and position

import pygame
from constants import *

class Field:
    def __init__(self):
        self.goal_color = WHITE
        
        
    def draw(self, screen):
        # draw posts
        pygame.draw.line(screen,WHITE, (GOAL_X, GOAL_Y), (GOAL_X, GOAL_Y + GOAL_HEIGHT), 3)
        pygame.draw.line(screen,WHITE, (GOAL_X + GOAL_WIDTH, GOAL_Y), (GOAL_X + GOAL_WIDTH, GOAL_Y+GOAL_HEIGHT), 6)
        pygame.draw.line(screen,WHITE, (GOAL_X, GOAL_Y), (GOAL_X  + GOAL_WIDTH, GOAL_Y), 3)
        
        # draw penalty spot
        pygame.draw.circle(screen, WHITE, (PENALTY_X,PENALTY_Y), 5)
        
        
                