from art import logo, vs
from game_data import data
import random

# TODO: Vygenerovat A i B aby ukazovali sami sebe 50 uzivatelu
# Rozmyslet se jestli pomoci listu nebo dict
# https://replit.com/@appbrewery/higher-lower-final


# TODO: vymyslet abz se 49 zmensovala. Nahradit variable
LAST_NUMBER = len(data) - 1
lo = 0


def minus_number(number_last):
    number_last -= 1
    return number_last


# TODO: SCORE
def score(number, bool_result):
    if bool_result:
        number += 1
    return number


# TODO: ODSTRANIT UZIVATELE, KTERY UZ TAM BYL
def remove_name(number_in_list, name_of_list):
    name_of_list.pop(number_in_list)
    return name_of_list

def check_list(listA, listB):
    result = True
    if len(listA) == 0 or len(listB) == 0:
        result = False
    return result



# TODO: VYPOCITANI FOLLOWERS, KTERY MAJ
def vypocet_followers(new_list, numA, numB, guess):
    first_pick = new_list[numA]["follower_count"]
    second_pick = new_list[numB]["follower_count"]
    print(f"First Pick: {first_pick}")
    print(f"Second Pick: {second_pick}")
    if guess == "A":
        guess = new_list[numA]["follower_count"]
    if guess == "B":
        guess = new_list[numB]["follower_count"]
    result = True
    if first_pick == guess and first_pick > second_pick:
        result = True
    elif second_pick == guess and second_pick > first_pick:
        result = True
    elif (first_pick == guess or second_pick == guess) and first_pick == second_pick:
        result = True
    else:
        result = False
        print("PROHRA")
    return result


# TODO: PRINT OBOJIHO
# TODO: MRKNOUT NA LISTY VIZ NIZ:
#LAST_NUMBER SE NEAKTUALIZUJE
# NumeberA: .........15.........
# NumberB: .........45.........
# NumberA list: .........45.........
# NumberB list: .........45.........
def print_A_or_B(number):
    lo = 0
    nu = 1

    ahoj = list(data)
    os = list(data)
    for x in ahoj:
        print(x)

    while nu > 0:
        numberA = random.randint(0, number)
        numberB = random.randint(0, number)
        print(f"NumeberA: {numberA:.^20}")
        print(f"NumberB: {numberB:.^20}")
        print(f"NumberA list: {len(ahoj):.^20}")
        print(f"NumberB list: {len(os):.^20}")
        print(f"Number: {number:.^20}")

        print("Compare A: " + ahoj[numberA]["name"] + ", a " + ahoj[numberA]["description"] + ", from " + ahoj[numberA]["country"])
        print(ahoj[numberA]["follower_count"])

        print(vs)

        print("Against B: " + ahoj[numberB]["name"] + ", a " + ahoj[numberB]["description"] + ", from " + ahoj[numberB]["country"])
        print(ahoj[numberB]["follower_count"])
        guess = input("Who has more followers? Type 'A' or 'B': ")
        remove_name(numberA, ahoj)
        remove_name(numberB, os)

        result = vypocet_followers(ahoj, numberA, numberB, guess)
        no_data = check_list(ahoj, os)
        lo = score(lo, result)
        if not no_data:
            print("No data in list. I guess you won!")
            exit()
        if not result:
            print(f"You lost! Your final score: {lo}")
            exit()
        print(f"You're right! Current score: {lo}")

    print("Ok")


# TODO: VSECHNO HODIT DO GAME A PTAT SE NA HRU ZNOVU
def game():
    pass


print_A_or_B(minus_number(LAST_NUMBER))

