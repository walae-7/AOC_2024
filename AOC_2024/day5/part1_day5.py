data = open("data.txt", 'r')

comparisons = []
lists = []

for line in data:
    if line.strip():  
        line = line.strip().replace("|", ",").split(",")  
        if len(line) == 2:
            comparisons.append(line)
        else :
            lists.append(line)
                        
    
def check(n, m, comparisons) :
    for element in comparisons :
        if n in element and m in element and element.index(n) > element.index(m) : 
            return False
    return True
            
flag_1 = True
sum = 0
for element in lists :
    length = len(element)
    flag_1 = True
    for i in range(length) : 
        if flag_1 :
            for j in range(i+1,length) :
                if check(element[i], element[j], comparisons=comparisons) :
                    continue
                else : 
                    flag_1 = False
                    break
    if  flag_1 : sum += int(element[length//2])
    
print(sum)
                
            
        
     

