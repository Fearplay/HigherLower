from art import logo, vs
from game_data import data
import random
import datetime


number_of_data = len(data) - 1
again_whole_game = True
again_calculate_followers = True


def score(number, bool_result):
    if bool_result:
        number += 1
    return number


def remove_name(number_in_list, name_of_list):
    name_of_list.pop(number_in_list)
    return name_of_list


def check_list(list_with_data):
    result = True
    if len(list_with_data) == 1:
        result = False
    return result


def calculation_of_followers(new_list, first_number, second_number, guess):
    first_pick = new_list[first_number]["follower_count"]
    second_pick = new_list[second_number]["follower_count"]
    if guess == "A":
        guess = new_list[first_number]["follower_count"]
    if guess == "B":
        guess = new_list[second_number]["follower_count"]
    if first_pick == guess and first_pick > second_pick:
        result = True
    elif second_pick == guess and second_pick > first_pick:
        result = True
    elif (first_pick == guess or second_pick == guess) and first_pick == second_pick:
        result = True
    else:
        result = False
    return result


def compare_a_or_b(end_number):
    global again_calculate_followers
    again_calculate_followers = True
    score_number = 0

    data_list = list(data)

    number_a = random.randint(0, end_number)
    while again_calculate_followers:
        number_b = random.randint(0, end_number)
        print(logo)

        print("Compare A: " + data_list[number_a]["name"] + ", a " + data_list[number_a]["description"] + ", from " + data_list[number_a]["country"])

        print(vs)

        print("Against B: " + data_list[number_b]["name"] + ", a " + data_list[number_b]["description"] + ", from " + data_list[number_b]["country"])

        guess = input("Who has more followers? Type 'A' or 'B': ").upper()
        result = calculation_of_followers(data_list, number_a, number_b, guess)

        remove_name(number_a, data_list)

        no_data = check_list(data_list)

        score_number = score(score_number, result)
        if not no_data and result:
            print(f"No data in list. Your final score: {score_number}")
            again_calculate_followers = False
        if not result:
            print(f"You lost! Your final score: {score_number}")
            again_calculate_followers = False

        if no_data and result:
            print(f"You're right! Current score: {score_number}")
            print("")

        if 0 < number_a < number_b or number_a == len(data_list) or number_b == len(data_list):
            number_a = number_b - 1
        else:
            number_a = number_b
        end_number -= 1


def game():
    global again_whole_game
    date = datetime.datetime.now()
    real_hour = date.hour
    while again_whole_game:
        option = input("Do you want to play higher or lower? -y for yes, anything for no: ").upper()
        if option != 'Y':
            if 6 < real_hour < 18:
                print("Have a nice day!")
            else:
                print("Have a nice evening!")
            exit()
        compare_a_or_b(number_of_data)


if __name__ == "__main__":
    game()
