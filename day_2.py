import re

file = open("day_2_input.txt", "r")
content = file.read().split("\n")
# only 12 red cubes, 13 green cubes, and 14 blue cubes in the bag
red = 12
green = 13
blue = 14
thresholds = {'red': red, 'blue': blue, 'green': green}

def remove_game(game_string):
    pattern = r'^Game \d+: '
    return re.sub(pattern, '', game_string)

def process_game_vals(games):
    updated_game_list = []
    nt = games.split(", ")
    for n in nt:
        split = n.split(' ')
        key = split[1]
        val = split[0]
        updated_game_list.append({key: val})

    return updated_game_list

processed_string = [remove_game(game) for game in content]

#################################
# pt 1 answer
#################################
def do_the_thing(one_game):
    # Each instance of this is 1 game
    processed_thing = one_game.split("; ")
    for pt in processed_thing:
        new_list = process_game_vals(pt)
        for g in new_list:
            for key, val in thresholds.items():
                if(key in g and int(g[key]) > val):
                    return False
                else:
                    continue
    return True


valid_games = 0
for idx, one_game in enumerate(processed_string):
    check = do_the_thing(one_game)
    if(check):
        valid_games += (idx + 1)
print("SUM: ", valid_games)

#################################
# pt 2 answer
#################################
def do_the_thing_again(one_game):
    smallest_vals = {}
    processed_thing = one_game.split("; ")
    for pt in processed_thing:
        new_list = process_game_vals(pt)
        for g in new_list:
            for key, current_val in g.items():
                if(key in smallest_vals):
                    if (int(current_val) > int(smallest_vals[key])):
                        smallest_vals[key] = current_val
                else:
                    smallest_vals[key] = current_val
    product = 1
    for val in smallest_vals.values():
        product *= int(val)
    return product


total = 0
for one_game in processed_string:
    summed = do_the_thing_again(one_game)
    total += summed
print("TOTAL: ", total)