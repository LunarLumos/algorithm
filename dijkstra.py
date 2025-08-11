import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

# Example graph
graph = {
    '1': [('2', 10), ('3', 3), ('4', 4)],
    '2': [('1', 2), ('3', 5), ('4', 6)],
    '3': [('1', 7), ('2', 7), ('4', 1)],
    '4': []
}

start_node = '1'
shortest_distances = dijkstra(graph, start_node)

# Print shortest distances
for node, dist in shortest_distances.items():
    print("Distance from node", start_node, "to node", node, "is", dist)
