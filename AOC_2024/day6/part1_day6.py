file = open("dummy_data.txt", 'r')
map = []
i = 0
for line in file : 
    line = line.strip().split(",")
    map.append(line)
    if '^' in line[0] :
        position = (int(i),int(line[0].index('^')))
    i+= 1

def direction(live_direction):
    match live_direction :
        case (-1,0):
            return (0,1)
        case (0,1):
            return (1,0)
        case (1,0):
            return (0,-1)
        case (0,-1):
            return (-1,0)
        case _:
            print("piripipiww")


def check_limits(live_position,live_direction,map):
    if live_position[0] == 0 and live_direction == (0,-1) :
        return False
    elif live_position[0] == len(map) -1 and live_direction == (0,1) :
        return False
    elif live_position[1] == 0 and live_direction == (-1,0) :
        return False 
    elif live_position[1] == len(map[0][0])-1 and live_direction == (1,0) :
        return False
    return True
 
live_position = position
live_direction = (-1,0)
sum = 0

while check_limits(live_position = live_position, live_direction=live_direction , map = map) :
    position_on_map = map[live_position[0] + live_direction[0]][0][live_position[1] + live_direction[1]]
    if position_on_map == '#' :
        live_direction = direction(live_direction)
    live_position = (live_position[0] + live_direction[0],live_position[1] + live_direction[1])
    sum+=1

    print(live_position)
    print(sum)

    

