import sys
from collections import defaultdict, deque

def find_route(n, marks):
    if n == 0:
        return []
    
    graph = defaultdict(list)
    for u, v in marks:
        graph[u].append(v)
        graph[v].append(u)
    
    # Find the starting point (city with the smallest index)
    start = min(graph.keys())
    
    # Use BFS to find the route
    route = []
    visited = set()
    queue = deque([start])
    
    while queue:
        city = queue.popleft()
        if city not in visited:
            visited.add(city)
            route.append(city)
            for neighbor in graph[city]:
                if neighbor not in visited:
                    queue.append(neighbor)
    
    return route

def main():
    input = sys.stdin.read
    data = input().strip().split()
    
    index = 0
    while index < len(data):
        n = int(data[index])
        index += 1
        if n == 0:
            break
        
        marks = []
        for _ in range(n):
            u = int(data[index])
            v = int(data[index + 1])
            marks.append((u, v))
            index += 2
        
        route = find_route(n, marks)
        print(" ".join(map(str, route)))

if __name__ == "__main__":
    main()