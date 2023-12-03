with open('day3_data.txt') as f:
    data = f.read().splitlines()
    #
# so line lenght is 140
# print(symbols) # {'@', '*', '=', '.', '%', '-', '#', '/', '$', '&', '+'} these are all the symbols there are in file

#now I will determine positions of symbols in a line
#file is small data
# numbers should be [540,186,48,681,249,935,957,857,512,89,97,874
sum_of_parts = 0
symbols = {'-', '@', '+', '%', '*', '/', '&', '$', '=', '#'}
dict_symbols = {
    '@': [],
    '*': [],
    '=': [],
    '%': [],
    '-': [],
    '#': [],
    '/': [],
    '$': [],
    '&': [],
    '+': []
}
#this part reads coordinates of symbols in lines
list_of_dictonaries_symbols = []
count = 0
for line in data:
    for char in line:
        count += 1
        if char in symbols:
            dict_symbols[char].append(count-1)
            dict_symbols[char] = sorted(dict_symbols[char]) # is it really necessary
    count = 0
    list_of_dictonaries_symbols.append(dict_symbols)
    # clear dict_symbols
    dict_symbols = {
        '@': [],  # list of tuples, in these tuple i will store line number and position on a line
        '*': [],
        '=': [],
        '%': [],
        '-': [],
        '#': [],
        '/': [],
        '$': [],
        '&': [],
        '+': []
    }

# this part read coordinates of numbers in line
count_num = 0
is_number = False
list_of_dictonaries_numbers = []
dict_numbers = {}
for line in data:
    # print("line is", data.index(line))
    for char in line:
        count_num += 1
        if char.isdigit():
            is_number = True
            if line[count_num-2].isdigit():
                continue
            if count_num+1 == len(line):
                number = int(line[count_num-1])
                dict_numbers[number] = [count_num-1]
                break
            if line[count_num-1].isdigit() and line[count_num].isdigit() and line[count_num+1].isdigit():
                number = int(line[count_num - 1:count_num+2])
                dict_numbers[number] = [count_num-1, count_num, count_num+1] # here i append positions of numbers to their coordinates list
            elif line[count_num-1].isdigit() and line[count_num].isdigit():
                number = int(line[count_num - 1:count_num + 1])
                dict_numbers[number] = [count_num - 1, count_num]  # here i append positions of numbers to their coordinates list
            elif line[count_num-1].isdigit() and (not line[count_num].isdigit()):
                number = int(line[count_num-1])
                dict_numbers[number] = [count_num - 1]
            elif line[count_num].isdigit() and (not line[count_num-1].isdigit()):
                number = int(line[count_num-1])
                dict_numbers[number] = [count_num-1]
            continue
    list_of_dictonaries_numbers.append(dict_numbers)
    dict_numbers = {}
    count_num = 0

#first check online neighours of numbers
on_line_parts = []
# i will go through all lines, by 2 lines at a time
# i will check if on line 1 there is a number, if there are neighbouring symbols on the same line and
#if on the line 2 there are neighbouring symbols to the number from line 1
# if there are, i will append numbers to list_of_parts

for k in range(len(list_of_dictonaries_numbers)):
    # print("k is", k)
    # print(list_of_dictonaries_numbers[k])
    # # print(list_of_dictonaries_symbols[k])
    # print(f"this is line number {k}")
    # print("numbers", list_of_dictonaries_numbers[k])
    # print("symbols" , list_of_dictonaries_symbols[k])
    # print("on-line neighbours")
    for number in list_of_dictonaries_numbers[k]:
        # print("number is", number)
        # print("number position is", list_of_dictonaries_numbers[k][number])
        # print("symbols are", list_of_dictonaries_symbols[k])
        # print("symbols position is", list_of_dictonaries_symbols[k][symbol])
        for symbol in list_of_dictonaries_symbols[k]:
            if symbol in list_of_dictonaries_numbers[k][number]:
                continue
            for position in list_of_dictonaries_numbers[k][number]:
                if position-1 in list_of_dictonaries_symbols[k][symbol] or position+1 in list_of_dictonaries_symbols[k][symbol]:
                    # print(f"number {number} is on line {k} and has on-line neighbour {symbol}")
                    on_line_parts.append(number)
                    break
                else:
                    continue

of_line_parts = []
#now i will check if there are off-line neighbours
# i will go through all lines, by 2 lines at a time
for line in data:
    index = data.index(line)
    print(index)
    print(list_of_dictonaries_numbers[index]) # this is numbers on line
    print(list_of_dictonaries_symbols[index]) # this is symbols on line
    # print(list_of_dictonaries_numbers[index+1]) # this is numbers on next line
    # print(list_of_dictonaries_symbols[index+1]) # this is symbols on next line
    # print("off-line neighbours")
    for number in list_of_dictonaries_numbers[index]:
        # check if symbols are in previous line
        for symbol in list_of_dictonaries_symbols[index-1]:

            for position in list_of_dictonaries_numbers[index][number]:
                if position-1 in list_of_dictonaries_symbols[index-1][symbol] or position+1 in list_of_dictonaries_symbols[index-1][symbol]:
                    print(f"number {number} is on line {index} and has off-line neighbour {symbol}")

                    of_line_parts.append(number)
                    break
                elif index+1 == len(list_of_dictonaries_symbols):
                        if position-1 in list_of_dictonaries_symbols[index][symbol] or position+1 in list_of_dictonaries_symbols[index][symbol]:
                            print(f"number {number} is on line {index} and has off-line neighbour {symbol}")

                            of_line_parts.append(number)
                            break

                elif position-1 in list_of_dictonaries_symbols[index+1][symbol] or position+1 in list_of_dictonaries_symbols[index+1][symbol]:
                    print(f"number {number} is on line {index} and has off-line neighbour {symbol}")

                    of_line_parts.append(number)
                    break
                else:
                    continue

sum_of_parts = sum(on_line_parts) + sum(of_line_parts)
print("sum of parts is", sum_of_parts)

# solution is 505537
