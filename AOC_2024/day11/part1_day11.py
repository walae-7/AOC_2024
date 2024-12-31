line = open("data.txt", "r").read().strip().split(" ") #insane anass hack

n = 25

def update(line, n) :
    empty_line =[]
    if n == 0 :
        return len(line)
    else :
        for element in line :
            element = int(element)
            if element == 0:
                element =  1
                empty_line.append(element)
                
            elif len(str(element))%2 == 0 :
                mid = len(str(element)) // 2
                element1 = int(str(element)[:mid]) 
                element2 = int(str(element)[mid:]) 
                empty_line.append(element1)
                empty_line.append(element2)
            else :
                element*= 2024
                empty_line.append(element)


    return update(empty_line, n-1)

print(update(line, n))
            
