from collections import deque

def read_map(filename):
    with open(filename, "r") as f:
        grid = f.readlines()
    length = len(grid)
    obstacles = []
    start = end = None
    
    for i, line in enumerate(grid):
        for j, element in enumerate(line):
            if element == '#':
                obstacles.append((i, j))
            elif element == 'S':
                start = (i, j)
            elif element == 'E':
                end = (i, j)
                
    return start, end, obstacles, length

def get_neighbours(pos, obstacles, length):
    dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    return [
        (pos[0] + dx, pos[1] + dy) for dx, dy in dirs
        if 0 <= pos[0] + dx < length 
        and 0 <= pos[1] + dy < length 
        and (pos[0] + dx, pos[1] + dy) not in obstacles
    ]

def find_paths(start, length, obstacles):
    distances = {start: 0}
    queue = deque([start])
    paths = []
    
    while queue:
        current = queue.popleft()
        paths.append(current)
        
        for neighbor in get_neighbours(current, obstacles, length):
            if neighbor not in distances:
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)
                
    return paths, distances

def count_time_matches(paths, distances, time_limit):
    count = 0
    for i, pos in enumerate(paths):
        for neighbor in get_neighbours(pos, [], length):
            if neighbor in distances and distances[neighbor] - distances[pos] >= time_limit:
                count += 1
    return count

# Main execution
start, end, obstacles, length = read_map("data")
paths, distances = find_paths(start, length, obstacles)
real_time = 100
time_limit = real_time + 2
print(count_time_matches(paths, distances, time_limit))
