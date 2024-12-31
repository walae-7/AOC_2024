import re
list = open("data.txt",'r')
file = list.read()
pattern = re.compile(r'mul\(([0-9]{1,3}),([0-9]{1,3})\)')
sum = 0
for match in pattern.finditer(file) :
    sum += (int(match.group(1)))*(int(match.group(2)))
print(sum)