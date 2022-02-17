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


# Update players points
def update_players_rating(players_rating: list, players_point: list) -> None:
    with open("rating.txt", "w") as file:
        updated_rating = ''

        for player in players_rating:
            if player[0] == players_point[0]:
                player[1] = players_point[1]

            updated_rating += ":".join(player) + '\n'

        file.write(updated_rating)


# Append new player to the end of rating
def append_new_player_to_rating(players_point: list) -> None:
    with open("rating.txt", "a") as file:
        file.write(":".join(players_point) + '\n')


# rating = get_players_rating()
# nikita_points = check_player_in_rating(rating, 'Nikita')
# update_players_rating(rating, ['Nikita', '230'])
# append_new_player_to_rating(['Alex', '50'])
