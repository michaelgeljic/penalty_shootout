import pygame
import sys
from constants import *
from field import Field

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
    
    # Main game loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
        
        # Fill screen with green
        screen.fill(GREEN)
        
        # Draw field
        field.draw(screen)
        
        # Update display
        pygame.display.flip()
        
        # Control frame rate using FPS constant
        clock.tick(FPS)
        
    # Clean up
    pygame.quit()
    sys.exit()
    

if __name__ == "__main__":
    main()
    