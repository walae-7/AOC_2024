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
            
def swap(n, m, comparisons , list_element) :
    if not check(n,m,comparisons) :
        i = element.index(n)
        j = element.index(m)
        list_element[i]= m           
        list_element[j]= n   
    return list_element      


flag_1 = True
sum = 0
for element in lists :
    length = len(element)
    element0 = 0
    for i in range(length) : 
        for j in range(i+1,length) :
            if check(element[i], element[j], comparisons=comparisons) :
                continue
            else : 
                element0 = swap(element[i], element[j], comparisons=comparisons, list_element = element)
                
    if element0!=0:
        sum += int(element0[length//2])

    
print(sum)
                
            