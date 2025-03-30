from collections import defaultdict
import heapq

def bfs(maze, start, end):
    """Breadth-First Search (defined but returns None)"""
    return None

def dfs(maze, start, end):
    """Depth-First Search (defined but returns None)"""
    return None

def ucs(maze, start, end):
    """Uniform Cost Search (defined but returns None)"""
    return None

class Node:
    def __init__(self, position, parent=None, g=0, h=0):
        self.position = position
        self.parent = parent
        self.g = g
        self.h = h
        self.f = g + h
    
    def __lt__(self, other):
        return self.f < other.f or (self.f == other.f and self.h < other.h)

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(maze, start, goal):
    open_list = []
    closed_set = set()
    open_set = set()  # Để kiểm tra nhanh
    all_nodes = {}  # Lưu tất cả các node đã tạo
    
    start_node = Node(start, None, 0, heuristic(start, goal))
    heapq.heappush(open_list, start_node)
    open_set.add(start)
    all_nodes[start] = start_node
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while open_list:
        current_node = heapq.heappop(open_list)
        open_set.remove(current_node.position)
        closed_set.add(current_node.position)
        
        if current_node.position == goal:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]
        
        for dx, dy in directions:
            neighbor = (current_node.position[0] + dx, current_node.position[1] + dy)
            
            # Kiểm tra ranh giới và ô có thể đi qua
            if (0 <= neighbor[0] < len(maze) and 0 <= neighbor[1] < len(maze[0])):
                if maze[neighbor[0]][neighbor[1]] != ' ':
                    continue
                
                if neighbor in closed_set:
                    continue
                
                new_g = current_node.g + 1
                
                if neighbor not in all_nodes or new_g < all_nodes[neighbor].g:
                    neighbor_node = Node(neighbor, current_node, new_g, heuristic(neighbor, goal))
                    if neighbor not in open_set:
                        heapq.heappush(open_list, neighbor_node)
                        open_set.add(neighbor)
                    all_nodes[neighbor] = neighbor_node
    
    return None