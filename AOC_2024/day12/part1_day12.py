import time

f = open("data.txt", "r")
data = []


for line in f.readlines() :
    temp_line = []
    for element in line.strip():
        temp_line.append(element)
    data.append(temp_line)
    
start_time = time.time()

alphabet_maj = [chr(i) for i in range(65, 91)]

def areaAndPerimeter(region) :
    perimeter = 0
    for element in region :         #on va checker ds toutes les directions:
        if (element[0] + 1 , element[1]) not in region : #down
            perimeter += 1
        if (element[0] - 1 , element[1]) not in region : #up
            perimeter += 1
        if (element[0] , element[1] + 1) not in region : #right
            perimeter += 1
        if (element[0] , element[1] - 1 ) not in region : #left
            perimeter += 1 
    area = len(region)
    return area, perimeter
    
def findRegions(map, letter, regions = None):
    n = len(map)    
    m = len(map[0]) 
    regions = []
    def search(i, j):
        if (i, j) in region or map[i][j] != letter:  #we check if already in region or is different than the searched letter
            return
        region.add((i, j)) 

        if i + 1 < n: search(i + 1, j)  # DOWN
        if i - 1 >= 0: search(i - 1, j) # UP
        if j + 1 < m: search(i, j + 1) # RIGHT
        if j - 1 >= 0: search(i, j - 1) # LEFT

    for i in range(n):
        for j in range(m):
            if map[i][j] == letter :
                if len(regions) == 0 or not any((i, j) in region for region in regions):
                    region = set()  
                    search(i, j)
                    regions.append(list(region))

    return regions  

counter = 0
for letter in alphabet_maj :
    regions = findRegions(data, letter)
    for region in regions:
        area, perimeter = areaAndPerimeter(region)
        counter += area*perimeter

end_time = time.time()
        
print(counter)
print("Time elapsed: ", end_time - start_time)