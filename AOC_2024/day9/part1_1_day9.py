f = open("data.txt", "r")
data = f.readlines()[0].strip()
f.close()

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

def compressFile(file):
    right = len(file)-1
    left = 0
    while left < right:
        if file[right] != '.':
            while file[left] != '.':
                left += 1
                if left == right:
                    return file
            file[left] = file[right]
            file[right] = '.'
        right -= 1

    return file

def calculateCheckSum(compressed):
    sum = 0
    for i in range(len(compressed)):
        if compressed[i] != ".":
            sum += i * int(compressed[i])
    return sum

# print(data)
result = createFile(data)
# print("".join(result))
compressed = compressFile(result)
# print("".join(compressed))
print(calculateCheckSum(compressed))