from typing import Union


# Return list of rating
def get_players_rating() -> list:
    with open("rating.txt") as file:
        return [(player.strip()).split(':') for player in file.readlines()]


# Find name in rating.txt and return users points or return None if user not found
def check_player_in_rating(players_rating: list, name: str) -> Union[list, None]:
    for player in players_rating:
        if player[0] == name:
            return player


# Update player points
def update_players_rating(players_rating: list, player_points: list) -> None:
    with open("rating.txt", "w") as file:
        updated_rating = ''

        for player in players_rating:
            if player[0] == player_points[0]:
                player[1] = player_points[1]

            updated_rating += ":".join(player) + '\n'

        file.write(updated_rating)


# Append new player to the end of rating
def append_new_player_to_rating(player_points: list) -> None:
    with open("rating.txt", "a") as file:
        file.write(":".join(player_points) + '\n')


# Start fight
def start_fight(users_choice: str, programs_choice: str) -> str:
    from game import ALL_ITEMS

    # Draw
    if users_choice == programs_choice:
        return "Draw"

    else:
        slice_1 = len(ALL_ITEMS) - ALL_ITEMS.index(users_choice) - 1

        if slice_1 == 7:
            weaker_then_users_choice = ALL_ITEMS[8:]

        elif slice_1 < 7:
            slice_2 = 7 - slice_1
            weaker_then_users_choice = ALL_ITEMS[ALL_ITEMS.index(users_choice) + 1:]
            weaker_then_users_choice += ALL_ITEMS[:slice_2]

        else:
            weaker_then_users_choice = ALL_ITEMS[ALL_ITEMS.index(users_choice) + 1:ALL_ITEMS.index(users_choice) + 8]

        # User win
        if programs_choice in weaker_then_users_choice:
            return "Win"

        # User lose
        else:
            return "Lose"


