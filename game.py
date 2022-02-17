import random

from functions import get_players_rating, check_player_in_rating, update_players_rating, append_new_player_to_rating, start_fight
import pyinputplus as pyip

ALL_ITEMS = ['rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf', 'sponge',
             'paper', 'air', 'water', 'dragon', 'devil', 'lightning', 'gun']


if __name__ == '__main__':
    players_rating = get_players_rating()

    name = pyip.inputStr("Enter your name: ")
    print(f"Hello, {name}!")
    player_points = check_player_in_rating(players_rating, name)

    # Users not found in rating list
    if player_points is None:
        append_new_player_to_rating([name, '0'])
        players_rating = get_players_rating()
        player_points = check_player_in_rating(players_rating, name)

    options = (pyip.inputStr("Please, set a list of options separated by a comma: ", strip=True, blank=True)).split(',')
    # Set default options If the user inputs an empty line
    if options == ['']:
        options = ['rock', 'paper', 'scissors']

    print("Okay, let's start!")

    score = 0
    # Start the game
    while True:
        users_input = pyip.inputStr("Input your choice (!exit to stop the game): ", strip=True)

        # User stopped the game
        if users_input == '!exit':
            player_points[1] = str(int(player_points[1]) + score)
            update_players_rating(players_rating, [player_points[0], player_points[1]])

            print("Bye!")
            break

        elif users_input not in options:  # Invalid input
            print("Invalid input!")

        else:  # Correct input
            programs_choice = random.choice(options)
            result = start_fight(users_input, programs_choice)

            if result == "Draw":
                score += 50
                print(f"Draw -> There is a draw ({programs_choice})")

            elif result == "Win":
                score += 100
                print(f"Win -> Well done. The computer chose {programs_choice} and failed")

            else:
                print(f"Lose -> Sorry, but the computer chose {programs_choice}")
