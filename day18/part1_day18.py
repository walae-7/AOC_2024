from heapq import heappush, heappop
import time 
f = open("data.txt", "r")
data = []

for line in f.readlines() :
    temp_line = []
    for element in line.strip().split(","):
        temp_line.append(int(element))
    data.append(tuple(temp_line))
  
  
obstacle_size = 1024
grid_size = 71
obstacles = data[:obstacle_size]
grid = [ [ '.' for _ in range(grid_size)] for _ in range(grid_size)]
for obstacle in obstacles :
    grid[obstacle[1]][obstacle[0]] = '#'
for row in grid :
    print(f"{''.join(row)} ")



startingPosition = ( 0 , 0 )
endingPosition = (grid_size -1 , grid_size -1 )
distances = {}
distances[startingPosition] = 0

def dijkstra(stratingPosition, endingPosition) : 
    def getNeighbours(position):
        dirs = [ (0,-1), (0,1) , (-1,0) , (1,0) ]
        neighbours = []
        for dir in dirs :
            new_position = (position[1] + dir[1] , position[0] + dir[0] ) #so that they're in the same (x,y) coordinates as the obstacles, and we can comapre them in the next line
            if new_position not in obstacles and new_position[0] < grid_size and new_position[0]> -1 and new_position[1] < grid_size and new_position[1] > -1 :
                neighbours.append((new_position[1],new_position[0]))
        return neighbours
    
    queue = []
    heappush(queue, (0,stratingPosition))
    position = stratingPosition
    while queue :
        cost, position = heappop(queue)

        if position == endingPosition :
            return cost , position
        neighbours = getNeighbours(position = position)
        for neighbour in neighbours :
            if neighbour not in distances or distances[neighbour] > 1 + cost :
                heappush(queue, (1 + cost , neighbour))
                distances[neighbour] = cost + 1 
    return float("inf")

start_time = time.time()
          
cost , position = dijkstra(startingPosition, endingPosition )    

end_time = time.time()
print(f"Time taken: {end_time - start_time}")
print(cost, position)