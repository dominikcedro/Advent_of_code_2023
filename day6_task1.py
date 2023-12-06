import re
import numpy as np
def read_file_get_input(file):
    matrix = np.empty((0, 4), int)
    with open("day6_data.txt") as f:
        data = f.read().splitlines()
    for line in data:
        numbers = re.findall(r'\d+', line)
        numbers = [int(number) for number in numbers]
        new_row = np.array(numbers)
        matrix = np.vstack((matrix, new_row))
    return matrix

def get_pairs(matrix):
    pairs = []
    for k in range(0,4):
        column = matrix[:, k].tolist()
        pairs.append(column)
    return pairs

def calculate_possible(pairs):
    possibles = []
    for pair in pairs:
        distance = pair[1]
        time = pair[0]
        button_time1 = 0
        calculated_distance = 0
        while calculated_distance <= distance:
            calculated_distance = button_time1 * (time - button_time1)
            button_time1 += 1
        range_begin = button_time1-1
        button_time2 = time
        calculated_distance2 = 0
        while calculated_distance2 <= distance:
            calculated_distance2 = button_time2 * (time - button_time2)
            button_time2 -= 1
        range_end = button_time2+1
        possible = range_end - range_begin +1
        possibles.append(possible)
    result = 1
    for k in possibles:
        result *= k
    print(result)

def main():
    matrix = read_file_get_input("day6_data.txt")
    pairs = get_pairs(matrix)
    calculate_possible(pairs)


main()