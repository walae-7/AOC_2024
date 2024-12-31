from functools import cache
line = open("data.txt", "r").read().strip().split(" ") #insane anass hack

#lists are not hashable, so we should use tuples

@cache
def update_element(element): 
    element = int(element)
    if element == 0:
        return [1]
        
    elif len(str(element))%2 == 0 :
        mid = len(str(element)) // 2
        element1 = int(str(element)[:mid]) 
        element2 = int(str(element)[mid:]) 
        return [element1, element2]
        
    else :
        return [2024*element]
  
@cache
def update_list(L, n) :
    if n == 0:
        return len(L)
    else: 
        return sum(update_list(tuple(update_element(stone)), n - 1) for stone in L)
    
print(update_list(tuple(line), 75))