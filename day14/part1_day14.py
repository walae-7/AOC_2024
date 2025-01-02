import math
data = open("data", 'r').read().splitlines()
positionsAndVelocities = []

for line in data:
    positionsAndVelocities.append([int(line.split()[0].split('=')[1].split(',')[0]) ,  
                                   int(line.split()[0].split(',')[1]), 
                                   int(line.split()[1].split('=')[1].split(',')[0]) ,  
                                   int(line.split()[1].split(',')[1])])

width = 101
height = 103
time = 100
quadrants = [0,0,0,0]

for positionAndVelocity in positionsAndVelocities:
    # for the evolution of each robot
    positionAndVelocity[0] += time*positionAndVelocity[2]
    positionAndVelocity[1] += time*positionAndVelocity[3]
    while positionAndVelocity[0] < 0 :
        positionAndVelocity[0] = width - abs(positionAndVelocity[0])
    while positionAndVelocity[0] >= width :
        positionAndVelocity[0] =  positionAndVelocity[0] -width

    while positionAndVelocity[1] < 0 :
        positionAndVelocity[1] = height - abs(positionAndVelocity[1])
    while positionAndVelocity[1] >= height:
        positionAndVelocity[1] =  positionAndVelocity[1] -height
    #counting in each one of the quadrants
    if positionAndVelocity[0] == width//2 or positionAndVelocity[1] == height //2 :
        continue
    if positionAndVelocity[0] <= width//2 and positionAndVelocity[1] <= height //2 :
        quadrants[0] += 1
    elif positionAndVelocity[0] > width//2 and positionAndVelocity[1] <= height //2 :
        quadrants[1] += 1
    elif positionAndVelocity[0] <= width//2 and positionAndVelocity[1] > height //2 :
        quadrants[2] += 1
    elif positionAndVelocity[0] > width//2 and positionAndVelocity[1] > height //2 :
        quadrants[3] += 1

print(math.prod(quadrants))

