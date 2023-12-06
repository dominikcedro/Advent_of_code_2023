
def read_file_get_input(file):
    with open("day6_data.txt") as f:
        data = f.read().splitlines()
    word = ""
    time_and_dist = []
    for line in data:
        for char in line:
            if char.isdigit():
                word +=char
        time_and_dist.append(int(word))
        word = ""
    return time_and_dist

def calculate_possible(pairs):
    possibles = []
    distance = pairs[1]
    time = pairs[0]
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

def execute(file):
    time_and_dist = read_file_get_input(file)
    calculate_possible(time_and_dist)

execute("day6_data.txt")