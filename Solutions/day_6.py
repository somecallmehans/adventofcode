from functools import reduce

def part_2_parse(file):
    new_list = []
    time_line = next(file).split()[1:]
    distance_line = next(file).split()[1:]
    time_value = int("".join(time_line))
    distance_value = int("".join(distance_line))
    new_list = [time_value, distance_value]
    return new_list

res_dict = {}
with open("Inputs/day_6_input.txt", "r") as file:
    file_copy = file
    new_data = part_2_parse(file_copy)
    for line in file:
        key, *values = line.split()
        res_dict[key] = values

def wtw():
    ways = []
    for idx, time in enumerate(res_dict['Time:']):
        ways_to_win = 0
        f_time = int(time)
        f_distance = int(res_dict["Distance:"][idx])
        for i in range(0, f_time):
            if((i * (f_time - i)) > f_distance):
                ways_to_win += 1
        ways.append(ways_to_win)
    tt = reduce((lambda x, y: x * y), ways)
    print(tt)

print(new_data)
ways2win = 0
for i in range(0, new_data[0]):
    if((i * (new_data[0] - i)) > new_data[1]):
        ways2win += 1
print(ways2win)