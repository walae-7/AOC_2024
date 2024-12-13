file = open("data.txt", 'r')
line = file.readlines()[0].strip()


def createFile(line):
    result = []
    counter = 0
    for i in range(0, len(line)):
        if i%2 == 0:
            for j in range(0, int(line[i])):
                result.append(str(counter))
            counter += 1
        else:
            for j in range(0, int(line[i])):
                result.append('.')
            
    return result

disk_file_list = createFile(line)

m = len(disk_file_list)
left = 0
right = m-1
while left < right :
    if disk_file_list[left] == '.' :
        if disk_file_list[right] != '.':
            disk_file_list[left] = disk_file_list[right]
            disk_file_list[right] = '.'
            left +=1
        right-=1
    else :
        left+=1


def calculateCheckSum(compressed):
    sum = 0
    for i in range(len(compressed)):
        if compressed[i] != ".":
            sum += i * int(compressed[i])
    return sum

print(calculateCheckSum(disk_file_list))