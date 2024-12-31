f = open("data.txt", "r")
data = []

for line in f.readlines() :
    temp_line = []
    for element in line.strip():
        temp_line.append(int(element))
    data.append(temp_line)
    
trailheads = []

for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == 0:
            trailheads.append((i,j))

chain ={i : i +1 for i in range(9)}

print(chain)
print(trailheads)
print(len(trailheads))

def valid_neighbors(matrix, i, j):
    rows, cols = len(matrix), len(matrix[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] 
    neighbors = []
    neighbors_positions = []
    for di, dj in directions:
        ni, nj = i + di, j + dj
        if 0 <= ni < rows and 0 <= nj < cols and matrix[i][j] in chain:
            if chain[matrix[i][j]] == matrix[ni][nj]:
                neighbors.append(matrix[ni][nj])
                neighbors_positions.append((ni,nj))
    return neighbors, neighbors_positions

def parkours(trailheads, data) :
    def single_parkour(list_, data, results) :
        neighbors, neighbors_positions = valid_neighbors(data, list_[-1][0], list_[-1][1])
        n = len(neighbors)
        
        
        for i in range(n) : 
            list_.append(neighbors_positions[i])
            if neighbors[i]!=9 :
                single_parkour(list_, data, results)
            else:
                results.append(list(list_))
            list_.pop()

    counter = 0
    for trailhead in trailheads :
        list_ = [trailhead]
        results = []
        single_parkour(list_, data, results)
        counter += sum(1 for result in results if len(result) == 10)

    return counter
        
counter = parkours(trailheads=trailheads, data = data)
print(counter)


