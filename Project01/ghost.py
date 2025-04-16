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
        # Sử dụng thuật toán tương ứng với button đã chọn

        # Trường hợp "ALL"
        # if self.algorithm == "ALL":
        #     self.path = {
        #         "BFS": bfs(maze, start, end),
        #         "DFS": dfs(maze, start, end),
        #         "UCS": ucs(maze, start, end),
        #         "A*": astar(maze, start, end)
        #     }
        # else:
        if self.algorithm == "BFS":
            self.path = bfs(maze, start, end)
        elif self.algorithm == "DFS":
            self.path = dfs(maze, start, end)
        elif self.algorithm == "UCS":
            self.path = ucs(maze, start, end)
        elif self.algorithm == "A*":
            self.path = astar(maze, start, end)

        self.path_index = 0
            
    def move(self):
        # if self.algorithm == "ALL":
        # # Duyệt qua từng thuật toán và cập nhật vị trí riêng biệt
        #     for algo, path in self.path.items():
        #         if path and self.path_index < len(path):
        #             current_time = pygame.time.get_ticks()  # Lấy thời gian hiện tại (ms)
        #             # Kiểm tra xem đã đủ thời gian để di chuyển chưa
        #             if current_time - self.last_move_time >= self.move_delay:
        #                 next_pos = path[self.path_index]
        #                 if algo == "BFS":
        #                     self.x_bfs, self.y_bfs = next_pos[1], next_pos[0]
        #                 elif algo == "DFS":
        #                     self.x_dfs, self.y_dfs = next_pos[1], next_pos[0]
        #                 elif algo == "UCS":
        #                     self.x_ucs, self.y_ucs = next_pos[1], next_pos[0]
        #                 elif algo == "A*":
        #                     self.x_astar, self.y_astar = next_pos[1], next_pos[0]

        #     # Cập nhật thời gian di chuyển cuối cùng
        #     self.last_move_time = pygame.time.get_ticks()

        #     # Tăng chỉ số đường đi sau khi xử lý tất cả thuật toán
        #     self.path_index += 1
        # else:   
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
        # if self.algorithm == "ALL":
        #     win.blit(self.image, (self.x_bfs * GRID_SIZE + offset_x, self.y_bfs * GRID_SIZE + offset_y))
        #     win.blit(self.image, (self.x_dfs * GRID_SIZE + offset_x, self.y_dfs * GRID_SIZE + offset_y))
        #     win.blit(self.image, (self.x_ucs * GRID_SIZE + offset_x, self.y_ucs *   GRID_SIZE + offset_y))
        #     win.blit(self.image, (self.x_astar * GRID_SIZE + offset_x, self.y_astar * GRID_SIZE + offset_y))
        # else:
            win.blit(self.image, (self.x * GRID_SIZE + offset_x, self.y * GRID_SIZE + offset_y))