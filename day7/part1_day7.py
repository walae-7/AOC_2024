file = open("data.txt", 'r')

list = []
i = 0
for line in file : 
    line = line.strip().replace(": " , " ").split(" ")
    list.append(line)
    
def check(target, numbers):
    n = len(numbers)
    if n == 1 :
        return numbers[0] == target
    else :
        return check(target, [numbers[0] + numbers[1]] + numbers[2:]) or check(target, [numbers[0] * numbers[1]] + numbers[2:])        
             
total_sum = 0
for line in list :
    target = int(line[0])
    numbers =  [int(n) for n in line[1:]]
    if check(target = target, numbers = numbers) :
        total_sum+= target
        
print(total_sum)
    
    