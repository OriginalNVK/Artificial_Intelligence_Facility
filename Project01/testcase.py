from measurement import measure_ucs_performance, measure_dfs_performance, measure_bfs_performance, measure_astar_performance
from settings import MAZE

test_cases = [
    {"name": "Gần nhau", "start": (3, 4), "end": (5, 6)},
    {"name": "Khoảng cách trung bình", "start": (3, 4), "end": (9, 12)},
    {"name": "Xa nhau", "start": (3, 4), "end": (15, 16)},
    {"name": "Có nhiều rào cản", "start": (7, 1), "end": (9, 1)},
    {"name": "Đường dài nhất", "start": (3, 4), "end": (15, 3)},
]

results = []
for case in test_cases:
    ucs_result = measure_ucs_performance(MAZE, case["start"], case["end"])
    dfs_result = measure_dfs_performance(MAZE, case["start"], case["end"])
    bfs_result = measure_bfs_performance(MAZE, case["start"], case["end"])
    astar_result = measure_astar_performance(MAZE, case["start"], case["end"])

    results.append(
        {
            "name": case["name"],
            "start": case["start"],
            "end": case["end"],
            "ucs": {
                "path_length": len(ucs_result["path"]) if ucs_result["path"] else 0,
                "execution_time": ucs_result["execution_time"],
                "memory_usage": ucs_result["memory_usage"],
                "expanded_nodes": ucs_result["expanded_nodes"],
            },
            "dfs": {
                "path_length": len(dfs_result["path"]) if dfs_result["path"] else 0,
                "execution_time": dfs_result["execution_time"],
                "memory_usage": dfs_result["memory_usage"],
                "expanded_nodes": dfs_result["expanded_nodes"],
            },
            "bfs": {
                "path_length": len(bfs_result["path"]) if bfs_result["path"] else 0,
                "execution_time": bfs_result["execution_time"],
                "memory_usage": bfs_result["memory_usage"],
                "expanded_nodes": bfs_result["expanded_nodes"],
            },
            "astar": {
                "path_length": len(astar_result["path"]) if astar_result["path"] else 0,
                "execution_time": astar_result["execution_time"],
                "memory_usage": astar_result["memory_usage"],
                "expanded_nodes": astar_result["expanded_nodes"],
            },
        }
    )

# In kết quả
for result in results:
    print(f"Test case: {result['name']}")
    print(f"Start: {result['start']}, End: {result['end']}")
    print("UCS:")
    print(f"  Path length: {result['ucs']['path_length']}")
    print(f"  Execution time: {result['ucs']['execution_time']} milliseconds")
    print(f"  Memory usage: {result['ucs']['memory_usage']} bytes")
    print(f"  Expanded nodes: {result['ucs']['expanded_nodes']} nodes")
    print("DFS:")
    print(f"  Path length: {result['dfs']['path_length']}")
    print(f"  Execution time: {result['dfs']['execution_time']} milliseconds")
    print(f"  Memory usage: {result['dfs']['memory_usage']} bytes")
    print(f"  Expanded nodes: {result['dfs']['expanded_nodes']} nodes")
    print("BFS:")
    print(f"  Path length: {result['bfs']['path_length']}")
    print(f"  Execution time: {result['bfs']['execution_time']} milliseconds")
    print(f"  Memory usage: {result['bfs']['memory_usage']} bytes")
    print(f"  Expanded nodes: {result['bfs']['expanded_nodes']} nodes")
    print("A*:")
    print(f"  Path length: {result['astar']['path_length']}")
    print(f"  Execution time: {result['astar']['execution_time']} milliseconds")
    print(f"  Memory usage: {result['astar']['memory_usage']} bytes")
    print(f"  Expanded nodes: {result['astar']['expanded_nodes']} nodes")
    print("-" * 40)
