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

def read_rows(data):
    improvised_matrix = []
    seed  = 79
    for line in data:
        if data.index(line) < 2:
            continue
        # check if line is empty
        if any(c.isalpha() for c in line):
            print(line)
            print(improvised_matrix)
            for k in range(0,len(improvised_matrix)):
                source_range = [improvised_matrix[k][1], (improvised_matrix[k][1]+improvised_matrix[k][2])-1]
                print(source_range)
                if source_range[0] < seed < source_range[1]:
                    print(f"seed {seed} is in range")
                    output = seed + (improvised_matrix[k][0] - improvised_matrix[k][1])
                    print(f"output is {output}")
                    continue
                else:
                    print(f"seed {seed} is not in range")
                    output = seed
                    print(f"output is {output}")



            improvised_matrix = []
            continue
        else:
            new_row = extract_numbers_from_line(line)
            improvised_matrix.append(new_row)
            print(new_row)
    # print(improvised_matrix)



data = read_data("day5_data.txt")
read_rows(data)