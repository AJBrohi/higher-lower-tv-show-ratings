# import required modules
from art import logo, vs
from random import choice
from data import tv_series
from os import system


def print_tv_series(series, print_rating):
    """This function takes dictionary of a series and boolean of printing rating and print the details of tv series along with printing rating only 'TV Series A'."""
    print(f"""
Name: {series['name']}, {series['year']}
Genre: {series['genre']}""")
    if print_rating:
        print(f"Rating: {series['rating']}")


def answer(a, b):
    """returns the name of TV Series which have higher rating"""
    return a if a >= b else b


def play_game():
    """this is the main function of playing the game"""
    # define score
    score = 0

    # define the boolean of user_play
    user_play = True

    while user_play:
        # clear the console first
        clear()

        # prints logo to screen
        print(logo)

        # if the score is greater than 0. Prints a message to the console to show score. else randomly choose tv series A at first time
        if score > 0:
            print(f"Correct Answer. Your current score is: {score}")
        else:
            tv_series_a = choice(tv_series)

        # print details of tv series A
        print("TV Series A -")
        print_tv_series(tv_series_a, True)

        # print the ascii of vs
        print(vs)

        # randomly choose tv series B
        tv_series_b = choice(tv_series)

        # if both series are same
        while tv_series_a == tv_series_b:
            tv_series_b = choice(tv_series)

        # print details of tv series B
        print("TV Series B -")
        print_tv_series(tv_series_b,  False)

        # compare ratings by calling answer function and have the correct tv series name as an answer
        correct_answer = answer(tv_series_a['rating'], tv_series_b['rating'])

        # ask user to choose a movie by typing A or B
        user_choice = input(
            "\nWhich TV Series Have Higher IMDb Rating?\nType 'A' or 'B' - ").lower()

        # if correct A: then score will increase by 1
        # if correct B: then score will increase by 1 and tv series B will be the tv series A in next round
        # if failed: print wrong answer message and show the final score
        if user_choice == 'a' and correct_answer == tv_series_a['rating']:
            score += 1
        elif user_choice == 'b' and correct_answer == tv_series_b['rating']:
            tv_series_a = tv_series_b
            score += 1
        else:
            print(f'Wrong Answer. Your final score is - {score}')

            # ask user to play again
            user_play_game = input(
                "Do you want to play again? Type 'Y' or 'N' - ").lower()
            if user_play_game == 'n':
                user_play = False
                print("\nThank you for using the program. Goodbye!")
            else:
                # reset the score
                score = 0


# define clear to clear the console
def clear(): return system('cls')


# start game by calling this function
play_game()
