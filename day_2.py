"""
@author: Dominik Cedro
02.12.2023
Advent of Code 2023
"""



def task_1():
    """This is my solution for the first task for Advent of Code 2023
    This function is given a file with data and returns the multiplication of numbers of marbles in each game,
    numbers are the numbers of marbles for each color that were necessary to play each game.

    Returns:
         int: multiplication of minimum numbers of marbles in each game
    """
    number = 0
    game_num = 0
    possible_game = 0
    dict_colors = {'red': 0, 'green': 0, 'blue': 0}
    with open('day_2_data.txt', 'r') as f:
        data = f.readlines()
        for line in data:
            for word in line.split():
                if word == 'Game':
                    dict_colors = {'red': 0, 'green': 0, 'blue': 0}
                    game_num += 1
                    continue
                if word.isdigit():
                    number = int(word)
                if word.isalpha() or word[:-1].isalpha():
                    color = word
                    if color in dict_colors:
                        if dict_colors[color] > 0:
                            dict_colors[color] = 0
                        dict_colors[color] += number
                    elif color[:-1] in dict_colors:
                        if dict_colors[color[:-1]] > 0:
                            dict_colors[color[:-1]] = 0
                        color = color[:-1]
                        dict_colors[color] += number
                    if dict_colors['red'] > 12 or dict_colors['green'] > 13 or dict_colors['blue'] > 14:
                        dict_colors = {'red': 0, 'green': 0, 'blue': 0}
                        possible_game -= game_num
                        break
            possible_game += game_num
    return possible_game


def task2():
    ''' This is my solution for the second task for Advent of Code 2023
    This function is given a file with data and returns the sum of all the game IDs, that were possible
    with 12 red, 13 green and 14 blue marbles.

    Returns:
        int: sum of all the game IDs, that were possible with 12 red, 13 green and 14 blue marbles.

    '''
    number = 0
    game_num = 0
    dict_colors = {'red': 0, 'green': 0, 'blue': 0}
    sum_numbers = 0
    with open('day_2_data.txt', 'r') as f:
        data = f.readlines()
    for line in data:
        for word in line.split():
            if word == 'Game':
                dict_colors = {'red': 0, 'green': 0, 'blue': 0}
                game_num += 1
                continue
            if word.isdigit():
                number = int(word)
            if word.isalpha() or word[:-1].isalpha():
                color = word
                if color in dict_colors:
                    if dict_colors[color] < number != 0:
                        dict_colors[color] = number
                elif color[:-1] in dict_colors:
                    if dict_colors[color[:-1]] < number != 0:
                        dict_colors[color[:-1]] = number
        sum_numbers += (dict_colors['red'] * dict_colors['green'] * dict_colors['blue'])
    return sum_numbers

print(f"solutions are: {task_1()} and {task2()}")




