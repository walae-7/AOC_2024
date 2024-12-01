list = open("input_part1.txt",'r')
column1 = []
column2 = []
for line in list:
    column1.append(int(line.split()[0]))
    column2.append(int(line.split()[1]))

sm = 0
for element in column1:
    n=0
    while element in column2 :
        column2.remove(element)
        n+=1
    sm+=element*n
    

print(sm)
