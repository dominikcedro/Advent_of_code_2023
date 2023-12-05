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
                if source_range[0] < input < source_range[1]:
                    # print(f"seed {input} is in range")
                    output = input + (improvised_matrix[k][0] - improvised_matrix[k][1])
                    # print(f"output is  {output}")
                    input = output
                    if line == "finish":
                        print(f"final output is {output}")
                        break
                    continue
                else:
                    if output == 0:
                        # print(f"seed {input} is not in range")
                        output = input
                        input = output
                        if line == "finish":
                            print(f"final output is {output}")
                            break
                        continue
            improvised_matrix = []
            continue
        else:
            new_row = extract_numbers_from_line(line)
            improvised_matrix.append(new_row)
            # print(new_row)





data = read_data("day5_data.txt")
# list_seeds = [79, 14, 55, 13]
# for seed in list_seeds:
#     print(f"seed is {seed}")
#     read_rows(data,seed)

read_rows(data, 14)