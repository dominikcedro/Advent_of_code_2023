import numpy as np
import re
def read_data(file):
    with open(file) as f:
        data = f.read().splitlines()
    return data


def extract_numbers_from_line(line):
    # Using regular expression to find all numbers in the line
    numbers = re.findall(r'\d+', line)

    # Converting the found numbers from strings to integers
    numbers = [int(number) for number in numbers]

    return numbers

def read_rows(data, input):
    improvised_matrix = []
    asigned = False
    output = 0
    for line in data:
        if data.index(line) < 2:
            continue

        if any(c.isalpha() for c in line):
            # print(line)
            # print(improvised_matrix)
            for k in range(0, len(improvised_matrix)):
                output = 0
                source_range = [improvised_matrix[k][1], (improvised_matrix[k][1]+improvised_matrix[k][2])-1]
                # print(source_range)
                if source_range[0] <= input <= source_range[1]:
                    # print(f"seed {input} is in range")
                    if asigned:
                        continue
                    output = input + (improvised_matrix[k][0] - improvised_matrix[k][1])
                    asigned = True
                    # print(f"output is asigned {output}")
                    input = output
                    if line == "finish":
                        # print(f"final output is {output}")
                        return output
                    continue
                else:
                    if output == 0:
                        # print(f"seed {input} is not in range")
                        output = input
                        input = output
                        if line == "finish":
                            # print(f"final output is {output}")
                            return output
                        continue
            improvised_matrix = []
            asigned = False
            continue
        else:
            new_row = extract_numbers_from_line(line)
            improvised_matrix.append(new_row)
            # print(new_row)

def get_seeds(data):
    for line in data:
        original_seeds = extract_numbers_from_line(line)
        return original_seeds

def veri_hard_task(data, original_seeds):
    new_seeds = []
    seed = 0
    while len(original_seeds) > 0:
        for i in original_seeds:
            print(original_seeds)
            # here do veri hard calculations
            range = [original_seeds[0], int(original_seeds[0]) + int(original_seeds[1]-1)]
            print(f"range is {range[0]} and {range[1]}")
            start, stop = int(range[0]), int(range[1])
            seed = start
            new_seeds.append(seed)
            while seed < stop:
                seed = seed + 1
                new_seeds.append(seed)
            print(new_seeds)
            print(len(new_seeds))


            del original_seeds[:2]
            continue
def execute():
    data = read_data("day5_data.txt")
    original_seeds = get_seeds(data)
    # i will take te first and second seed as the range and immidiatly delete them from the list
    # but lets do it in a different function :)
    veri_hard_task(data, original_seeds)


execute()
