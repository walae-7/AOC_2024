import time
import copy
from itertools import combinations


start_time = time.time()

f = open("dummy_data_2.txt", "r")
data = []


for line in f.readlines() :
    temp_line = []
    for element in line.strip():
        temp_line.append(element)
    data.append(temp_line)

alphabet_maj = [chr(i) for i in range(65, 91)]

def areaAndshared_side(region) :
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
    shared_side = 0
     
    combs = combinations(region, 2)
    for comb in list(combs):
        if (abs(comb[0][0] - comb[1][0]) == 1 and comb[0][1] == comb[1][1]):
            r1, c1 = comb[0]
            r2, c2 = comb[1]
            shared_side += 1
            if (r1, c1-1) not in region and (r2, c2-1) not in region:
                shared_side += 1
            elif (r1, c1+1) not in region and (r2, c2+1) not in region:
                shared_side += 1
            elif (r1-1, c1) not in region and (r2-1, c2) not in region:
                shared_side += 1
            elif (r1+1, c1) not in region and (r2+1, c2) not in region:
                shared_side += 1
                
        elif (comb[0][0] == comb[1][0] and abs(comb[0][1] - comb[1][1]) == 1):
            r1, c1 = comb[0]
            r2, c2 = comb[1]
            shared_side += 1
            if (r1, c1-1) not in region and (r2, c2-1) not in region:
                shared_side += 1
            elif (r1, c1+1) not in region and (r2, c2+1) not in region:
                shared_side += 1
            elif (r1-1, c1) not in region and (r2-1, c2) not in region:
                shared_side += 1
            elif (r1+1, c1) not in region and (r2+1, c2) not in region:
                shared_side += 1
            

    area = len(region)
    sides = perimeter - shared_side
    return area, sides
      
    
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
                    print(f"region : {region} , letter : {letter }, regions : {regions}")

    return regions  

counter = 0
for letter in alphabet_maj :
    regions = findRegions(data, letter)
    for region in regions:
        area, perimeter = areaAndshared_side(region)
        print(f"area : {area} , perimeter : {perimeter}")
        counter += area*perimeter

end_time = time.time()
        
print(counter)
print("Time elapsed: ", end_time - start_time)