data = open("data", 'r').read().splitlines()
machinesAndPrizes = []
temp = []
for i, line in enumerate(data):
    if i%4 == 0 or i%4 == 1 :
        temp.append((int(line.split()[2].split('+')[1].split(',')[0])  ,  int(line.split()[3].split('+')[1] )))
    elif i%4 == 2:
        temp.append((int(line.split()[1].split('=')[1].split(',')[0])  ,   int(line.split()[2].split('=')[1] )))
    elif i % 4 == 3:
        machinesAndPrizes.append(temp)
        temp = []
if temp:
    machinesAndPrizes.append(temp)

print(machinesAndPrizes)
counter = 0
for machine in machinesAndPrizes:
    a1 = machine[0][0]
    a2 = machine[0][1]
    b1 = machine[1][0]
    b2 = machine[1][1]
    c1 = machine[2][0] + 10000000000000
    c2 = machine[2][1] + 10000000000000
    x = (c1*b2 - b1*c2 )/ ( a1*b2 - b1*a2)
    y = (a1*c2 - c1*a2 )/ ( a1*b2 - b1*a2)
    
    if int(x) == x and int(y) == y:
        counter += 3*x + y
        continue 

print(counter)
