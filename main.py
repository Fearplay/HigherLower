from art import logo, vs
from game_data import data
import random

# TODO: Vygenerovat A i B aby ukazovali sami sebe 50 uzivatelu
# Rozmyslet se jestli pomoci listu nebo dict
# https://replit.com/@appbrewery/higher-lower-final


# TODO: vymyslet abz se 49 zmensovala. Nahradit variable
LAST_NUMBER = len(data)-1
lo = 0


def minus_number(number_last):
    number_last -= 1
    return number_last

#TODO: SCORE
def score(number, bool_result):
    if bool_result:
        number += 1
    else:
        number = 0
    return number

#TODO: ODSTRANIT UZIVATELE, KTERY UZ TAM BYL
def remove_name(number_in_list, name_of_list):
    name_of_list.pop(number_in_list)
    return name_of_list

#TODO: VYPOCITANI FOLLOWERS, KTERY MAJ
def vypocet_followers(new_list, numA, numB, guess):
    first_pick = new_list[numA]["follower_count"]
    second_pick = new_list[numB]["follower_count"]
    if guess == "A":
        guess = new_list[numA]["follower_count"]
    if guess == "B":
        guess = new_list[numB]["follower_count"]
    result = True
    print("GUe", guess)
    if first_pick == guess and first_pick > second_pick:
        print("LOS")
    elif second_pick == guess and second_pick > first_pick:
        print("DOS")
    else:
        result = False
        print("PROHRA")
    return result

#TODO: PRINT OBOJIHO
def print_A_or_B(number):
    lo = 0
    nu = 1

    numberA = random.randint(0, number)
    numberB = random.randint(0, number)
    ahoj = list(data)
    for x in ahoj:
        print(x)
    print(numberA)
    while nu > 0:
        print("Compare A: "+ahoj[numberA]["name"] + ", a " + ahoj[numberA]["description"] + ", from " + ahoj[numberA]["country"])



        print(vs)

        print("Against B: "+ahoj[numberB]["name"] + ", a " + ahoj[numberB]["description"] + ", from " + ahoj[numberB]["country"])
        remove_name(numberA, ahoj)
        remove_name(numberB, ahoj)
        guess = input("Who has more followers? Type 'A' or 'B': ")
        result = vypocet_followers(ahoj, numberA, numberB, guess)
        lo = score(lo, result)
        print(f"You're right! Current score: {lo}")

    print("Ok")

#TODO: VSECHNO HODIT DO GAME A PTAT SE NA HRU ZNOVU
def game():
    pass


print_A_or_B(minus_number(LAST_NUMBER))
