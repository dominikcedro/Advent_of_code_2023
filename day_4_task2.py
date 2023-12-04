import math

import day_4

def calculate_points_mod(dictonary_games):
    dictonary_new = {}
    sum_of_points = 0
# this code below calculates points
    for key in dictonary_games:
        card_nr = dictonary_games[key][0]
        user_nums = dictonary_games[key][1]
        lottery_nums = dictonary_games[key][2]
        points = 0
        for num in user_nums:
            if num in lottery_nums:
                if points == 0:
                    points += 1
                else:
                    points = points * 2
        if points > 0:
            if points == 1:
                dictonary_new[key] = [card_nr, user_nums, lottery_nums, int(points)]
            else:
                dictonary_new[key] = [card_nr, user_nums, lottery_nums, int(math.log(points, 2)+1)]

    return dictonary_new

def main():
    data = day_4.read_data("day4_data.txt")
    dictonary_games = day_4.clean_dictonary(data)
    dictonary_new = calculate_points_mod(dictonary_games)
    return dictonary_games, dictonary_new

dictonary_games, dictonary_new = main()
# print(len(dictonary_new))
# dictonary_games(key) : [card_nr, user_nums, lottery_nums]
# dictonary_new(key) : [card_nr, user_nums, lottery_nums, matching_numbers]
# for card in dictonary_games:
#     print(f"{card} : {dictonary_games[card]}")
# for game in dictonary_new:
#     print(f"{game} : {(dictonary_new[game])}")
list_originals = []
list_copies = []
for key in dictonary_games:
    list_originals.append(key)
# print(list_originals)



for number in list_originals:
    for key in dictonary_new:
            if number == key:
                for i in range(1,dictonary_new[key][3]+1):
                    list_copies.append(dictonary_games[key+i][0])
                    # print(dictonary_games[key+i])
print(list_originals)
print(list_copies)

def even_more_copies(list_originals, list_copies):
    new_list_copies = []
    for number in list_copies:
        for key in dictonary_new:
            if number == key:
                for i in range(1, dictonary_new[key][3] + 1):
                    new_list_copies.append(dictonary_games[key + i][0])

    list_originals += list_copies
    if new_list_copies == []:
        return list_originals
    list_copies = []
    list_copies += new_list_copies
    even_more_copies(list_originals, list_copies)

print(even_more_copies(list_originals,list_copies))
print(len(list_originals))















# for card in dictonary_new:
#     for game in dictonary_games:
#         list_originals.append(dictonary_games[game])
#         if dictonary_new[card][0] == dictonary_games[game][0]:
#             print(f"{card} : {dictonary_new[card]}") # this is the new card
#             # print(f"{game} : {dictonary_games[game]}") # this is the original card
#             for i in range(dictonary_new[card][3]):
#                  #i i+1 is the copy number
#                 list_copies.append(dictonary_games[game+i+1])
#                 dictonary_new[card][3] -= 1
#                 # print(f"{game+i+1} : {dictonary_games[game+i+1]}")  # this is the original card
#                 print("")
# #
# for card in dictonary_new:
#     for i in range(list_copies[card][3]):
#         # i i+1 is the copy number
#         print("card")
#         print("")
#         print(f"copies left: {dictonary_new[3]}")
#         list_copies.append(dictonary_games[game + i + 1])
#         dictonary_new[card][3] -= 1
# print(len(list_originals))
# print(len(list_copies))
