import math
import os
import time
import copy

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

data = open("data", 'r').read().splitlines()
positionsAndVelocities = []

for line in data:
    positionsAndVelocities.append([int(line.split()[0].split('=')[1].split(',')[0]) ,  
                                   int(line.split()[0].split(',')[1]), 
                                   int(line.split()[1].split('=')[1].split(',')[0]) ,  
                                   int(line.split()[1].split(',')[1])])

width = 101
height = 103


def grid(positionsAndVelocities_, width, height):
    empty_grid = [['.' for _ in range(width)] for _ in range(height)]
    for positionAndVelocity in positionsAndVelocities_:
        empty_grid[positionAndVelocity[1]][positionAndVelocity[0]] = '#'
    for row in empty_grid:
        print(f"{''.join(row)} ")
        

def evolution(temp, time):
    for positionAndVelocity in temp:
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

i = 0
while i<10000:
    i+=1
    evolution(positionsAndVelocities, 1)
    grid(positionsAndVelocities, width, height)
    print(i)
    #clear_console()




