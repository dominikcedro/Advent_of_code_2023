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


def execute():
    data = read_data("day5_data.txt")
    list_seeds = [3082872446, 316680412, 2769223903, 74043323, 4131958457, 99539464, 109726392, 353536902, 619902767,
                  648714498,
                  3762874676, 148318192, 1545670780, 343889780, 4259893555, 6139816, 3980757676, 20172062, 2199623551,
                  196958359]
    list_results = []
    compare_result = read_rows(data, list_seeds[0])
    for seed in list_seeds:
        result = read_rows(data, seed)
        if result < compare_result:
            compare_result = result
    print(compare_result)


execute()