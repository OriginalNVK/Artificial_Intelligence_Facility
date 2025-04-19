import matplotlib.pyplot as plt
import numpy as np

# Dữ liệu từ đề bài: Từng thuật toán có 5 test case (tương ứng với 5 cột: Gần nhau, TB, Xa, Rào cản, Dài nhất)
labels = ['Gần nhau', 'Khoảng cách TB', 'Xa nhau', 'Nhiều rào cản', 'Đường dài nhất']

# UCS
ucs_path_len = [5, 17, 27, 19, 22]
ucs_expanded_nodes = [23, 96, 190, 137, 153]
ucs_exec_time_s = [160000 / 1e9, 348200 / 1e9, 1230500 / 1e9, 840100 / 1e9, 1081300 / 1e9]
ucs_memory_bytes = [5.421875 * 1024, 16.640625 * 1024, 27.265625 * 1024, 16.8203125 * 1024, 16.640625 * 1024]

# DFS
dfs_path_len = [45, 81, 97, 71, 76]
dfs_expanded_nodes = [47, 146, 171, 88, 102]
dfs_exec_time_s = [182700 / 1e9, 911100 / 1e9, 1180600 / 1e9, 519200 / 1e9, 704700 / 1e9]
dfs_memory_bytes = [29.21875 * 1024, 81.5859375 * 1024, 69.1484375 * 1024, 37.25 * 1024, 41.078125 * 1024]

# BFS
bfs_path_len = [5, 17, 27, 19, 22]
bfs_expanded_nodes = [23, 101, 192, 137, 148]
bfs_exec_time_s = [75400 / 1e9, 479200 / 1e9, 898800 / 1e9, 618700 / 1e9, 661100 / 1e9]
bfs_memory_bytes = [3.46875 * 1024, 11.6875 * 1024, 13.2109375 * 1024, 12.3359375 * 1024, 11.6875 * 1024]

# A*
astar_path_len = [5, 21, 29, 19, 22]
astar_expanded_nodes = [4, 56, 66, 39, 44]
astar_exec_time_s = [78300 / 1e9, 611100 / 1e9, 890000 / 1e9, 421200 / 1e9, 425600 / 1e9]
astar_memory_bytes = [6.1953125 * 1024, 19.4140625 * 1024, 22.5234375 * 1024, 12.703125 * 1024, 13.658203125 * 1024]

# Hàm vẽ biểu đồ
def plot_metrics(algorithm_name, path_lengths, expanded_nodes, exec_times, memory_usages):
    x = np.arange(len(labels))
    width = 0.35

    fig, axs = plt.subplots(3, 1, figsize=(10, 10))
    fig.suptitle(f"Biểu đồ đánh giá thuật toán {algorithm_name}", fontsize=16)

    # 1. Độ dài đường đi và số nút mở rộng
    axs[0].bar(x - width/2, path_lengths, width, label='Độ dài đường đi', color='mediumpurple')
    axs[0].bar(x + width/2, expanded_nodes, width, label='Số nút mở rộng', color='mediumseagreen')
    axs[0].set_title("Độ dài đường đi và số nút mở rộng")
    axs[0].set_xticks(x)
    axs[0].set_xticklabels(labels)
    axs[0].legend()

    # 2. Thời gian thực thi
    axs[1].bar(x, exec_times, color='coral')
    axs[1].set_title("Thời gian thực thi (giây)")
    axs[1].set_xticks(x)
    axs[1].set_xticklabels(labels)

    # 3. Bộ nhớ sử dụng
    axs[2].bar(x, memory_usages, color='dodgerblue')
    axs[2].set_title("Sử dụng bộ nhớ (bytes)")
    axs[2].set_xticks(x)
    axs[2].set_xticklabels(labels)

    plt.tight_layout()
    plt.subplots_adjust(top=0.9)
    return fig

# Tạo biểu đồ cho từng thuật toán
fig_ucs = plot_metrics("UCS", ucs_path_len, ucs_expanded_nodes, ucs_exec_time_s, ucs_memory_bytes)
fig_dfs = plot_metrics("DFS", dfs_path_len, dfs_expanded_nodes, dfs_exec_time_s, dfs_memory_bytes)
fig_bfs = plot_metrics("BFS", bfs_path_len, bfs_expanded_nodes, bfs_exec_time_s, bfs_memory_bytes)
fig_astar = plot_metrics("A*", astar_path_len, astar_expanded_nodes, astar_exec_time_s, astar_memory_bytes)

# Hiển thị một ví dụ
plt.show()

