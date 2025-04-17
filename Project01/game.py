import pygame
from settings import *
from button import Button
from pacman import Pacman
from ghost import Ghost

class Game:
    def __init__(self, win, algorithm):
        self.win = win
        self.algorithm = algorithm
        self.pacman = Pacman(1, 15)
        self.ghosts = []
        self.create_ghosts()
        self.maze = MAZE
        self.running = True
        self.show_result = False
        self.paths = {}
        
        # Calculate maze position to center it
        maze_width = len(MAZE[0]) * GRID_SIZE
        maze_height = len(MAZE) * GRID_SIZE
        self.maze_offset_x = (WIDTH - maze_width) // 2
        self.maze_offset_y = (HEIGHT - maze_height - 40) // 2  # Leave space for algorithm info
        
        # Position buttons below the maze
        button_y = self.maze_offset_y + maze_height + 10
        self.buttons = [
            Button(self.maze_offset_x, button_y, 100, 40, "Back", RED, (200, 50, 50)),
            Button(self.maze_offset_x + maze_width - 100, button_y, 100, 40, "Result", GREEN, (50, 200, 50))
        ]

    def draw_gradient_background(self):
        """Draw a vertical gradient background"""
        for y in range(HEIGHT):
            # Interpolate between two colors (light purple to dark blue)
            ratio = y / HEIGHT
            # Starting color: #BB86FC (light purple) -> RGB: (187, 134, 252)
            # Ending color: #3700B3 (dark blue) -> RGB: (55, 0, 179)
            r = int(187 * (1 - ratio) + 55 * ratio)
            g = int(134 * (1 - ratio) + 0 * ratio)
            b = int(252 * (1 - ratio) + 179 * ratio)
            pygame.draw.line(self.win, (r, g, b), (0, y), (WIDTH, y))

    def create_ghosts(self):
        if self.algorithm == "ALL":
            self.ghosts.append(Ghost(1, 1, "BFS", BLUE))
            self.ghosts.append(Ghost(1, 1, "DFS", PINK))
            self.ghosts.append(Ghost(1, 1, "UCS", ORANGE))
            self.ghosts.append(Ghost(1, 1, "A*", RED))
        else:
            self.ghosts.append(Ghost(1, 1, self.algorithm, 
                                 BLUE if self.algorithm == "BFS" else 
                                 PINK if self.algorithm == "DFS" else 
                                 ORANGE if self.algorithm == "UCS" else RED))
            
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                return "QUIT"
                
            # xử lý handle click chuột để pacman di chuyển
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for button in self.buttons:
                    if button.is_clicked(mouse_pos, event):
                        if button.text == "Back":
                            return "MENU"
                        elif button.text == "Result":
                            # Kiểm tra xem ghost có bắt được pacman không
                            pacman_pos = self.pacman.get_pos()
                            ghost_caught = any((int(ghost.x), int(ghost.y)) == pacman_pos for ghost in self.ghosts)
                            if ghost_caught:
                                self.show_result = not self.show_result
                                if self.show_result:
                                    self.calculate_paths()
        return None
        
    def calculate_paths(self):
        for ghost in self.ghosts:
            ghost.show_path = True  # Bật hiển thị đường đi
            # Tạo actual_path từ visited_positions
            ghost.actual_path = [(y, x) for x, y in ghost.visited_positions]

            
    def update(self):
        pacman_pos = self.pacman.get_pos()
        for ghost in self.ghosts:
            if not ghost.path or len(ghost.path) == 0:
                ghost.find_path(self.maze, pacman_pos)
            # Lưu vị trí hiện tại vào lịch sử
            current_pos = (int(ghost.x), int(ghost.y))
            if not ghost.visited_positions or ghost.visited_positions[-1] != current_pos:
                ghost.visited_positions.append(current_pos)

            ghost.move()
        # # Tự động hiển thị khi ghost bắt được Pacman
        # if (int(ghost.x), int(ghost.y)) == pacman_pos:
        #     self.show_result = True
        #     ghost.show_path = True
         
    def draw_maze(self, surface):
        for row in range(len(self.maze)):
            for col in range(len(self.maze[0])):
                x = col * GRID_SIZE + self.maze_offset_x
                y = row * GRID_SIZE + self.maze_offset_y
                rect = pygame.Rect(x, y, GRID_SIZE, GRID_SIZE)
                
                # Draw floor background
                pygame.draw.rect(surface, FLOOR_COLOR, rect)
                
                if self.maze[row][col] == "#":
                    # Draw wall with 3D effect
                    wall_rect = pygame.Rect(x + 2, y + 2, GRID_SIZE - 4, GRID_SIZE - 4)
                    pygame.draw.rect(surface, WALL_COLOR, wall_rect, border_radius=CORNER_RADIUS)
                    
                    # Add shadow and highlight
                    pygame.draw.line(surface, WALL_SHADOW, (x + 3, y + GRID_SIZE - 3), 
                                    (x + GRID_SIZE - 3, y + GRID_SIZE - 3), 2)
                    pygame.draw.line(surface, WALL_SHADOW, (x + GRID_SIZE - 3, y + 3), 
                                    (x + GRID_SIZE - 3, y + GRID_SIZE - 3), 2)
                    pygame.draw.line(surface, WALL_HIGHLIGHT, (x + 3, y + 3), 
                                    (x + GRID_SIZE - 3, y + 3), 2)
                    pygame.draw.line(surface, WALL_HIGHLIGHT, (x + 3, y + 3), 
                                    (x + 3, y + GRID_SIZE - 3), 2)
                    
                    # Add wall texture
                    for i in range(0, GRID_SIZE - 4, 4):
                        pygame.draw.line(surface, (50, 50, 255), 
                                        (x + 4, y + 4 + i), 
                                        (x + GRID_SIZE - 4, y + 4 + i), 1)
                
                # Add rounded corners to empty spaces
                if self.maze[row][col] == " ":
                    pygame.draw.rect(surface, FLOOR_COLOR, rect, border_radius=2)
                    pygame.draw.rect(surface, (20, 20, 80), rect, 1, border_radius=2)
                
    def draw(self):
        # Draw gradient background first
        self.draw_gradient_background()
        
        # Vẽ maze
        self.draw_maze(self.win)
        
        # Vẽ đường đi khi show_result = True
        if self.show_result:
            for ghost in self.ghosts:
                if ghost.show_path:
                    # Vẽ tất cả các điểm đã đi qua
                    for pos in ghost.visited_positions:
                        x = pos[0] * GRID_SIZE + self.maze_offset_x + GRID_SIZE//2
                        y = pos[1] * GRID_SIZE + self.maze_offset_y + GRID_SIZE//2
                        pygame.draw.circle(self.win, ghost.color, (x, y), 3)

                    # Vẽ đường nối các điểm (tùy chọn)
                    if len(ghost.visited_positions) > 1:
                        for i in range(len(ghost.visited_positions) - 1):
                            start = (ghost.visited_positions[i][0] * GRID_SIZE + self.maze_offset_x + GRID_SIZE//2,
                                    ghost.visited_positions[i][1] * GRID_SIZE + self.maze_offset_y + GRID_SIZE//2)
                            end = (ghost.visited_positions[i+1][0] * GRID_SIZE + self.maze_offset_x + GRID_SIZE//2,
                                  ghost.visited_positions[i+1][1] * GRID_SIZE + self.maze_offset_y + GRID_SIZE//2)
                            pygame.draw.line(self.win, (*ghost.color, 150), start, end, 2)
        
        # Vẽ pacman và ghosts
        self.pacman.draw(self.win, self.maze_offset_x, self.maze_offset_y)
        for ghost in self.ghosts:
            ghost.draw(self.win, self.maze_offset_x, self.maze_offset_y)
        
        # Vẽ nút
        for button in self.buttons:
            button.draw(self.win)
        
        # Thêm thông tin thuật toán
        if self.algorithm != "ALL":
            info_y = self.maze_offset_y + len(self.maze) * GRID_SIZE + 20
            info = INFO_FONT.render(f"Algorithm: {self.algorithm}", True, WHITE)
            info_rect = info.get_rect(center=(WIDTH//2, info_y))
            self.win.blit(info, info_rect)