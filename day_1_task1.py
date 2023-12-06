"""
@author Dominik Cedro
01.12.2023
Advent of Code 2023 - day 1
"""

numbers_dict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five" : 5,
    "six" : 6,
    "seven" : 7,
    "eight" : 8,
    "nine" : 9
}

def check_digits(string):
    # check if the string contains just one digit
    count = 0
    number = ""
    for i in range(len(string)):
        if string[i].isdigit():
            count += 1
            number = string[i]
    if count == 1:
        return number
    else:
        return False



def take_digits(string, numbers_dict):
    digit_list =[]
    word = ""
    for i in string:
        if i.isdigit():
            digit_list.append(int(i))
        else:
            word += i
            for k in numbers_dict:
                if k in word:
                    digit_list.append(numbers_dict[k])
                    # leave last letter of the word only
                    word = i
    digit1 = int(digit_list[0])
    digit2 = int(digit_list[len(digit_list)-1])
    number = digit1 * 10 + digit2
    # print(string)
    # print(f'list was {digit_list} and number is {number}')
    return number

#
# def main(string):
#    single =  check_digits(string)
#    digit1 ,digit2 = take_digits(string)
#     if not single:
#         return digit1, digit2
#     else:
#         return single

# def main(string):
#     single_digit = check_digits(string)
#     if single_digit:
#         single_digit = int(single_digit + single_digit)
#         return single_digit
#     else:
#         number = take_digits(string)
#         return number
#
# open a file day_1_data.txt and read the content line by line
# for each line, call the main function
# print the result
def read_file():
    file = "day_1_data.txt"
    sum = 0
    with open(file) as f:
        for line in f:
            sum += take_digits(line, numbers_dict)
    print(sum)
read_file()
#

#
# numberos = ['two1nine',
# 'eightwothree',
# 'abcone2threexyz',
# 'xtwone3four',
# '4nineeightseven2',
# 'zoneight234',
# '7pqrstsixteen']
#
# for i in numberos:
#     print(take_digits(i, numbers_dict))

