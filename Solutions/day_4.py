import re

file = open("day_4_input.txt", "r")
lines = file.read().split("\n")


def remove_game(game_string):
    pattern = r'Card\s+\d+\s*:\s*'
    return re.sub(pattern, '', game_string)

def string_splitter(to_split):
    res = re.split(r'\s+', to_split)
    res = list(filter(None, res))
    return res

games = [remove_game(game) for game in lines]

def winning_guesses_exponents(winning, guesses):
    winning_nums = winning_numbers(winning, guesses)
    if winning_nums == 0 or winning_nums == 1:
        return winning_nums
    return 2 ** (winning_nums - 1)

def winning_numbers(winning, guesses):
    winners = [int(num) for num in winning]
    guessers = [int(num) for num in guesses]
    common_vals = set(winners) & set(guessers)
    return len(common_vals)

#################################
##PART 1 Solution
#################################
# for each winning pair, the power goes up by 1 starting at 0.
game_sum = 0
for idx, game in enumerate(games):
    [winning, guesses] = game.split('|')
    game_sum += winning_guesses_exponents(winning=string_splitter(winning), guesses=string_splitter(guesses))
print(game_sum)

#################################
##PART 2 Solution
#################################
card_list = [1 for _ in range(1, len(games) + 1)]
for idx, game in enumerate(games):
    [winning, guesses] = game.split('|')
    winners = winning_numbers(winning=string_splitter(winning), guesses=string_splitter(guesses))
    for i in range(0, card_list[idx]):
        for j in range(idx + 1, (idx + winners + 1)):
            card_list[i] += 1
card_sum = sum(card_list)
print(card_sum)
