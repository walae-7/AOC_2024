from itertools import combinations

file = open("data.txt", 'r')
map = []
for line in file : 
    line = line.strip().split(" ")
    map.append(line)
 
antennas = {}
n = len(map)
m = len(map[0][0])
antinodes = set()

for i in range(n) :
    element = map[i][0]
    m = len(element)
    for j in range(m) :
        character = element[j]
        if character != '.':
            if character not in antennas:
                antennas[character] = []
            antennas[character].append((i, j))
   
   
sum_total = 0

for element in antennas.keys() : 
    combs = combinations(antennas[element], 2)

    for comb in list(combs) :
        dx = comb[0][0] - comb[1][0]
        dy = comb[0][1] - comb[1][1]
        pos1 = (comb[0][0] , comb[0][1] )
        pos2 = (comb[1][0] , comb[1][1] )
        while pos1[0] >= 0 and pos1[0] < m and pos1[1] >= 0 and pos1[1] < n:
            antinodes.add(pos1)
            pos1 = (pos1[0] + dx, pos1[1] + dy)


        while pos2[0] >= 0 and pos2[0] < m and pos2[1] >= 0 and pos2[1] < n:
            antinodes.add(pos2)
            pos2 = (pos2[0] - dx, pos2[1] - dy)

print(sum_total+len(antinodes))

  

