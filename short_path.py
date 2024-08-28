import heapq
edges = [(1, 2, 4), (2, 3, 2), (1, 4, 2), (1, 2, 4)]
start = 1
end = 4
def dijkstra(edges, start, end):
    # สร้างกราฟในรูปแบบของ adjacency list
    graph = {}
    for edge in edges:
        u, v, weight = edge
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append((v, weight))
        graph[v].append((u, weight))

    # ใช้ priority queue (heap) เพื่อเก็บ node และระยะทางที่พบล่าสุด
    pq = [(0, start)]
    distances = {start: 0}
    visited = set()

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_node in visited:
            continue

        visited.add(current_node)

        if current_node == end:
            return current_distance

        for neighbor, weight in graph.get(current_node, []):
            distance = current_distance + weight
            if neighbor not in distances or distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return float('no way to reach the end')  



shortest_path_length = dijkstra(edges, start, end)
print(f"short distance : {shortest_path_length}")
