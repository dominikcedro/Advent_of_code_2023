import day_4




# good, it works i like it very much good computer :)

# so basically i have to divide cards into originals and copies
#there is only one original of the card, test is copies

# then i have to first check how many original cards i will have, it's gonna be those cards that had more than 0 points
# from these cards i can read their numbers and check how many copies there are

# the dictonary_games would be a carte blanche for everything, i won't modyfy it in any way

#first lets create a copy of this dict and delete all games that got no points

def calculate_points_mod(dictonary_games):
    dictonary_new = {}
    sum_of_points = 0
# this code below calculates points
    for key in dictonary_games:
        user_nums = dictonary_games[key][0]
        lottery_nums = dictonary_games[key][1]
        points = 0
        for num in user_nums:
            if num in lottery_nums:
                if points == 0:
                    points += 1
                else:
                    points = points * 2
        if points > 0:
            dictonary_new[key] = [user_nums, lottery_nums, points]

    return dictonary_new

def main():
    data = day_4.read_data("day4_data.txt")
    dictonary_games = day_4.clean_dictonary(data)
    dictonary_new = calculate_points_mod(dictonary_games)
    return dictonary_games, dictonary_new


dictonary_new = main()[1]
dictonary_games = main()[0]
# for key in dictonary_new:
#     print(f"{key} : {dictonary_new[key]}")
# print(len(dictonary_new))

# dictonary_new(key) : [user_nums, lottery_nums, points]

for game in dictonary_new:
    print(f"{game} : {(dictonary_new[game][2])}")