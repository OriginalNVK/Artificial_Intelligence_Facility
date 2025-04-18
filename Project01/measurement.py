import time
import tracemalloc


def measure_ucs_performance(maze, start, end):
    # Đo thời gian
    start_time = time.time()

    # Đo lượng bộ nhớ
    tracemalloc.start()

    # Biến đếm số node đã mở rộng
    expanded_nodes = [0]  # Dùng list để có thể thay đổi giá trị trong hàm UCS

    # Sửa đổi hàm UCS để đếm số node đã mở rộng
    def ucs_with_metrics(maze, start, end):
        from collections import defaultdict
        import heapq

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

            # Mỗi lần mở rộng một node, tăng biến đếm
            expanded_nodes[0] += 1
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

    # Chạy thuật toán
    path = ucs_with_metrics(maze, start, end)

    # Kết quả đo lường
    execution_time = time.time() - start_time
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return {
        "path": path,
        "execution_time": execution_time,  # milliseconds
        "memory_usage": peak, # bytes
        "expanded_nodes": expanded_nodes[0],
    }

def measure_dfs_performance(maze, start, end):
    start_time = time.time()
    tracemalloc.start()

    expanded_nodes = [0]

    def dfs_with_metrics(maze, start, end, visited, path):
        if start == end:
            return path

        visited.add(start)
        expanded_nodes[0] += 1

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dy, dx in directions:
            new_y, new_x = start[0] + dy, start[1] + dx
            neighbor = (new_y, new_x)

            if (
                0 <= new_y < len(maze)
                and 0 <= new_x < len(maze[0])
                and maze[new_y][new_x] == " "
                and neighbor not in visited
            ):
                result = dfs_with_metrics(maze, neighbor, end, visited, path + [neighbor])
                if result:
                    return result

        return None

    path = dfs_with_metrics(maze, start, end, set(), [start])

    execution_time = time.time() - start_time
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return {
        "path": path,
        "execution_time": execution_time,
        "memory_usage": peak,
        "expanded_nodes": expanded_nodes[0],
    }

def measure_bfs_performance(maze, start, end):
    start_time = time.time()
    tracemalloc.start()

    expanded_nodes = [0]

    from collections import deque

    def bfs_with_metrics(maze, start, end):
        queue = deque([(start, [start])])
        visited = set()

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while queue:
            current_pos, path = queue.popleft()

            if current_pos == end:
                return path

            if current_pos in visited:
                continue

            expanded_nodes[0] += 1
            visited.add(current_pos)

            for dy, dx in directions:
                new_y, new_x = current_pos[0] + dy, current_pos[1] + dx
                neighbor = (new_y, new_x)

                if (
                    0 <= new_y < len(maze)
                    and 0 <= new_x < len(maze[0])
                    and maze[new_y][new_x] == " "
                    and neighbor not in visited
                ):
                    queue.append((neighbor, path + [neighbor]))

        return None

    path = bfs_with_metrics(maze, start, end)

    execution_time = time.time() - start_time
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return {
        "path": path,
        "execution_time": execution_time,
        "memory_usage": peak,
        "expanded_nodes": expanded_nodes[0],
    }

def measure_astar_performance(maze, start, end):
    start_time = time.time()
    tracemalloc.start()

    expanded_nodes = [0]

    def astar_with_metrics(maze, start, goal):
        from collections import defaultdict
        import heapq

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

        open_list = []
        closed_set = set()
        open_set = set()
        all_nodes = {}

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

            expanded_nodes[0] += 1

            for dx, dy in directions:
                neighbor = (current_node.position[0] + dx, current_node.position[1] + dy)

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

    path = astar_with_metrics(maze, start, end)

    execution_time = time.time() - start_time
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return {
        "path": path,
        "execution_time": execution_time,
        "memory_usage": peak,
        "expanded_nodes": expanded_nodes[0],
    }
