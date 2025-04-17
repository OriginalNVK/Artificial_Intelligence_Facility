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
        "execution_time": execution_time * 1000,  # Đổi sang milliseconds
        "memory_usage": peak / 1024,  # Đổi sang KB
        "expanded_nodes": expanded_nodes[0],
    }
