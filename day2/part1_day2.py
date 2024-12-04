list = open("data.txt",'r')
def isValid(line):
    if sorted(line)!=line  and sorted(line,reverse=True) != line:
        return False
    
    flag = 0
    for i in range(n-1):
        diff = abs(line[i]-line[i+1])
        if diff>3 or diff<1 :
            flag = 1
            return False
        
    if flag == 0 :
        return True 


safe_reports = 0
for line in list :
        line = line.strip().split(" ")
        n = len(line)
        line = [int(line[i]) for i in range(n)] 
        if isValid(line) :
            safe_reports+= 1
print(safe_reports)
    