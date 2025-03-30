# ghost.py
import pygame
from settings import *
from algorithm import *

class Ghost:
    def __init__(self, x, y, algorithm, color):
        self.x = x
        self.y = y
        self.initial_x = x
        self.initial_y = y
        self.algorithm = algorithm
        self.color = color
        self.path = []
        self.path_index = 0
        self.image = pygame.image.load(GHOST_IMAGES[algorithm])
        self.image = pygame.transform.scale(self.image, (GRID_SIZE, GRID_SIZE))
        self.last_move_time = pygame.time.get_ticks()  # Lấy thời gian khởi tạo (ms)
        self.move_delay = 300  # Thời gian delay giữa các bước di chuyển (ms), ví dụ 300ms = 0.3 giây
        self.actual_path = []
        self.visited_positions = []  # Lưu tất cả các vị trí đã đi qua
        self.show_path = False
        
    def find_path(self, maze, pacman_pos):
        start = (int(self.y), int(self.x))
        end = (int(pacman_pos[1]), int(pacman_pos[0]))
        self.path = astar(maze, start, end)
        self.path_index = 0
            
    def move(self):
        if self.path and self.path_index < len(self.path):
            current_time = pygame.time.get_ticks()  # Lấy thời gian hiện tại (ms)
            # Kiểm tra xem đã đủ thời gian để di chuyển chưa
            if current_time - self.last_move_time >= self.move_delay:
                next_pos = self.path[self.path_index]
                self.x = next_pos[1]
                self.y = next_pos[0]
                self.actual_path.append(next_pos)
                self.path_index += 1
                self.last_move_time = current_time  # Cập nhật thời gian di chuyển cuối cùng
                
    def draw(self, win, offset_x=0, offset_y=0):
        win.blit(self.image, (self.x * GRID_SIZE + offset_x, self.y * GRID_SIZE + offset_y))