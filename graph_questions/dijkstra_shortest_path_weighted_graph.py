import heapq
import math
graph = {
    "A": {"B": 5, "C": 1},
    "B": {"A": 5, "C": 2, "D":1},
    "C": {"A": 1, "B": 2, "D": 4, "E": 8},
    "D": {"B": 1, "C": 4, "E": 3, "F": 6},
    "E": {"C": 8, "D": 3},
    "F": {"D": 6},
}

def init_distance(graph, s):
    distance = {s: 0}
    for vertex in graph:
        if vertex != s:
            distance[vertex] = math.inf # set as infinity
    return distance

def dijkstra(graph, s):
    pqueue = []
    heapq.heappush(pqueue, (0, s)) # add to heapqueue
    seen = set() # a set
    seen.add(s) # add to set
    parent = {s: None}
    distance = init_distance(graph, s)

    while (len(pqueue) > 0):
        pair = heapq.heappop(pqueue) #grab a pair
        dist = pair[0]
        vertex = pair[1]
        seen.add(vertex)

        nodes = graph[vertex].keys()
        for w in nodes:
            if w not in seen:
                 if dist + graph[vertex][w] < distance[w]:
                     heapq.heappush(pqueue, (dist + graph[vertex][w], w))
                     parent[w] = vertex
                     distance[w] = dist + graph[vertex][w]
    return parent, distance

parent, distance = dijkstra(graph, "A")
print(parent)
print(distance)


#########################################################################################

import heapq


def calculate_distances(graph, starting_vertex):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[starting_vertex] = 0

    pq = [(0, starting_vertex)]
    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq)

        # Nodes can get added to the priority queue multiple times. We only
        # process a vertex the first time we remove it from the priority queue.
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Only consider this new path if it's better than any path we've
            # already found.
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances


example_graph = {
    'U': {'V': 2, 'W': 5, 'X': 1},
    'V': {'U': 2, 'X': 2, 'W': 3},
    'W': {'V': 3, 'U': 5, 'X': 3, 'Y': 1, 'Z': 5},
    'X': {'U': 1, 'V': 2, 'W': 3, 'Y': 1},
    'Y': {'X': 1, 'W': 1, 'Z': 1},
    'Z': {'W': 5, 'Y': 1},
}
print(calculate_distances(example_graph, 'X'))
# => {'U': 1, 'W': 2, 'V': 2, 'Y': 1, 'X': 0, 'Z': 2}