from measurement import measure_ucs_performance
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
    result = measure_ucs_performance(MAZE, case["start"], case["end"])
    results.append(
        {
            "name": case["name"],
            "start": case["start"],
            "end": case["end"],
            "path_length": len(result["path"]) if result["path"] else 0,
            "execution_time": result["execution_time"],
            "memory_usage": result["memory_usage"],
            "expanded_nodes": result["expanded_nodes"],
        }
    )

# In kết quả
for result in results:
    print(f"Test case: {result['name']}")
    print(f"Start: {result['start']}, End: {result['end']}")
    print(f"Path length: {result['path_length']}")
    print(f"Execution time: {result['execution_time']} seconds")
    print(f"Memory usage: {result['memory_usage']} bytes")
    print(f"Expanded nodes: {result['expanded_nodes']}")
    print("-" * 40)
