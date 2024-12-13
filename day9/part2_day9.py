file = open("data.txt", 'r')
line = file.readlines()[0].strip()

def createFile(line):
    result_odd = []
    result_even = []
    counter = 0
    for i in range(0, len(line)):
        if i%2 == 0:
            temp_res = []
            for j in range(0, int(line[i])):
                temp_res.append(str(counter))
            result_even.append(temp_res)
            counter += 1
        else:
            temp_res = []
            for j in range(0, int(line[i])):
                
                temp_res.append('.')
            result_odd.append(temp_res)
            
    return result_odd, result_even

odd, even = createFile(line)

g = len(odd)
h = len(even)

for i, element_i in enumerate(reversed(even)): #liste des files
    file_length = len(element_i)
    for j, element_j in enumerate(odd[:h-i]): #liste des free space
        empty_file_length = element_j.count('.')
        if empty_file_length >= file_length :
            id = element_j.index('.')
            for k, sub_file_element in enumerate(element_i) :
                odd[j][k + id] = sub_file_element
                even[h-i-1][k] ='.'
            break 


def jme3(liste1 , liste2):
    n, m = len(liste1), len(liste2)
    liste = []
    for i in range(n):      
        liste.append(liste1[i])
        if i<m :
            liste.append(liste2[i])
    return liste

disk_file_list = jme3(even,odd)

compacted_file = [item for sublist in disk_file_list for item in sublist]

def calculateCheckSum(compressed):
    sum = 0
    for i in range(len(compressed)):
        if compressed[i] != ".":
            sum += i * int(compressed[i])
    return sum

print(calculateCheckSum(compacted_file))