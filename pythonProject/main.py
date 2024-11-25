# This is a sample Python script.
import random

from models.player import Player

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
num_turns = 0


def start_turn(player, dice_left, last_turn_score):
    if dice_left == 0:
        player.roll_dice(6)
    else:
        



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    players = []
    player1 = Player()
    player2 = Player()
    player3 = Player()
    players.append(player1)
    players.append(player2)
    players.append(player3)
    for player in players:
        start_turn(player, 0, 0)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
