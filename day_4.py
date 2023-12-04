
def read_data(file):
    with open(file) as f:
        data = f.read().splitlines()

    dictonary_games = {}
    word = ""
    for line in data:
        word = ""
        user_nums = []
        lottery_nums = []
        for char in line:
            word += char
            if word == f"Card   {data.index(line)+1}: ":
            # print(word) # card number
                dictonary_games[data.index(line)+1] = [data.index(line)+1]
                word = ""
            if word == f"Card  {data.index(line)+1}: ":
            # print(word) # card number
                dictonary_games[data.index(line)+1] = [data.index(line)+1]
                word = ""
            if word == f"Card {data.index(line)+1}: ":
            # print(word) # card number
                dictonary_games[data.index(line)+1] = [data.index(line)+1]
                word = ""
            if char == "|":

                word = word[:-2]
                user_nums = word.split(" ")
                dictonary_games[data.index(line)+1].append(user_nums)
            # print(word)
            # print(user_nums)
                word = ""

        lottery_nums = word.split(" ")
        dictonary_games[data.index(line)+1].append(lottery_nums)
    return dictonary_games
def clean_dictonary(dictonary_games):

    # print("before clearing dictonary")
    # for key in dictonary_games:
    #     print(f"{key} : {dictonary_games[key]}")
# print(dictonary_games)
#i have to clear dictonary of space characters
    for key in dictonary_games:
        user_nums = dictonary_games[key][1]
        lottery_nums = dictonary_games[key][2]
        for num in user_nums:
            if num == "":
                user_nums.remove(num)
        for num in lottery_nums:
            if num == "":
                lottery_nums.remove(num)
    return dictonary_games
    # print("after cleaning")
    # for key in dictonary_games:
    #     print(f"{key} : {dictonary_games[key]}")
#now lets check for each game how many points user got
def calculate_points(dictonary_games):
    sum_of_points = 0
# this code below calculates points
    for key in dictonary_games:
        user_nums = dictonary_games[key][1]
        lottery_nums = dictonary_games[key][2]
        points = 0
        for num in user_nums:
            if num in lottery_nums:
                if points == 0:
                    points += 1
                else:
                    points = points * 2
        # print(f"{key} got {points} points")
        sum_of_points += points
def main():
    dictonary_games = read_data("day4_data.txt")
    clean_dictonary(dictonary_games)
main()