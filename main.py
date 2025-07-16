import pygame
import sys
import math
from constants import *
from field import Field
from player import Player
from ball import Ball

# Main entry point for the game
def main():
    
    # Initialize pygame
    pygame.init()
    
    # Create the main window/screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Penalty Shootout Simulator")
    
    # Create clock for FPS control
    clock = pygame.time.Clock()
    
    # Create field 
    field = Field()
    
    # Create player
    player = Player()
    
    # Create ball
    ball = Ball()
    
    # Main game loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if not ball.active:
                    angle, power = player.get_shot_params()
                    ball.shoot(angle,power)
                    
        player.update()
        ball.update()
            
        
        # Draw everything
        screen.fill(GREEN)
        field.draw(screen)
        player.draw(screen)
        ball.draw(screen)
        
        # Draw aiming line from the ball if the ball is not moving
                # Draw aiming line from the ball if the ball is not moving
        if not ball.active:
            aim_length = 80
            angle = player.aim_angle
            start_x = ball.x + 10  # Offset 10 pixels to the right
            start_y = ball.y
            end_x = start_x + aim_length * math.cos(math.radians(angle))
            end_y = start_y - aim_length * math.sin(math.radians(angle))
            pygame.draw.line(screen, RED, (start_x, start_y), (end_x, end_y), 3)

        pygame.display.flip()
        clock.tick(FPS)
        
    # Clean up
    pygame.quit()
    sys.exit()
    

if __name__ == "__main__":
    main()
    