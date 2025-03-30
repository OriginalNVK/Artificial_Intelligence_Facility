import pygame
from settings import *

class Button:
    def __init__(self, x, y, width, height, text, color, hover_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.is_hovered = False
        
    def draw(self, win):
        color = self.hover_color if self.is_hovered else self.color
        pygame.draw.rect(win, color, self.rect, border_radius=10)
        pygame.draw.rect(win, WHITE, self.rect, 2, border_radius=10)
        
        text_surface = BUTTON_FONT.render(self.text, True, WHITE)
        text_rect = text_surface.get_rect(center=self.rect.center)
        win.blit(text_surface, text_rect)
        
    def check_hover(self, pos):
        self.is_hovered = self.rect.collidepoint(pos)
        return self.is_hovered
        
    def is_clicked(self, pos, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            return self.rect.collidepoint(pos)
        return False