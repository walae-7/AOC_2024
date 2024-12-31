import time
map = open("data", "r")

start = tuple()
end = tuple()
obstacles = []

for i, line in enumerate(map.readlines()) : 
    for j,element in enumerate(line) : 
        if element == '#' :
            obstacles.append((i,j))
        elif element == 'S' : 
            start = (i,j)
        elif element == 'E' : 
            end = (i,j) 
length = i + 1

grid = [ [ '.' for _ in range(length)] for _ in range(length)]
for obstacle in obstacles :
    grid[obstacle[0]][obstacle[1]] = '#'
for row in grid :
    print(f"{''.join(row)} ")


def getNeighbours(position, liste):
        dirs = [ (0,-1), (0,1) , (-1,0) , (1,0) ]
        neighbours = []
        for dir in dirs :
            new_position = ( position[0] + dir[0] , position[1] + dir[1] ) 
            if new_position not in liste and new_position[0] < length and new_position[0]> -1 and new_position[1] < length and new_position[1] > -1 :
                neighbours.append(new_position)
        return neighbours

def track(start) :
    visited = []
    queue = [start]
    while queue :
        current_element = queue.pop(0)
        visited.append(current_element)
        next_elements = getNeighbours(current_element, visited) 
        for element in next_elements :
            if grid[element[0]][element[1]] == '.' :
                queue.append(element)
    return visited
            
track = track(start)
real_time = 100
time_ = real_time + 2 #to work with indexes
counter = 0

start = time.time()
for position in track :
    index = track.index(position)
    neighbours = getNeighbours(position, track)
    for neighbour in neighbours :
        obstacles.append(neighbour)
        second_neighbours = getNeighbours(neighbour, obstacles)
        for second_neighbour in second_neighbours :
            if track.index(second_neighbour) - track.index(position) >= time_ :
                counter += 1
        obstacles.pop()


end = time.time()
print(end - start)

print(counter)

#I got an extremely long time of execution (approx 20secs). I'm gonna change my approach in part 2 ...