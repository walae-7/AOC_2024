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
    temp_patterns.append((line.strip(),))

patterns = tuple(temp_patterns) 
counter = 0


@cache
def check_pattern(pattern):
    @cache
    def match_pattern(pattern, start):
        if start >= len(pattern):
            return 1
        counter = 0
        for combination in combinations:
            if pattern[start:].startswith(combination):
                counter+=match_pattern(pattern, start + len(combination))  
        return counter
        
    return match_pattern(pattern[0], 0)   

#Je retournait True et counter dans la fonction match_pattern, mais en fait il vaut mieux retourner un seul type de donnée

gen_counter = 0 
for pattern in patterns:
    counter = check_pattern(pattern) 
    gen_counter+=counter
    
print(gen_counter)


    
    