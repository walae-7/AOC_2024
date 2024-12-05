import re
list = open("data.txt",'r')
file = list.read()
pattern = r'(do\(\))|(don\'t\(\))|mul\(([0-9]{1,3}),([0-9]{1,3})\)'

matches = re.findall(pattern, file)
coeff = 1
sum = 0
for match in matches :
    if match[1] == 'don\'t()':
        coeff = 0
    elif match[0] == 'do()':
        coeff = 1
    if match[2] and match[3]:
        sum += coeff * (int(match[2]))*(int(match[3]))
        print(sum)
    


print(sum)

