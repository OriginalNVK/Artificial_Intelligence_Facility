import pygame
from settings import *
from button import Button

class Menu:
    def __init__(self, win):
        self.win = win
        self.buttons = []
        self.create_buttons()
        self.ghost_images = {}
        self.load_ghost_images()
        
    def load_ghost_images(self):
        for algo, path in GHOST_IMAGES.items():
            img = pygame.image.load(path)
            img = pygame.transform.scale(img, (80, 80))
            self.ghost_images[algo] = img
            
    def create_buttons(self):
        button_width, button_height = 120, 50
        spacing = 20
        total_width = 4 * button_width + 3 * spacing
        start_x = (WIDTH - total_width) // 2
        
        # Algorithm selection buttons
        self.buttons.append(Button(start_x, 450, button_width, button_height, "BFS", BLUE, (200, 100, 150)))
        self.buttons.append(Button(start_x + button_width + spacing, 450, button_width, button_height, "DFS", PINK, (100, 200, 100)))
        self.buttons.append(Button(start_x + 2*(button_width + spacing), 450, button_width, button_height, "UCS", ORANGE, (200, 50, 50)))
        self.buttons.append(Button(start_x + 3*(button_width + spacing), 450, button_width, button_height, "A*", RED, (50, 50, 200)))
        
        # All algorithms button
        self.buttons.append(Button((WIDTH - button_width) // 2, 520, button_width, button_height, "ALL", YELLOW, (200, 200, 50)))
    
    def draw_gradient_background(self):
        # Màu gradient (có thể điều chỉnh theo ý muốn)
        top_color = (20, 20, 60)    # Màu xanh đêm đậm
        bottom_color = (80, 0, 100)  # Màu tím sẫm

        for y in range(HEIGHT):
            # Tính toán màu trung gian cho mỗi dòng
            ratio = y / HEIGHT
            r = int(top_color[0] + (bottom_color[0] - top_color[0]) * ratio)
            g = int(top_color[1] + (bottom_color[1] - top_color[1]) * ratio)
            b = int(top_color[2] + (bottom_color[2] - top_color[2]) * ratio)

            # Vẽ từng dòng với màu được tính toán
            pygame.draw.line(self.win, (r, g, b), (0, y), (WIDTH, y))
    
    def draw(self):
        self.draw_gradient_background()
        # self.win.fill(BLACK)
        
        # Draw title
        title = TITLE_FONT.render("PACMAN PATHFINDING", True, WHITE)
        subtitle = BUTTON_FONT.render("Select Algorithm", True, WHITE)
        self.win.blit(title, (WIDTH//2 - title.get_width()//2, 100))
        self.win.blit(subtitle, (WIDTH//2 - subtitle.get_width()//2, 170))
        
        # Draw ghost representations
        self.win.blit(self.ghost_images["BFS"], (WIDTH//2 - 200, 250))
        self.win.blit(self.ghost_images["DFS"], (WIDTH//2 - 80, 250))
        self.win.blit(self.ghost_images["UCS"], (WIDTH//2 + 40, 250))
        self.win.blit(self.ghost_images["A*"], (WIDTH//2 + 160, 250))
        
        # Draw buttons
        for button in self.buttons:
            button.draw(self.win)
            
    def handle_events(self, event):
        mouse_pos = pygame.mouse.get_pos()
        for button in self.buttons:
            button.check_hover(mouse_pos)
            
        for i, button in enumerate(self.buttons):
            if button.is_clicked(mouse_pos, event):
                if i == 0:
                    return "BFS"
                elif i == 1:
                    return "DFS"
                elif i == 2:
                    return "UCS"
                elif i == 3:
                    return "A*"
                elif i == 4:
                    return "ALL"
        return None