from functools import cache
f = open("data.txt", "r")

#We need tuples to use them as keys in the cache
combinations = tuple()
patterns = tuple()
i = 0

temp_combinations = []
temp_patterns = []

for line in f.readlines():
    if i == 0:
        for element in line.strip().split(", "):
            temp_combinations.append(element)
        combinations = tuple(temp_combinations)
        i = 1
        continue
    if line.strip() == "":
        continue
    temp_patterns.append((line.strip()))

patterns = tuple(temp_patterns)

print(combinations)
print(patterns)

@cache
def check_pattern(pattern):
    @cache

    def match_pattern(pattern, start):
        if start >= len(pattern):
            return True
            
        for combination in combinations:
            if pattern[start:].startswith(combination):
                if match_pattern(pattern, start + len(combination)):
                    return True
        
        return False
    
    result = match_pattern(pattern[0], 0)
    return True if result  else False

counter = 0
for pattern in patterns:
    counter+=1 if check_pattern(pattern) else 0
    
print(counter)
    
    