import pygame
from menu import Menu
from game import Game
from settings import *

def main():
    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pacman Pathfinding")
    clock = pygame.time.Clock()
    
    current_screen = "MENU"
    menu = Menu(win)
    game = None
    selected_algorithm = None
    
    running = True
    while running:
        clock.tick(FRAME_RATE)  # Giữ FPS ổn định
        mouse_pos = pygame.mouse.get_pos()
            
        if current_screen == "MENU":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    
                selected_algorithm = menu.handle_events(event)
                if selected_algorithm:
                    current_screen = "GAME"
                    game = Game(win, selected_algorithm)
                    
            menu.draw()
            
        elif current_screen == "GAME":
            action = game.handle_events()
            if action == "QUIT":
                running = False
            elif action == "MENU":
                current_screen = "MENU"
                selected_algorithm = None
                game = None
            else:
                game.update()
                game.draw()
                
        pygame.display.update()
        clock.tick(60)
        
    pygame.quit()

if __name__ == "__main__":
    main()