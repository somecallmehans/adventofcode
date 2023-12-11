import re

filename = "Inputs/day_7_input.txt"

file = open(filename, "r")
lines = file.read().split("\n")

instructions = list(lines[0])
paths = lines[2:len(lines)]
pattern = re.compile(r'[A-Z]{3}')

path_dict = {}
for p in paths:
    split_paths = p.split()
    code1 = pattern.findall(split_paths[2])[0]
    code2 = pattern.findall(split_paths[3])[0]
    path_dict[split_paths[0]] = [code1, code2]

counter = 0
idx = 0

curr_key = 'AAA'
print(curr_key)

while curr_key != 'ZZZ':
    counter += 1
    print(curr_key)
    if(instructions[idx] == 'L'):
        curr_key = path_dict[curr_key][0]
    if(instructions[idx] == 'R'):
        curr_key = path_dict[curr_key][1]
    
    idx += 1
    idx %= len(instructions)

print(counter)
