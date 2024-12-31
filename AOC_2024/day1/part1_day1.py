list = open("input_part1.txt",'r')
column1 = []
column2 = []
for line in list:
    column1.append(line.split()[0])
    column2.append(line.split()[1])
column1.sort()
column2.sort()
    
diff = [abs(int(i)-int(j)) for i,j in zip(column1, column2)]
print(sum(diff))