from collections import defaultdict, deque
import heapq


def bfs(maze, start, end):
    """Breadth-First Search (defined but returns None)"""
    queue = deque([start])
    visited = set([start])
    parent = {start: None}

    directions = [(-1,0), (1,0), (0,-1), (0,1)]

    while queue:
        current = queue.popleft()

        # Nếu tìm thấy Pacman
        if current == end:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1]  # Đường đi từ vị trí start -> end
        
        # Duyệt các ô lân cận
        for dx, dy in directions:
            neighbor = (current[0] + dx, current[1] + dy)

            # Kiểm tra ranh giới
            if(0 <= neighbor[0] < len(maze) and 0 <= neighbor[1] < len(maze[0]) and maze[neighbor[0]][neighbor[1]] == ' ' and neighbor not in visited):
                queue.append(neighbor)
                visited.add(neighbor)
                parent[neighbor] = current  

    # Trả về None nếu không tìm thấy đường đi
    return None


def dfs(maze, start, end):
    """Depth-First Search"""
    stack = [(start, [start])]
    visited = set()

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while stack:
        current, path = stack.pop()

        if current == end:
            return path

        if current in visited:
            continue

        visited.add(current)

        for dx, dy in directions:
            neighbor = (current[0] + dx, current[1] + dy)

            if (
                0 <= neighbor[0] < len(maze)
                and 0 <= neighbor[1] < len(maze[0])
                and maze[neighbor[0]][neighbor[1]] == " "
                and neighbor not in visited
            ):
                stack.append((neighbor, path + [neighbor]))

    return None


def ucs(maze, start, end):
    priority_queue = [(0, start, [start])]
    visited = set()
    cost_so_far = defaultdict(lambda: float("inf"))
    cost_so_far[start] = 0

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while priority_queue:
        current_cost, current_pos, path = heapq.heappop(priority_queue)

        if current_pos == end:
            return path

        if current_pos in visited:
            continue

        visited.add(current_pos)

        for dy, dx in directions:
            new_y, new_x = current_pos[0] + dy, current_pos[1] + dx
            neighbor = (new_y, new_x)

            if (
                0 <= new_y < len(maze)
                and 0 <= new_x < len(maze[0])
                and maze[new_y][new_x] == " "
            ):

                new_cost = current_cost + 1

                if new_cost < cost_so_far[neighbor]:
                    cost_so_far[neighbor] = new_cost
                    new_path = path + [neighbor]
                    heapq.heappush(priority_queue, (new_cost, neighbor, new_path))

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
            if 0 <= neighbor[0] < len(maze) and 0 <= neighbor[1] < len(maze[0]):
                if maze[neighbor[0]][neighbor[1]] != " ":
                    continue

                if neighbor in closed_set:
                    continue

                new_g = current_node.g + 1

                if neighbor not in all_nodes or new_g < all_nodes[neighbor].g:
                    neighbor_node = Node(
                        neighbor, current_node, new_g, heuristic(neighbor, goal)
                    )
                    if neighbor not in open_set:
                        heapq.heappush(open_list, neighbor_node)
                        open_set.add(neighbor)
                    all_nodes[neighbor] = neighbor_node

    return None
