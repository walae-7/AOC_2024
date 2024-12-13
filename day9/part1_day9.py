file = open("dummy_data.txt", 'r')
line = file.readlines()[0].strip()
print(line)

n= len(line)
disk_file = []
index = 0
for i, element in enumerate(line): 
    if i % 2 == 0:  
        print(str(index)*int(element))
        disk_file.append(str(index)*int(element)) 
        index+=1
    else:
        print('.'*int(element))
        disk_file.append('.'*int(element)) 
print(disk_file) 
disk_file_string = ''.join(disk_file)
disk_file_list = list(disk_file_string)

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